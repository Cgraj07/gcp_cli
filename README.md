# GCP CLI

An AI-powered command-line interface for executing Google Cloud Platform commands using natural language.

## Features

🤖 **AI-Powered Command Generation** - Use Vertex AI Gemini to generate GCP Python scripts from natural language queries

🛡️ **Safe Execution** - Preview generated code before execution with user confirmation

🔑 **Flexible Authentication** - Support for service account JSON files and Application Default Credentials

💻 **Rich CLI Experience** - Beautiful terminal output with syntax highlighting and interactive mode

📦 **Modular Architecture** - Easy to extend and customize for different GCP services

## Installation

### Prerequisites

- Python 3.8 or higher
- Google Cloud Platform account with Vertex AI enabled
- GCP credentials (service account JSON or Application Default Credentials)

### Install from source

```bash
# Clone the repository
git clone https://github.com/Cgraj07/gcp-cli.git

# Install dependencies
pip install -r requirements.txt

# Install the package
pip install -e .
```

## Quick Start

### 1. Set up credentials

**Recommended: Use Application Default Credentials (ADC)**

```bash
# Authenticate once - credentials stored securely
gcloud auth application-default login
```

That's it! The library will automatically use these credentials.

<details>
<summary>Alternative: Service Account Key (Not recommended for local development)</summary>

**Only use this for CI/CD or production environments:**

```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/credentials.json"
```
</details>

### 2. Run your first command

```bash
# Execute a simple query
gcp-cli execute "list all compute instances in us-central1"

# Start interactive mode
gcp-cli interactive

# Run a Python script
gcp-cli run my_script.py
```

## Usage

### Execute Mode

Execute a natural language GCP command:

```bash
gcp-cli execute "list all cloud storage buckets"
gcp-cli execute "create a compute instance named test-vm in us-central1-a"
gcp-cli execute "list all IAM service accounts"
```

Options:
- `--no-preview`: Skip code preview and execute immediately
- `--dry-run`: Generate code without executing
- `--context`: Add additional context for code generation

### Interactive Mode

Start an interactive session for multiple commands:

```bash
gcp-cli interactive
```

In interactive mode, you can:
- Execute multiple commands in sequence
- View command history with `history` command
- Exit with `exit` or `quit`

### Run Script

Execute an existing Python script:

```bash
gcp-cli run my_gcp_script.py
```

### Configuration

Create a configuration file:

```bash
gcp-cli init-config --output myconfig.yaml
```

Example config file (`myconfig.yaml`):

```yaml
project_id: my-project
location: us-central1
model: gemini-2.0-flash-exp
max_output_tokens: 8192
temperature: 1.0
top_p: 0.95
preview_before_execute: true
log_level: INFO
```

> **Note:** Authentication uses Application Default Credentials (ADC).  
> Run `gcloud auth application-default login` before using the library.

Use a config file:

```bash
gcp-cli --config myconfig.yaml execute "list all instances"
```

### View Information

Display current configuration:

```bash
gcp-cli info
```

View command history:

```bash
gcp-cli history
```

## Python API

You can also use GCP CLI as a Python library:

```python
from gcp_cli import GCPCommandExecutor, ConfigManager, CredentialManager

# Initialize
config = ConfigManager()
config.set('project_id', 'my-project')
config.set('location', 'us-central1')

credentials = CredentialManager(credentials_path='/path/to/creds.json')

executor = GCPCommandExecutor(config=config, credentials=credentials)

# Execute a query
result = executor.execute_natural_query(
    query="list all compute instances",
    preview=True,
    dry_run=False
)

print(result['output'])
```

## Command Examples

Here are some example queries you can try:

### Compute Engine
- "list all compute instances"
- "create a compute instance named my-vm in us-central1-a with machine type n1-standard-1"
- "stop the instance named my-vm"

### Cloud Storage
- "list all storage buckets"
- "create a storage bucket named my-bucket in us-central1"
- "upload file data.txt to bucket my-bucket"

### Cloud SQL
- "list all cloud sql instances"
- "create a postgres cloud sql instance named my-db"

### IAM
- "list all service accounts"
- "create a service account named my-sa"
- "list IAM roles for project"

## Configuration Options

| Option | Description | Default |
|--------|-------------|---------|
| `project_id` | GCP project ID | None (auto-detected from credentials) |
| `location` | Default GCP location | us-central1 |
| `model` | Vertex AI model to use | gemini-2.0-flash-exp |
| `max_output_tokens` | Max tokens for code generation | 8192 |
| `temperature` | Generation temperature | 1.0 |
| `top_p` | Generation top_p | 0.95 |
| `preview_before_execute` | Show preview before execution | true |
| `log_level` | Logging level | INFO |

## Environment Variables

You can override configuration with environment variables:

- `GOOGLE_APPLICATION_CREDENTIALS`: Path to credentials JSON
- `GCP_CLI_PROJECT_ID`: Project ID
- `GCP_CLI_LOCATION`: GCP location
- `GCP_CLI_MODEL`: Model name

## Safety Features

- **Code Preview**: Review generated code before execution
- **User Confirmation**: Explicit confirmation required (unless `--no-preview`)
- **Dry Run Mode**: Test code generation without execution
- **Command History**: Track all executed commands
- **Error Handling**: Comprehensive error messages and logging
- **Timeout Protection**: 5-minute execution timeout

## Project Structure

```
Cloud_AI/
├── gcp_cli/
│   ├── __init__.py          # Package initialization
│   ├── cli.py               # CLI interface
│   ├── executor.py          # Command execution
│   ├── ai_generator.py      # AI code generation
│   ├── credentials.py       # Credential management
│   ├── config.py            # Configuration handling
│   └── utils.py             # Utility functions
├── examples/
│   └── basic_usage.py       # Usage examples
├── setup.py                 # Package setup
├── requirements.txt         # Dependencies
└── README.md               # This file
```

## Development

### Running Tests

```bash
# Install development dependencies
pip install pytest pytest-cov

# Run tests
pytest tests/
```

### Contributing

Contributions are welcome! Please ensure:
- Code follows PEP 8 style guidelines
- All tests pass
- New features include tests and documentation

## Troubleshooting

### "Failed to validate GCP credentials"

Authenticate with gcloud:
```bash
gcloud auth application-default login
```

### "Project ID not found"

Provide project ID via:
- Config file: `project_id: my-project`
- Command line: `--project my-project`
- Environment: `export GCP_CLI_PROJECT_ID=my-project`

### "Model not found"

Ensure Vertex AI is enabled in your project:
```bash
gcloud services enable aiplatform.googleapis.com
```

## License

MIT License - see LICENSE file for details

## Support

For issues and questions:
- Open an issue on GitHub
- Check the documentation
- Review existing issues for similar problems

## Acknowledgments

Built with:
- [Vertex AI](https://cloud.google.com/vertex-ai) - AI-powered code generation
- [Click](https://click.palletsprojects.com/) - CLI framework
- [Rich](https://rich.readthedocs.io/) - Terminal formatting
- Google Cloud Client Libraries
