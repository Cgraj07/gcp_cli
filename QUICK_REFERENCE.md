# GCP CLI - Quick Reference

## Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Install the package
pip install -e .
```

## Basic Commands

### Execute a Command
```bash
# Basic usage
gcp-cli execute "list all compute instances"

# With config file
gcp-cli --config myconfig.yaml execute "list storage buckets"

# Preview only (dry-run)
gcp-cli execute --dry-run "create a compute instance"

# No preview (auto-execute)
gcp-cli execute --no-preview "list IAM service accounts"

# With additional context
gcp-cli execute "list instances" --context "only show running instances"
```

### Interactive Mode
```bash
# Start interactive session
gcp-cli interactive

# Commands in interactive mode:
gcp> list all cloud storage buckets
gcp> create a compute instance in us-central1
gcp> history
gcp> exit
```

### Run a Script
```bash
gcp-cli run my_script.py
```

### View Information
```bash
# Show current configuration
gcp-cli info

# Show command history
gcp-cli history

# Create example config
gcp-cli init-config --output myconfig.yaml
```

## Configuration

### Config File (YAML)
```yaml
project_id: your-project-id
location: us-central1
credentials_path: /path/to/credentials.json
model: gemini-1.5-pro
max_output_tokens: 8192
temperature: 1.0
top_p: 0.95
preview_before_execute: true
log_level: INFO
```

### Environment Variables
```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/credentials.json"
export GCP_CLI_PROJECT_ID="your-project-id"
export GCP_CLI_LOCATION="us-central1"
```

### Command Line Options
```bash
--config PATH         # Config file path
--credentials PATH    # Service account JSON
--project TEXT        # GCP project ID
--location TEXT       # GCP location
--log-level TEXT      # Logging level
```

## Python API

### Basic Usage
```python
from gcp_cli import GCPCommandExecutor

executor = GCPCommandExecutor()
result = executor.execute_natural_query(
    query="list all compute instances",
    preview=True,
    dry_run=False
)
```

### With Custom Config
```python
from gcp_cli import GCPCommandExecutor, ConfigManager

config = ConfigManager()
config.set('project_id', 'my-project')
config.set('location', 'us-east1')

executor = GCPCommandExecutor(config=config)
```

### With Credentials
```python
from gcp_cli import GCPCommandExecutor, CredentialManager

credentials = CredentialManager(
    credentials_path='/path/to/creds.json'
)

executor = GCPCommandExecutor(credentials=credentials)
```

## Example Queries

### Compute Engine
```bash
"list all compute instances"
"create a compute instance named my-vm in us-central1-a"
"stop the instance named my-vm"
"delete instance my-vm"
```

### Cloud Storage
```bash
"list all storage buckets"
"create a storage bucket named my-bucket"
"upload file data.txt to bucket my-bucket"
"list files in bucket my-bucket"
```

### Cloud SQL
```bash
"list all cloud sql instances"
"create a postgres instance named my-db"
```

### IAM
```bash
"list all service accounts"
"create a service account named my-sa"
"list IAM roles for project"
```

## Tips

1. **Be Specific**: More specific queries generate better code
2. **Use Context**: Add `--context` for additional requirements
3. **Preview First**: Always review generated code in preview mode
4. **Use Dry-Run**: Test code generation with `--dry-run`
5. **Interactive Mode**: Use for multiple related commands
6. **History**: Review past commands with `history` command

## Troubleshooting

### Credentials Issue
```bash
# Set credentials path
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/creds.json"

# Or use ADC
gcloud auth application-default login
```

### Project ID Not Found
```bash
# Set in config file
project_id: my-project

# Or via command line
gcp-cli --project my-project execute "..."

# Or via environment
export GCP_CLI_PROJECT_ID=my-project
```

### Enable Vertex AI
```bash
gcloud services enable aiplatform.googleapis.com
```

## Safety Features

- ✅ Code preview before execution
- ✅ User confirmation required
- ✅ Dry-run mode available
- ✅ Command history tracking
- ✅ 5-minute timeout protection
- ✅ Comprehensive error messages

## For This Project

Your specific configuration:
```bash
# Using the example config
./bin/python3 -m gcp_cli.cli --config example_config.yaml info

# Execute a command
./bin/python3 -m gcp_cli.cli --config example_config.yaml execute "list all cloud storage buckets"

# Interactive mode
./bin/python3 -m gcp_cli.cli interactive
```
