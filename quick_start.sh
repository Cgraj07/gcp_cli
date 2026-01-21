#!/bin/bash

# Quick Start Script for GCP CLI
# This script helps you get started with the GCP CLI library

set -e

echo "================================================"
echo "GCP CLI - Quick Start Setup"
echo "================================================"
echo ""

# Check Python version
echo "1. Checking Python version..."
python3 --version || { echo "Error: Python 3 is required"; exit 1; }
echo "✓ Python installed"
echo ""

# Install dependencies
echo "2. Installing dependencies..."
pip install -r requirements.txt
echo "✓ Dependencies installed"
echo ""

# Install the package
echo "3. Installing GCP CLI..."
pip install -e .
echo "✓ GCP CLI installed"
echo ""

# Verify installation
echo "4. Verifying installation..."
gcp-cli --help > /dev/null 2>&1 || { echo "Error: Installation verification failed"; exit 1; }
echo "✓ Installation verified"
echo ""

echo "================================================"
echo "Setup Complete! 🎉"
echo "================================================"
echo ""
echo "Next steps:"
echo "1. Configure your GCP credentials:"
echo "   export GOOGLE_APPLICATION_CREDENTIALS=\"/path/to/your/credentials.json\""
echo ""
echo "2. Or set up Application Default Credentials:"
echo "   gcloud auth application-default login"
echo ""
echo "3. Try your first command:"
echo "   gcp-cli execute \"list all cloud storage buckets\""
echo ""
echo "4. Or start interactive mode:"
echo "   gcp-cli interactive"
echo ""
echo "5. View configuration:"
echo "   gcp-cli info"
echo ""
echo "For more information, see README.md"
echo ""
