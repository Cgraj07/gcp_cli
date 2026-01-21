"""
Utility functions for GCP CLI.
"""

import logging
import os
from datetime import datetime
from pathlib import Path
from typing import Optional
from rich.console import Console
from rich.syntax import Syntax
from rich.panel import Panel
from rich.logging import RichHandler

console = Console()


def setup_logging(level: str = "INFO", log_file: Optional[str] = None):
    """
    Set up logging with Rich handler.
    
    Args:
        level: Logging level (DEBUG, INFO, WARNING, ERROR)
        log_file: Optional path to log file
    """
    handlers = [RichHandler(rich_tracebacks=True, console=console)]
    
    if log_file:
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(
            logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        )
        handlers.append(file_handler)
    
    logging.basicConfig(
        level=getattr(logging, level.upper()),
        format="%(message)s",
        datefmt="[%X]",
        handlers=handlers
    )


def print_code(code: str, language: str = "python", title: Optional[str] = None):
    """
    Print code with syntax highlighting.
    
    Args:
        code: Code to print
        language: Programming language for syntax highlighting
        title: Optional title for the code panel
    """
    syntax = Syntax(code, language, theme="monokai", line_numbers=True)
    if title:
        console.print(Panel(syntax, title=title, expand=False))
    else:
        console.print(syntax)


def print_success(message: str):
    """Print success message."""
    console.print(f"[bold green]✓[/bold green] {message}")


def print_error(message: str):
    """Print error message."""
    console.print(f"[bold red]✗[/bold red] {message}")


def print_warning(message: str):
    """Print warning message."""
    console.print(f"[bold yellow]⚠[/bold yellow] {message}")


def print_info(message: str):
    """Print info message."""
    console.print(f"[bold blue]ℹ[/bold blue] {message}")


def confirm_action(prompt: str, default: bool = False) -> bool:
    """
    Ask user for confirmation.
    
    Args:
        prompt: Confirmation prompt
        default: Default value if user just presses enter
        
    Returns:
        True if user confirms, False otherwise
    """
    default_str = "Y/n" if default else "y/N"
    response = console.input(f"{prompt} [{default_str}]: ").strip().lower()
    
    if not response:
        return default
    
    return response in ['y', 'yes']


def save_command_history(command: str, history_file: Optional[str] = None):
    """
    Save command to history file.
    
    Args:
        command: Command to save
        history_file: Path to history file
    """
    if not history_file:
        history_dir = Path.home() / '.gcp_cli'
        history_dir.mkdir(exist_ok=True)
        history_file = history_dir / 'history.txt'
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(history_file, 'a') as f:
        f.write(f"[{timestamp}] {command}\n")


def get_command_history(history_file: Optional[str] = None, limit: int = 10) -> list:
    """
    Get recent command history.
    
    Args:
        history_file: Path to history file
        limit: Maximum number of commands to return
        
    Returns:
        List of recent commands
    """
    if not history_file:
        history_dir = Path.home() / '.gcp_cli'
        history_file = history_dir / 'history.txt'
    
    if not os.path.exists(history_file):
        return []
    
    with open(history_file, 'r') as f:
        lines = f.readlines()
    
    return lines[-limit:] if len(lines) > limit else lines


def format_table_output(data: list, headers: list):
    """
    Format data as a table.
    
    Args:
        data: List of rows
        headers: List of column headers
    """
    from rich.table import Table
    
    table = Table(show_header=True, header_style="bold magenta")
    
    for header in headers:
        table.add_column(header)
    
    for row in data:
        table.add_row(*[str(cell) for cell in row])
    
    console.print(table)
