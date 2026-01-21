#!/usr/bin/env python3
"""
GCP CLI - AI-powered command line interface for Google Cloud Platform.
"""

import click
import logging
from pathlib import Path
from .executor import GCPCommandExecutor
from .config import ConfigManager
from .credentials import CredentialManager
from .utils import (
    setup_logging,
    print_success,
    print_error,
    print_info,
    get_command_history,
    console
)

logger = logging.getLogger(__name__)


@click.group()
@click.option('--config', '-c', type=click.Path(exists=True), help='Path to config file')
@click.option('--credentials', type=click.Path(exists=True), help='Path to service account JSON')
@click.option('--project', '-p', help='GCP project ID')
@click.option('--location', '-l', default='us-central1', help='GCP location')
@click.option('--log-level', default='INFO', help='Logging level')
@click.pass_context
def cli(ctx, config, credentials, project, location, log_level):
    """GCP CLI - AI-powered command execution for Google Cloud Platform."""
    
    # Set up logging
    setup_logging(level=log_level)
    
    # Initialize configuration
    config_manager = ConfigManager(config_path=config)
    
    # Override with command line arguments
    if project:
        config_manager.set('project_id', project)
    if location:
        config_manager.set('location', location)
    if credentials:
        config_manager.set('credentials_path', credentials)
    
    # Initialize credentials
    credentials_path = config_manager.get('credentials_path')
    credential_manager = CredentialManager(credentials_path=credentials_path)
    
    # Validate credentials
    if not credential_manager.validate():
        print_error("Failed to validate GCP credentials")
        ctx.exit(1)
    
    # Initialize executor
    executor = GCPCommandExecutor(
        config=config_manager,
        credentials=credential_manager
    )
    
    # Store in context
    ctx.obj = {
        'executor': executor,
        'config': config_manager,
        'credentials': credential_manager
    }


@cli.command()
@click.argument('query', nargs=-1, required=True)
@click.option('--no-preview', is_flag=True, help='Skip preview and execute immediately')
@click.option('--dry-run', is_flag=True, help='Generate code without executing')
@click.option('--context', help='Additional context for code generation')
@click.pass_context
def execute(ctx, query, no_preview, dry_run, context):
    """Execute a natural language GCP command.
    
    Example:
        gcp-cli execute "list all compute instances in us-central1"
    """
    executor = ctx.obj['executor']
    
    # Join query parts
    query_str = ' '.join(query)
    
    print_info(f"Query: {query_str}")
    
    # Execute query
    result = executor.execute_natural_query(
        query=query_str,
        preview=not no_preview,
        dry_run=dry_run,
        additional_context=context
    )
    
    # Display output
    if result['output']:
        console.print("\n[bold]Output:[/bold]")
        console.print(result['output'])
    
    if result['error']:
        ctx.exit(1)


@cli.command()
@click.pass_context
def interactive(ctx):
    """Start interactive mode for conversational command execution.
    
    In interactive mode, you can have a conversation with the AI to
    execute multiple GCP commands in sequence.
    """
    executor = ctx.obj['executor']
    
    console.print("[bold green]GCP CLI Interactive Mode[/bold green]")
    console.print("Type your GCP commands in natural language. Type 'exit' or 'quit' to exit.\n")
    
    while True:
        try:
            # Get user input
            query = console.input("[bold blue]gcp>[/bold blue] ").strip()
            
            if not query:
                continue
            
            if query.lower() in ['exit', 'quit', 'q']:
                print_info("Goodbye!")
                break
            
            # Special commands
            if query.lower() == 'history':
                history = get_command_history()
                console.print("\n[bold]Command History:[/bold]")
                for entry in history:
                    console.print(entry.strip())
                console.print()
                continue
            
            # Execute query
            result = executor.execute_natural_query(
                query=query,
                preview=True,
                dry_run=False
            )
            
            # Display output
            if result['output']:
                console.print("\n[bold]Output:[/bold]")
                console.print(result['output'])
                console.print()
            
        except KeyboardInterrupt:
            console.print("\n")
            print_info("Use 'exit' to quit")
        except Exception as e:
            print_error(f"Error: {e}")


@cli.command()
@click.argument('script_path', type=click.Path(exists=True))
@click.option('--no-preview', is_flag=True, help='Skip preview and execute immediately')
@click.pass_context
def run(ctx, script_path, no_preview):
    """Execute a Python script file.
    
    Example:
        gcp-cli run my_script.py
    """
    executor = ctx.obj['executor']
    
    result = executor.execute_script_file(
        script_path=script_path,
        preview=not no_preview
    )
    
    # Display output
    if result['output']:
        console.print("\n[bold]Output:[/bold]")
        console.print(result['output'])
    
    if result['error']:
        ctx.exit(1)


@cli.command()
@click.pass_context
def history(ctx):
    """Show command history."""
    history_entries = get_command_history(limit=20)
    
    if not history_entries:
        print_info("No command history found")
        return
    
    console.print("[bold]Command History:[/bold]\n")
    for entry in history_entries:
        console.print(entry.strip())


@cli.command()
@click.option('--output', '-o', default='gcp_cli_config.yaml', help='Output config file path')
@click.pass_context
def init_config(ctx, output):
    """Initialize a configuration file with defaults.
    
    Example:
        gcp-cli init-config --output myconfig.yaml
    """
    config = ctx.obj['config']
    config.save_config(output)
    print_success(f"Configuration saved to {output}")


@cli.command()
@click.pass_context
def info(ctx):
    """Display current configuration and credentials info."""
    config = ctx.obj['config']
    credentials = ctx.obj['credentials']
    
    console.print("[bold]GCP CLI Configuration:[/bold]\n")
    console.print(f"Project ID: {config.get('project_id') or credentials.get_project_id()}")
    console.print(f"Location: {config.get('location')}")
    console.print(f"Model: {config.get('model')}")
    console.print(f"Credentials Path: {credentials.credentials_path or 'Using ADC'}")
    console.print(f"Preview Mode: {config.get('preview_before_execute')}")


def main():
    """Main entry point."""
    cli(obj={})


if __name__ == '__main__':
    main()
