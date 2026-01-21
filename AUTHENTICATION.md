# GCP CLI - Authentication Setup Guide

## Recommended: Application Default Credentials (ADC)

For **security and ease of use**, this library uses Google Cloud Application Default Credentials (ADC).

### ✅ Quick Setup

Run this command once:

```bash
gcloud auth application-default login
```

This will:
- Open your browser to authenticate
- Store credentials securely in `~/.config/gcloud/`
- Work automatically with the library (no config needed!)

### Verify Setup

```bash
gcloud auth application-default print-access-token
```

If you see a token, you're all set! ✅

---

## Using the Library After Authentication

Once you've run `gcloud auth application-default login`, the library **just works**:

```python
from gcp_cli import GCPCommandExecutor

# No credentials needed - uses ADC automatically!
executor = GCPCommandExecutor()

result = executor.execute_natural_query(
    query="list all cloud storage buckets",
    dry_run=True
)

print(result['code'])
```

---

## For CI/CD or Production

### Option 1: Service Account Key (Not Recommended for Local Dev)

If you need to use a service account key file:

```python
from gcp_cli import GCPCommandExecutor, CredentialManager

credentials = CredentialManager(
    credentials_path='/path/to/service-account.json'
)

executor = GCPCommandExecutor(credentials=credentials)
```

### Option 2: Workload Identity (Recommended for GKE/Cloud Run)

The library automatically uses workload identity when running on GCP services like:
- Google Kubernetes Engine (GKE)
- Cloud Run
- Cloud Functions
- Compute Engine

No configuration needed!

---

## Environment Variables

Set these if needed:

```bash
# Optional: Set project ID
export GOOGLE_CLOUD_PROJECT=your-project-id

# Optional: Use service account key (not recommended)
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/key.json
```

---

## Security Best Practices

✅ **DO:**
- Use `gcloud auth application-default login` for local development
- Use Workload Identity for GCP services
- Add `*.json` to `.gitignore` to never commit credentials

❌ **DON'T:**
- Commit service account keys to git
- Hardcode credentials in code
- Share credential files

---

## Troubleshooting

### "Could not automatically determine credentials"

Run:
```bash
gcloud auth application-default login
```

### "The Application Default Credentials are not available"

Make sure gcloud is installed:
```bash
# Install gcloud SDK
curl https://sdk.cloud.google.com | bash

# Or on macOS
brew install --cask google-cloud-sdk

# Then authenticate
gcloud auth application-default login
```

### Multiple Projects

Set the active project:
```bash
gcloud config set project YOUR_PROJECT_ID
```

Or in your config file:
```yaml
project_id: your-project-id
location: us-central1
```

---

## Summary

**Simple Setup:**
```bash
# 1. Install gcloud SDK (one-time)
brew install --cask google-cloud-sdk  # macOS

# 2. Authenticate (one-time)
gcloud auth application-default login

# 3. Use the library (no credentials in code!)
python3 your_script.py
```

That's it! The library handles everything else automatically. 🚀
