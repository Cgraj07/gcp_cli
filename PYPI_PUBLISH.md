# Publishing to PyPI (Python Package Index)

## 🎉 Good News!

Your library is **already published** on GitHub and users can install it with:

```bash
pip install git+https://github.com/YOUR_USERNAME/gcp-cli.git
```

---

## 📦 To Publish on PyPI (Optional but Recommended)

Publishing on PyPI allows users to install with just:

```bash
pip install gcp-cli
```

### Step 1: Update `setup.py`

Make sure your `setup.py` has proper metadata:

```python
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="gcp-cli-ai",  # Must be unique on PyPI
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="AI-powered CLI for executing GCP commands using natural language",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YOUR_USERNAME/gcp-cli",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Systems Administration",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=[
        "google-cloud-aiplatform>=1.38.0",
        "click>=8.1.0",
        "PyYAML>=6.0",
        "rich>=13.0.0",
        "google-auth>=2.23.0",
        "google-cloud-storage>=2.10.0",
    ],
    entry_points={
        "console_scripts": [
            "gcp-cli=gcp_cli.cli:main",
        ],
    },
    keywords="gcp google-cloud cli ai gemini vertex-ai automation",
)
```

### Step 2: Install Build Tools

```bash
pip install --upgrade build twine
```

### Step 3: Build the Package

```bash
cd /Users/govind/Desktop/Govind/projects/Cloud_AI

# Build distribution files
python3 -m build
```

This creates:
- `dist/gcp-cli-ai-0.1.0.tar.gz` (source distribution)
- `dist/gcp_cli_ai-0.1.0-py3-none-any.whl` (wheel)

### Step 4: Test Upload to TestPyPI (Recommended First)

```bash
# Create account at https://test.pypi.org/ first

# Upload to TestPyPI
python3 -m twine upload --repository testpypi dist/*
```

Test installation:
```bash
pip install --index-url https://test.pypi.org/simple/ gcp-cli-ai
```

### Step 5: Upload to PyPI

```bash
# Create account at https://pypi.org/ first

# Upload to PyPI
python3 -m twine upload dist/*
```

Users can now install with:
```bash
pip install gcp-cli-ai
```

---

## 🏷️ Create a GitHub Release

### Option 1: Via GitHub Web UI

1. Go to your repository on GitHub
2. Click "Releases" → "Create a new release"
3. **Tag**: `v0.1.0`
4. **Release title**: `v0.1.0 - Initial Release`
5. **Description**:

```markdown
# GCP CLI v0.1.0 - Initial Release

AI-powered CLI for executing Google Cloud Platform commands using natural language.

## ✨ Features

- 🤖 Natural language to GCP Python code using Vertex AI Gemini
- 🛡️ Safe execution with preview mode
- 🔐 Application Default Credentials (no hardcoded keys!)
- 💻 Rich CLI experience with syntax highlighting
- 📦 Python library API
- 🎯 Interactive mode

## 📦 Installation

```bash
pip install git+https://github.com/YOUR_USERNAME/gcp-cli.git
```

## 🚀 Quick Start

```bash
# Authenticate
gcloud auth application-default login

# Execute GCP commands
gcp-cli execute "list all cloud storage buckets"

# Interactive mode
gcp-cli interactive
```

## 📚 Documentation

See [README.md](https://github.com/YOUR_USERNAME/gcp-cli) for full documentation.

## 🙏 Acknowledgments

Built with Google Vertex AI, Click, and Rich.
```

6. **Upload assets** (optional):
   - Attach `dist/*.tar.gz` and `dist/*.whl` files from your build

7. Click **"Publish release"**

### Option 2: Via GitHub CLI

```bash
# Install gh CLI if needed
brew install gh

# Create release
gh release create v0.1.0 \
  --title "v0.1.0 - Initial Release" \
  --notes "AI-powered CLI for GCP commands. See README for details." \
  dist/*.tar.gz dist/*.whl
```

---

## 📝 Update README with Installation Badge

Add to your `README.md`:

```markdown
[![GitHub release](https://img.shields.io/github/v/release/YOUR_USERNAME/gcp-cli)](https://github.com/YOUR_USERNAME/gcp-cli/releases)
[![PyPI version](https://badge.fury.io/py/gcp-cli-ai.svg)](https://pypi.org/project/gcp-cli-ai/)
```

---

## 🔄 For Future Updates

### Update Version

1. Edit `setup.py` - change version to `0.1.1`, `0.2.0`, etc.
2. Commit changes
3. Create new tag: `git tag v0.1.1`
4. Push tag: `git push --tags`
5. Create GitHub release
6. Rebuild and upload to PyPI:
   ```bash
   python3 -m build
   python3 -m twine upload dist/*
   ```

---

## ✅ Current Status

Your library is **already published and usable**! Anyone can install with:

```bash
pip install git+https://github.com/YOUR_USERNAME/gcp-cli.git
```

**Optional next steps:**
- ⭐ Publish to PyPI (makes it easier to discover and install)
- 🏷️ Create a GitHub Release (professional touch)
- 📊 Add badges to README
- 📢 Share on social media or Reddit (r/Python, r/googlecloud)

---

## 🎯 Quick Publish Script

Save this as `publish.sh`:

```bash
#!/bin/bash

# Quick publish script
set -e

echo "🔨 Building package..."
python3 -m build

echo "🧪 Uploading to TestPyPI..."
python3 -m twine upload --repository testpypi dist/*

echo "✅ Test installation:"
echo "pip install --index-url https://test.pypi.org/simple/ gcp-cli-ai"
echo ""
echo "If test works, upload to PyPI with:"
echo "python3 -m twine upload dist/*"
```

Make executable:
```bash
chmod +x publish.sh
./publish.sh
```

---

## 🎊 Congratulations!

Your library is **live** and ready for the world! 🚀
