# GCP CLI

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

An AI-powered command-line interface for executing Google Cloud Platform commands using natural language.

Powered by **Google Vertex AI Gemini** to generate and execute GCP Python scripts from plain English queries.

## ✨ Features

🤖 **AI-Powered** - Generate GCP scripts from natural language using Vertex AI  
🛡️ **Safe Execution** - Preview code before running with user confirmation  
🔑 **Secure Authentication** - Uses Application Default Credentials (no hardcoded keys!)  
💻 **Rich CLI** - Beautiful syntax highlighting and interactive mode  
📦 **Python Library** - Use programmatically in your own scripts  
🎯 **Easy Setup** - One command authentication with `gcloud auth`

## 🚀 Quick Start

### 1. Install

```bash
pip install git+https://github.com/yourusername/gcp-cli.git
```

Or clone and install locally:

```bash
git clone https://github.com/yourusername/gcp-cli.git
cd gcp-cli
pip install -e .
```

### 2. Authenticate

```bash
# One-time setup - authenticate with Google Cloud
gcloud auth application-default login
```

### 3. Use It!

```bash
# Execute GCP commands in natural language
gcp-cli execute "list all cloud storage buckets"

# Or start interactive mode
gcp-cli interactive
```

## 📖 Usage

### CLI Commands

```bash
# Execute a command (with preview)
gcp-cli execute "list all compute instances in us-central1"

# Dry-run (generate code without executing)
gcp-cli execute --dry-run "create a storage bucket"

# Auto-execute without preview
gcp-cli execute --no-preview "list service accounts"

# Interactive mode
gcp-cli interactive

# View configuration
gcp-cli info

# View command history
gcp-cli history
```

### Python API

```python
from gcp_cli import GCPCommandExecutor

# Initialize (uses ADC automatically)
executor = GCPCommandExecutor()

# Execute a query
result = executor.execute_natural_query(
    query="list all cloud storage buckets",
    preview=True
)

print(result['code'])    # Generated Python code
print(result['output'])  # Execution output
```

## 🔧 Configuration

Create a config file `~/.gcp_cli_config.yaml`:

```yaml
project_id: your-project-id
location: us-central1
model: gemini-2.0-flash-exp
preview_before_execute: true
log_level: INFO
```

Use it:

```bash
gcp-cli --config ~/.gcp_cli_config.yaml execute "list buckets"
```

## 🔐 Authentication

This library uses [Application Default Credentials (ADC)](https://cloud.google.com/docs/authentication/application-default-credentials):

```bash
# For local development
gcloud auth application-default login

# For GKE/Cloud Run/Cloud Functions
# ADC works automatically via Workload Identity
```

**Never commit credential files to git!** This library is designed to work without hardcoded credentials.

## 📚 Examples

```bash
# Cloud Storage
gcp-cli execute "list all storage buckets"
gcp-cli execute "create a bucket named my-bucket-123"

# Compute Engine
gcp-cli execute "list compute instances in us-central1"
gcp-cli execute "list all compute zones"

# IAM
gcp-cli execute "list all service accounts"
gcp-cli execute "show IAM roles for project"

# Cloud SQL
gcp-cli execute "list all cloud sql instances"
```

## 🛠️ Development

```bash
# Clone the repository
git clone https://github.com/yourusername/gcp-cli.git
cd gcp-cli

# Install in development mode
pip install -e .

# Run tests
pytest tests/
```

## 📄 Documentation

- [Full README](README.md) - Complete documentation
- [Authentication Guide](AUTHENTICATION.md) - Setup and security
- [Testing Guide](TESTING_GUIDE.md) - How to test the library
- [Library Usage](LIBRARY_USAGE.md) - Python API details
- [Quick Reference](QUICK_REFERENCE.md) - Command cheat sheet

## 🤝 Contributing

Contributions welcome! Please ensure:
- Code follows PEP 8
- Tests pass
- Documentation is updated
- No credentials in commits

## 📝 License

MIT License - see [LICENSE](LICENSE) file

## ⚠️ Security

**NEVER commit GCP credentials to this repository!**

- ✅ Use `gcloud auth application-default login`
- ✅ Use Workload Identity on GCP services
- ❌ Don't hardcode credentials
- ❌ Don't commit `.json` key files

## 🙏 Acknowledgments

Built with:
- [Google Vertex AI](https://cloud.google.com/vertex-ai) - AI-powered code generation
- [Click](https://click.palletsprojects.com/) - CLI framework
- [Rich](https://rich.readthedocs.io/) - Terminal formatting

---

**Made with ❤️ for GCP developers**
