"""
AI-powered command generation using Vertex AI Gemini.
"""

import logging
import vertexai
from vertexai.generative_models import GenerativeModel
from typing import Optional, Dict, Any
from .config import ConfigManager
from .credentials import CredentialManager

logger = logging.getLogger(__name__)


class AICommandGenerator:
    """Generates GCP commands using Vertex AI Gemini."""
    
    def __init__(
        self,
        config: Optional[ConfigManager] = None,
        credentials: Optional[CredentialManager] = None
    ):
        """
        Initialize AI command generator.
        
        Args:
            config: Configuration manager
            credentials: Credential manager
        """
        self.config = config or ConfigManager()
        self.credentials = credentials or CredentialManager()
        
        # Initialize Vertex AI
        project_id = self.config.get('project_id') or self.credentials.get_project_id()
        location = self.config.get('location', 'us-central1')
        
        if not project_id:
            raise ValueError("Project ID not found. Set it in config or credentials.")
        
        vertexai.init(project=project_id, location=location)
        
        # Initialize model
        model_name = self.config.get('model', 'gemini-3-flash-preview')
        self.model = GenerativeModel(model_name)
        
        logger.info(f"Initialized AI generator with model: {model_name}")
    
    def generate_command(
        self,
        query: str,
        credentials_path: Optional[str] = None,
        additional_context: Optional[str] = None
    ) -> str:
        """
        Generate GCP Python command from natural language query.
        
        Args:
            query: Natural language query (e.g., "list all compute instances")
            credentials_path: Optional credentials path to include in script
            additional_context: Optional additional context for generation
            
        Returns:
            Generated Python code as string
        """
        # Build prompt
        prompt = self._build_prompt(query, credentials_path, additional_context)
        
        # Get generation config
        generation_config = self.config.get_generation_config()
        
        # Generate code
        logger.info(f"Generating command for query: {query}")
        
        try:
            responses = self.model.generate_content(
                [prompt, query],
                generation_config=generation_config,
                stream=True
            )
            
            generated_text = ""
            for response in responses:
                generated_text += response.text
            
            # Clean the generated code
            clean_code = self._clean_code(generated_text)
            
            logger.debug(f"Generated code:\n{clean_code}")
            return clean_code
            
        except Exception as e:
            logger.error(f"Failed to generate command: {e}")
            raise
    
    def _build_prompt(
        self,
        query: str,
        credentials_path: Optional[str] = None,
        additional_context: Optional[str] = None
    ) -> str:
        """
        Build prompt for code generation.
        
        Args:
            query: User query
            credentials_path: Optional credentials path
            additional_context: Optional additional context
            
        Returns:
            Formatted prompt string
        """
        # Get credentials path from config if not provided
        if not credentials_path:
            credentials_path = self.config.get('credentials_path')
        
        prompt = """You are an expert GCP engineer. Generate ONLY Python code to accomplish the requested GCP task.

Requirements:
1. Return ONLY the Python code, no explanations or markdown formatting
2. Use official Google Cloud client libraries (google-cloud-*)
3. Include proper error handling
4. Add informative print statements for output
5. Make the code production-ready and well-commented
"""
        
        if credentials_path:
            prompt += f"""6. Use this credentials path for authentication: '{credentials_path}'
   Set credentials like: os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '{credentials_path}'
"""
        else:
            prompt += """6. Use Application Default Credentials (no explicit credentials path needed)
"""
        
        if additional_context:
            prompt += f"\nAdditional Context:\n{additional_context}\n"
        
        prompt += "\nGenerate the Python code now:\n"
        
        return prompt
    
    def _clean_code(self, generated_text: str) -> str:
        """
        Clean generated code by removing markdown formatting.
        
        Args:
            generated_text: Raw generated text
            
        Returns:
            Cleaned Python code
        """
        # Remove markdown code blocks
        lines = generated_text.splitlines()
        
        # Find the start and end of code block
        start_idx = 0
        end_idx = len(lines)
        
        for i, line in enumerate(lines):
            if line.strip().startswith('```'):
                if start_idx == 0:
                    start_idx = i + 1
                else:
                    end_idx = i
                    break
        
        # Extract code lines (skip markdown fence)
        if start_idx > 0 or end_idx < len(lines):
            code_lines = lines[start_idx:end_idx]
        else:
            code_lines = lines
        
        # Join and return
        clean_code = '\n'.join(code_lines)
        
        return clean_code.strip()
    
    def validate_code(self, code: str) -> bool:
        """
        Validate generated Python code.
        
        Args:
            code: Python code to validate
            
        Returns:
            True if code is valid Python
        """
        try:
            compile(code, '<string>', 'exec')
            return True
        except SyntaxError as e:
            logger.error(f"Code validation failed: {e}")
            return False
