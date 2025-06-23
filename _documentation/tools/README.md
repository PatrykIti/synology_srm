# Documentation Validation Tools

This directory contains tools for maintaining documentation quality and consistency.

## Tools Overview

### 1. validate_docs.py
Main validation tool that checks:
- **Link Validity**: Internal and external markdown links
- **Template Compliance**: Required sections and structure
- **Formatting**: Consistent formatting rules

**Usage:**
```bash
# Basic validation
python validate_docs.py

# Skip link checking (faster)
python validate_docs.py --no-links

# Include external URL checking (slower)
python validate_docs.py --check-external

# Output as JSON for CI/CD
python validate_docs.py --json

# Validate specific directory
python validate_docs.py --dir /path/to/docs
```

### 2. fix_whitespace.py
Removes trailing whitespace from documentation files.

**Usage:**
```bash
python fix_whitespace.py
```

### 3. fix_broken_links.py
Fixes known broken cross-reference links in documentation.

**Usage:**
```bash
python fix_broken_links.py
```

## CI/CD Integration

The validation tools are integrated with GitHub Actions:

1. **Automatic Validation**: Runs on every PR and push
2. **PR Comments**: Validation results posted as PR comments
3. **Build Failure**: Fails CI build if errors are found
4. **Artifacts**: JSON results uploaded for analysis

See `.github/workflows/validate-docs.yml` for configuration.

## Configuration Files

### validation-config.yaml
Central configuration for validation rules:
- Required/optional sections
- Formatting rules
- Severity levels
- CI/CD behavior

### .github/markdown-link-check.json
Configuration for markdown-link-check tool:
- URL patterns to ignore
- HTTP headers for specific sites
- Retry settings
- Timeout configuration

### .github/cspell.json
Spell checker configuration:
- Custom dictionary for technical terms
- Paths to ignore
- Pattern exclusions

## Running Locally

1. **Install Dependencies:**
```bash
pip install requests pyyaml
npm install -g markdown-link-check
npm install -g cspell
```

2. **Run Full Validation:**
```bash
# Python validation
python _documentation/tools/validate_docs.py

# Link checking
markdown-link-check _documentation/**/*.md

# Spell checking
cspell _documentation/**/*.md
```

3. **Fix Common Issues:**
```bash
# Fix trailing whitespace
python _documentation/tools/fix_whitespace.py

# Fix broken links
python _documentation/tools/fix_broken_links.py
```

## Pre-commit Hook

Add this to `.git/hooks/pre-commit`:
```bash
#!/bin/bash
python _documentation/tools/validate_docs.py
if [ $? -ne 0 ]; then
    echo "Documentation validation failed. Please fix errors before committing."
    exit 1
fi
```

## Validation Rules

### Required Elements
- All sections from TEMPLATE.md
- Breadcrumb navigation
- Cross-references section
- H1 title at document start

### Formatting Rules
- No tabs (use spaces)
- No trailing whitespace
- Consistent indentation
- Proper markdown syntax

### Link Rules
- Internal links must point to existing files
- External links should be reachable (optional check)
- Anchors must exist in target documents

## Troubleshooting

### Common Errors

1. **Missing Required Section**
   - Add the missing section to your document
   - Copy structure from TEMPLATE.md

2. **Broken Internal Link**
   - Check if target file exists
   - Verify correct relative path
   - Run fix_broken_links.py

3. **Trailing Whitespace**
   - Run fix_whitespace.py
   - Configure editor to remove on save

4. **Template Non-compliance**
   - Compare with TEMPLATE.md
   - Ensure all required sections present
   - Check breadcrumb navigation

## Contributing

When adding new validation rules:
1. Update validation-config.yaml
2. Modify validate_docs.py
3. Update this README
4. Test thoroughly
5. Update CI/CD workflow if needed