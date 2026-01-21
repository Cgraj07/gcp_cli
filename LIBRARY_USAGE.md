# How to Use GCP CLI as a Library

Your project is **already set up as a library**! Here's how to use it:

---

## ✅ Already Done

Your project has all the required library files:
- ✅ `setup.py` - Package configuration
- ✅ `gcp_cli/` - Main package directory
- ✅ `gcp_cli/__init__.py` - Exports main classes
- ✅ `requirements.txt` - Dependencies

---

## 📦 Install as a Library

### Option 1: Install in Development Mode (Recommended for Development)
```bash
cd /Users/govind/Desktop/Govind/projects/Cloud_AI
pip install -e .
```

**Benefits:**
- ✅ Changes to code are immediately available
- ✅ No need to reinstall after editing
- ✅ Perfect for development

### Option 2: Regular Install
```bash
cd /Users/govind/Desktop/Govind/projects/Cloud_AI
pip install .
```

### Option 3: Install from Anywhere
```bash
pip install /Users/govind/Desktop/Govind/projects/Cloud_AI
```

---

## 🐍 Use in Python Scripts

Once installed, you can use it in **any Python script**:

### Example 1: Basic Usage
```python
#!/usr/bin/env python3
from gcp_cli import GCPCommandExecutor

# Create executor (uses default config)
executor = GCPCommandExecutor()

# Execute a query
result = executor.execute_natural_query(
    query="list all cloud storage buckets",
    preview=False,  # No preview
    dry_run=True    # Safe mode - no execution
)

# Access results
print("Generated Code:")
print(result['code'])

if result['error']:
    print(f"Error: {result['error']}")
```

### Example 2: With Custom Configuration
```python
from gcp_cli import GCPCommandExecutor, ConfigManager

# Load your config file
config = ConfigManager(config_path='example_config.yaml')

# Create executor with config
executor = GCPCommandExecutor(config=config)

# Execute query
result = executor.execute_natural_query(
    query="list compute instances in us-central1"
)

print(result['output'])
```

### Example 3: With Custom Credentials
```python
from gcp_cli import GCPCommandExecutor, CredentialManager

# Set up credentials
credentials = CredentialManager(
    credentials_path='cs-agentspace-demos-c1d59a358865.json'
)

# Create executor
executor = GCPCommandExecutor(credentials=credentials)

# Use it
result = executor.execute_natural_query(
    query="list all service accounts"
)
```

### Example 4: Programmatic Configuration
```python
from gcp_cli import GCPCommandExecutor, ConfigManager

# Create config programmatically
config = ConfigManager()
config.set('project_id', 'cs-agentspace-demos')
config.set('location', 'us-central1')
config.set('model', 'gemini-3-flash-preview')
config.set('credentials_path', 'cs-agentspace-demos-c1d59a358865.json')

# Use it
executor = GCPCommandExecutor(config=config)
result = executor.execute_natural_query("show project details")
```

---

## 📝 Create Your Own Scripts

**Example Script:** `my_gcp_script.py`

```python
#!/usr/bin/env python3
"""
My custom GCP automation script using gcp_cli library.
"""

from gcp_cli import GCPCommandExecutor, ConfigManager

def list_all_resources():
    """List all GCP resources."""
    
    # Initialize with config
    config = ConfigManager(config_path='example_config.yaml')
    executor = GCPCommandExecutor(config=config)
    
    # List different resources
    resources = [
        "list all cloud storage buckets",
        "list all compute instances",
        "list all service accounts",
    ]
    
    for query in resources:
        print(f"\n{'='*60}")
        print(f"Query: {query}")
        print('='*60)
        
        result = executor.execute_natural_query(
            query=query,
            preview=False,  # No preview
            dry_run=False   # Actually execute
        )
        
        if result['output']:
            print(result['output'])
        
        if result['error']:
            print(f"Error: {result['error']}")

if __name__ == '__main__':
    list_all_resources()
```

Run it:
```bash
python3 my_gcp_script.py
```

---

## 🌍 Use from Anywhere

After installing with `pip install -e .`, you can:

### 1. Import in Any Python Script
```python
# From any directory
from gcp_cli import GCPCommandExecutor
```

### 2. Use the CLI Command
```bash
# From any directory
gcp-cli execute "list all buckets"
```

---

## 📦 Package Distribution (Optional)

### Create Distribution Files
```bash
cd /Users/govind/Desktop/Govind/projects/Cloud_AI
python3 setup.py sdist bdist_wheel
```

This creates:
- `dist/gcp-cli-0.1.0.tar.gz` - Source distribution
- `dist/gcp_cli-0.1.0-py3-none-any.whl` - Wheel distribution

### Install from Distribution
```bash
pip install dist/gcp-cli-0.1.0.tar.gz
```

### Share with Others
Send the `.tar.gz` or `.whl` file to others, and they can install it:
```bash
pip install gcp-cli-0.1.0.tar.gz
```

---

## 🚀 Quick Start for Library Usage

```bash
# 1. Install the library
cd /Users/govind/Desktop/Govind/projects/Cloud_AI
pip install -e .

# 2. Create a test script
cat > test_library.py << 'EOF'
from gcp_cli import GCPCommandExecutor

executor = GCPCommandExecutor()
result = executor.execute_natural_query(
    query="list all cloud storage buckets",
    dry_run=True
)
print(result['code'])
EOF

# 3. Run it
python3 test_library.py
```

---

## Summary

✅ **Your project is already a library!**
- Install with: `pip install -e .`
- Import with: `from gcp_cli import GCPCommandExecutor`
- Use in any Python script
- Share as a package file (`.tar.gz` or `.whl`)

The library is ready to use! 🎉
