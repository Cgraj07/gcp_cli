#!/usr/bin/env python3
"""
Basic usage examples for GCP CLI library.
"""

from gcp_cli import GCPCommandExecutor, ConfigManager, CredentialManager


def example_1_basic_usage():
    """Example 1: Basic command execution with defaults."""
    print("=" * 60)
    print("Example 1: Basic Usage")
    print("=" * 60)
    
    # Use default configuration and credentials
    executor = GCPCommandExecutor()
    
    # Execute a simple query
    result = executor.execute_natural_query(
        query="list all cloud storage buckets",
        preview=True,
        dry_run=True  # Just generate code, don't execute
    )
    
    print(f"Generated code:\n{result['code']}")
    print()


def example_2_with_config():
    """Example 2: Using custom configuration."""
    print("=" * 60)
    print("Example 2: Custom Configuration")
    print("=" * 60)
    
    # Create custom configuration
    config = ConfigManager()
    config.set('project_id', 'my-gcp-project')
    config.set('location', 'us-east1')
    config.set('preview_before_execute', False)  # Auto-execute
    
    # Initialize with custom config
    executor = GCPCommandExecutor(config=config)
    
    # Execute command
    result = executor.execute_natural_query(
        query="list all compute instances in us-east1",
        dry_run=True
    )
    
    print(f"Query: {result['query']}")
    print(f"Code generated: {len(result['code'])} characters")
    print()


def example_3_with_credentials():
    """Example 3: Using service account credentials."""
    print("=" * 60)
    print("Example 3: Service Account Credentials")
    print("=" * 60)
    
    # Set up credentials
    credentials = CredentialManager(
        credentials_path='/path/to/service-account.json'
    )
    
    # Initialize executor
    executor = GCPCommandExecutor(credentials=credentials)
    
    # Execute command
    result = executor.execute_natural_query(
        query="list all IAM service accounts",
        dry_run=True
    )
    
    print(f"Using credentials: {credentials.credentials_path}")
    print(f"Project ID: {credentials.get_project_id()}")
    print()


def example_4_advanced_query():
    """Example 4: Complex query with additional context."""
    print("=" * 60)
    print("Example 4: Advanced Query with Context")
    print("=" * 60)
    
    executor = GCPCommandExecutor()
    
    # Provide additional context for better code generation
    additional_context = """
    I need to filter instances that are running.
    Also, show the instance name, zone, and status.
    Format the output as a table.
    """
    
    result = executor.execute_natural_query(
        query="list compute instances",
        additional_context=additional_context,
        dry_run=True
    )
    
    print(f"Generated code:\n{result['code']}")
    print()


def example_5_from_config_file():
    """Example 5: Load configuration from file."""
    print("=" * 60)
    print("Example 5: Load from Config File")
    print("=" * 60)
    
    # Create a sample config
    config = ConfigManager()
    config.set('project_id', 'example-project')
    config.set('location', 'us-west1')
    config.set('model', 'gemini-1.5-pro')
    config.save_config('example_config.yaml')
    
    # Load from config file
    config_from_file = ConfigManager(config_path='example_config.yaml')
    
    print(f"Loaded config:")
    print(f"  Project: {config_from_file.get('project_id')}")
    print(f"  Location: {config_from_file.get('location')}")
    print(f"  Model: {config_from_file.get('model')}")
    print()


def example_6_error_handling():
    """Example 6: Error handling."""
    print("=" * 60)
    print("Example 6: Error Handling")
    print("=" * 60)
    
    executor = GCPCommandExecutor()
    
    # This might generate invalid code or fail
    result = executor.execute_natural_query(
        query="do something impossible that will fail",
        dry_run=True
    )
    
    if result['error']:
        print(f"Error occurred: {result['error']}")
    else:
        print("Command executed successfully")
    
    print()


if __name__ == '__main__':
    print("\n" + "=" * 60)
    print("GCP CLI Library - Usage Examples")
    print("=" * 60 + "\n")
    
    # Run examples
    try:
        example_1_basic_usage()
        example_2_with_config()
        # example_3_with_credentials()  # Requires valid credentials
        example_4_advanced_query()
        example_5_from_config_file()
        example_6_error_handling()
        
        print("=" * 60)
        print("All examples completed!")
        print("=" * 60)
        
    except Exception as e:
        print(f"Error running examples: {e}")
        print("\nNote: Some examples require valid GCP credentials to run.")
