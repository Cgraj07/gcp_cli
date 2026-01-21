# GCP CLI - Testing Guide

## Quick Test Commands

### 1. ✅ Verify Installation (Already Working!)

```bash
# Show help
./bin/python3 -m gcp_cli.cli --help

# Show current configuration
./bin/python3 -m gcp_cli.cli --config example_config.yaml info
```

**Expected Output:** Configuration details including project ID, location, model, and credentials path.

---

## 2. Test Code Generation (Dry-Run Mode)

This generates code WITHOUT executing it - perfect for testing!

```bash
# Test 1: Simple query
./bin/python3 -m gcp_cli.cli --config example_config.yaml execute --dry-run "list all cloud storage buckets"

# Test 2: Compute Engine query
./bin/python3 -m gcp_cli.cli --config example_config.yaml execute --dry-run "list all compute instances in us-central1"

# Test 3: IAM query
./bin/python3 -m gcp_cli.cli --config example_config.yaml execute --dry-run "list all service accounts"
```

**What to Expect:**
- The AI will generate Python code
- Code will be displayed with syntax highlighting
- No execution (safe to test)
- You can review the generated code quality

---

## 3. Test with Preview Mode (Interactive Confirmation)

This generates code and asks for confirmation before executing:

```bash
# The CLI will:
# 1. Generate code
# 2. Show you the code
# 3. Ask "Execute this command? [y/N]:"
# 4. Wait for your approval (press 'n' to cancel)

./bin/python3 -m gcp_cli.cli --config example_config.yaml execute "list all cloud storage buckets"
```

**Safety Features:**
- You see the code before it runs
- You can cancel by typing 'n'
- Safe for testing real commands

---

## 4. Test Interactive Mode

Start a conversational session:

```bash
./bin/python3 -m gcp_cli.cli interactive
```

**In interactive mode, try these commands:**
```
gcp> list all cloud storage buckets
gcp> history
gcp> exit
```

**Note:** 
- Type your queries naturally
- Type `history` to see command history
- Type `exit` or `quit` to leave

---

## 5. Test Python API

Create a test script (`test_api.py`):

```python
#!/usr/bin/env python3
from gcp_cli import GCPCommandExecutor, ConfigManager

# Load your config
config = ConfigManager(config_path='example_config.yaml')

# Initialize executor
executor = GCPCommandExecutor(config=config)

# Test with dry-run (no execution)
result = executor.execute_natural_query(
    query="list all cloud storage buckets",
    dry_run=True
)

print("Generated Code:")
print(result['code'])
print("\nQuery:", result['query'])
print("Executed:", result['executed'])
```

Run it:
```bash
./bin/python3 test_api.py
```

---

## 6. Test Different GCP Services

### Storage Buckets
```bash
./bin/python3 -m gcp_cli.cli execute --dry-run "list all storage buckets"
./bin/python3 -m gcp_cli.cli execute --dry-run "create a storage bucket named test-bucket-12345"
```

### Compute Engine
```bash
./bin/python3 -m gcp_cli.cli execute --dry-run "list compute instances"
./bin/python3 -m gcp_cli.cli execute --dry-run "list all compute zones"
```

### IAM
```bash
./bin/python3 -m gcp_cli.cli execute --dry-run "list all service accounts"
./bin/python3 -m gcp_cli.cli execute --dry-run "list IAM policy bindings"
```

### Cloud SQL
```bash
./bin/python3 -m gcp_cli.cli execute --dry-run "list all cloud sql instances"
```

---

## 7. Test Real Execution (When Ready)

**⚠️ ONLY run these when you're ready to execute real GCP commands:**

```bash
# With preview (you'll be asked to confirm)
./bin/python3 -m gcp_cli.cli execute "list all cloud storage buckets"

# Auto-execute (no preview)
./bin/python3 -m gcp_cli.cli execute --no-preview "list all storage buckets"
```

---

## Testing Checklist

- [ ] ✅ Help system works (`--help`)
- [ ] ✅ Configuration loads correctly (`info` command)
- [ ] Test dry-run mode (generates code without executing)
- [ ] Test preview mode (shows code and asks for confirmation)
- [ ] Test different GCP services (Storage, Compute, IAM, etc.)
- [ ] Test interactive mode
- [ ] Test Python API
- [ ] Test command history
- [ ] Test real execution (when ready)

---

## Recommended Testing Workflow

### Step 1: Dry-Run Tests (Safe, No Execution)
Start with these to verify AI generation is working:

```bash
# Test 5 different types of queries
./bin/python3 -m gcp_cli.cli execute --dry-run "list all cloud storage buckets"
./bin/python3 -m gcp_cli.cli execute --dry-run "list compute instances"
./bin/python3 -m gcp_cli.cli execute --dry-run "list service accounts"
./bin/python3 -m gcp_cli.cli execute --dry-run "list all cloud sql instances"
./bin/python3 -m gcp_cli.cli execute --dry-run "show project information"
```

### Step 2: Review Generated Code
Check if the AI-generated code:
- Uses correct GCP client libraries
- Has proper authentication setup
- Includes error handling
- Has informative print statements

### Step 3: Preview Mode Tests
When code quality looks good, test with preview mode:

```bash
# You can review and cancel
./bin/python3 -m gcp_cli.cli execute "list all cloud storage buckets"
# Answer 'n' to cancel if you don't want to execute
```

### Step 4: Execute Real Commands
When confident, execute actual commands:

```bash
# Simple read-only command
./bin/python3 -m gcp_cli.cli execute "list all cloud storage buckets"
# Answer 'y' to execute
```

---

## Troubleshooting Tests

### If you get "Failed to validate GCP credentials":
```bash
# Check your credentials file exists
ls -la apt-decorator-422604-i0-46b8ef356f34.json

# Verify it's set in config
cat example_config.yaml
```

### If Vertex AI API errors occur:
```bash
# Ensure Vertex AI is enabled
gcloud services enable aiplatform.googleapis.com --project=apt-decorator-422604-i0
```

### If code generation fails:
- Check your internet connection
- Verify GCP credentials have proper permissions
- Check the Vertex AI API is enabled

---

## Example Test Session

```bash
# 1. Verify setup
./bin/python3 -m gcp_cli.cli --config example_config.yaml info

# 2. Test code generation (dry-run)
./bin/python3 -m gcp_cli.cli execute --dry-run "list all storage buckets"

# 3. Review the generated code (it will show Python code)

# 4. If code looks good, try with preview
./bin/python3 -m gcp_cli.cli execute "list all storage buckets"
# Type 'n' to cancel or 'y' to execute

# 5. Test interactive mode
./bin/python3 -m gcp_cli.cli interactive
# Then type: list all cloud storage buckets
# Then type: exit
```

---

## Success Criteria

✅ **Your CLI is working if:**
1. `info` command shows your configuration
2. `--dry-run` generates valid Python code
3. Generated code uses Google Cloud client libraries
4. Preview mode shows code with syntax highlighting
5. You can cancel execution in preview mode
6. Interactive mode starts and accepts queries

🎉 **Based on the test results above, your CLI is WORKING!**

---

## Next Steps

1. **Start with dry-run tests** to verify code generation
2. **Review generated code quality** for different types of queries
3. **Use preview mode** when you want to execute real commands
4. **Build trust** by testing simple read-only operations first
5. **Use interactive mode** for exploratory work

Happy testing! 🚀
