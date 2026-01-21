"""
Credential management for GCP authentication.
"""

import os
from pathlib import Path
from typing import Optional
from google.auth import default
from google.oauth2 import service_account
import logging

logger = logging.getLogger(__name__)


class CredentialManager:
    """Manages GCP credentials for authentication."""
    
    def __init__(self, credentials_path: Optional[str] = None):
        """
        Initialize credential manager.
        
        Args:
            credentials_path: Path to service account JSON file. If None, uses ADC.
        """
        self.credentials_path = credentials_path
        self._credentials = None
        self._project_id = None
    
    def get_credentials(self):
        """
        Get GCP credentials.
        
        Returns:
            Google credentials object
        """
        if self._credentials:
            return self._credentials
        
        if self.credentials_path:
            # Use service account credentials
            if not os.path.exists(self.credentials_path):
                raise FileNotFoundError(
                    f"Credentials file not found: {self.credentials_path}"
                )
            
            self._credentials = service_account.Credentials.from_service_account_file(
                self.credentials_path
            )
            logger.info(f"Loaded credentials from {self.credentials_path}")
        else:
            # Use Application Default Credentials
            self._credentials, self._project_id = default()
            logger.info("Using Application Default Credentials")
        
        return self._credentials
    
    def get_project_id(self) -> Optional[str]:
        """
        Get GCP project ID from credentials.
        
        Returns:
            Project ID string or None
        """
        if self._project_id:
            return self._project_id
        
        if self.credentials_path and os.path.exists(self.credentials_path):
            import json
            with open(self.credentials_path, 'r') as f:
                creds_data = json.load(f)
                self._project_id = creds_data.get('project_id')
        
        return self._project_id
    
    def set_environment_credentials(self):
        """Set GOOGLE_APPLICATION_CREDENTIALS environment variable."""
        if self.credentials_path:
            os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = self.credentials_path
            logger.info(f"Set GOOGLE_APPLICATION_CREDENTIALS to {self.credentials_path}")
    
    @classmethod
    def from_environment(cls) -> 'CredentialManager':
        """
        Create credential manager from environment variables.
        
        Returns:
            CredentialManager instance
        """
        creds_path = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')
        return cls(credentials_path=creds_path)
    
    def validate(self) -> bool:
        """
        Validate that credentials are working.
        
        Returns:
            True if credentials are valid
        """
        try:
            creds = self.get_credentials()
            return creds is not None
        except Exception as e:
            logger.error(f"Credential validation failed: {e}")
            return False
