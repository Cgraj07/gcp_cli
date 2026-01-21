"""
Configuration management for GCP CLI.
"""

import os
from pathlib import Path
from typing import Dict, Any, Optional
import yaml
import json
import logging

logger = logging.getLogger(__name__)


class ConfigManager:
    """Manages configuration for GCP CLI."""
    
    DEFAULT_CONFIG = {
        'project_id': None,
        'location': 'us-central1',
        'model': 'gemini-2.0-flash-exp',
        'max_output_tokens': 8192,
        'temperature': 1.0,
        'top_p': 0.95,
        'preview_before_execute': True,
        'log_level': 'INFO',
    }
    
    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize configuration manager.
        
        Args:
            config_path: Path to config file (YAML or JSON)
        """
        self.config_path = config_path
        self.config = self.DEFAULT_CONFIG.copy()
        
        if config_path:
            self.load_config(config_path)
    
    def load_config(self, config_path: str):
        """
        Load configuration from file.
        
        Args:
            config_path: Path to config file
        """
        if not os.path.exists(config_path):
            logger.warning(f"Config file not found: {config_path}")
            return
        
        try:
            with open(config_path, 'r') as f:
                if config_path.endswith('.yaml') or config_path.endswith('.yml'):
                    loaded_config = yaml.safe_load(f)
                elif config_path.endswith('.json'):
                    loaded_config = json.load(f)
                else:
                    logger.warning(f"Unsupported config file format: {config_path}")
                    return
                
                if loaded_config:
                    self.config.update(loaded_config)
                    logger.info(f"Loaded configuration from {config_path}")
        except Exception as e:
            logger.error(f"Failed to load config: {e}")
    
    def get(self, key: str, default: Any = None) -> Any:
        """
        Get configuration value.
        
        Args:
            key: Configuration key
            default: Default value if key not found
            
        Returns:
            Configuration value
        """
        # Check environment variables first
        env_key = f"GCP_CLI_{key.upper()}"
        env_value = os.environ.get(env_key)
        if env_value is not None:
            return env_value
        
        return self.config.get(key, default)
    
    def set(self, key: str, value: Any):
        """
        Set configuration value.
        
        Args:
            key: Configuration key
            value: Configuration value
        """
        self.config[key] = value
    
    def save_config(self, output_path: str):
        """
        Save current configuration to file.
        
        Args:
            output_path: Path to save config file
        """
        try:
            with open(output_path, 'w') as f:
                if output_path.endswith('.yaml') or output_path.endswith('.yml'):
                    yaml.dump(self.config, f, default_flow_style=False)
                elif output_path.endswith('.json'):
                    json.dump(self.config, f, indent=2)
                else:
                    logger.error(f"Unsupported config file format: {output_path}")
                    return
                
                logger.info(f"Saved configuration to {output_path}")
        except Exception as e:
            logger.error(f"Failed to save config: {e}")
    
    @classmethod
    def from_dict(cls, config_dict: Dict[str, Any]) -> 'ConfigManager':
        """
        Create configuration manager from dictionary.
        
        Args:
            config_dict: Configuration dictionary
            
        Returns:
            ConfigManager instance
        """
        manager = cls()
        manager.config.update(config_dict)
        return manager
    
    def get_generation_config(self) -> Dict[str, Any]:
        """
        Get Vertex AI generation configuration.
        
        Returns:
            Generation config dictionary
        """
        return {
            'max_output_tokens': self.get('max_output_tokens'),
            'temperature': self.get('temperature'),
            'top_p': self.get('top_p'),
        }
