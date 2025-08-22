# 🛠️ Scripts

This directory contains maintenance and validation scripts for the awesome-learn-ai repository.

## 📋 Available Scripts

### 🔗 Link Validation Script

**File:** `validate_links.py`

Validates all Microsoft Learn URLs in the README.md file and reports broken links.

#### Usage

```bash
# Basic validation (Microsoft Learn URLs only)
python scripts/validate_links.py

# Generate detailed report
python scripts/validate_links.py --output-report broken_links.md

# Check all links (including external ones)
python scripts/validate_links.py --check-all

# Validate a different file
python scripts/validate_links.py --file CONTRIBUTING.md
```

#### Features

- ✅ Validates Microsoft Learn URLs by default
- 🔍 Option to check all links with `--check-all`
- 📄 Generates detailed markdown reports
- ⏱️ Respects rate limits with delays
- 🎯 Shows line numbers for broken links
- 📊 Provides summary statistics

#### Output

The script provides:
1. **Console output** with real-time validation status
2. **Summary statistics** (total, working, broken links)
3. **Optional markdown report** with detailed breakdown

#### Error Codes

- `0`: All links working
- `1`: Broken links found or validation error

## 🔄 Automated Usage

### GitHub Actions

You can integrate link validation into CI/CD:

```yaml
name: Validate Links
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.x'
      - name: Install dependencies
        run: pip install requests
      - name: Validate links
        run: python scripts/validate_links.py
```

### Pre-commit Hook

Add to `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: local
    hooks:
      - id: validate-links
        name: Validate Microsoft Learn Links
        entry: python scripts/validate_links.py
        language: system
        pass_filenames: false
```

## 📝 Contributing

When adding new scripts:

1. **Document** the script's purpose and usage
2. **Add examples** in this README
3. **Follow naming convention**: `snake_case.py`
4. **Include help text** with `--help` option
5. **Handle errors gracefully** with appropriate exit codes

## 🎯 Future Scripts

Planned additions:
- 📊 **Content statistics** (word count, reading time estimates)
- 🔄 **Automated link replacement** using Microsoft Learn API
- 📱 **Mobile compatibility checker** for markdown rendering
- 🌐 **Translation validation** for multilingual content