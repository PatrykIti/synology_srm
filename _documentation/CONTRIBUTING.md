# Contributing to SRM Documentation

Thank you for your interest in contributing to the Synology SRM system documentation project! This guide will help you understand our standards and processes.

## Table of Contents
- [Documentation Standards](#documentation-standards)
- [File Organization](#file-organization)
- [Template Usage](#template-usage)
- [Linking Conventions](#linking-conventions)
- [Workflow Process](#workflow-process)
- [Quality Checklist](#quality-checklist)
- [Tools and Validation](#tools-and-validation)

## Documentation Standards

### General Principles
1. **Accuracy**: All information must be technically accurate and verified
2. **Consistency**: Follow the established template and formatting
3. **Completeness**: Cover all aspects defined in the template
4. **Clarity**: Write for technical audience but remain clear
5. **Objectivity**: Focus on technical facts, not opinions

### Writing Style
- Use present tense for current state descriptions
- Use imperative mood for instructions
- Be concise but thorough
- Avoid marketing language or subjective assessments
- Include specific version numbers and technical details

## File Organization

### Directory Structure
```
_documentation/
├── structure/          # System directory documentation
│   ├── bin.md         # One file per directory
│   ├── etc.md
│   └── ...
├── packages/          # Software package documentation
│   ├── index.md       # Package documentation index
│   ├── safe-access/   # Individual package directories
│   │   └── README.md
│   └── ...
├── guides/            # Comprehensive guides
├── tools/             # Documentation tools
├── _templates/        # Documentation templates
│   └── package_analysis_template.md
├── TEMPLATE.md        # Master template
├── CONTRIBUTING.md    # This file
└── README.md          # Project overview
```

### File Naming
- Use lowercase with no spaces
- Match the directory name exactly (e.g., `/usr.syno/` → `usr.syno.md`)
- Use hyphens for multi-word filenames
- Always use `.md` extension

## Template Usage

All structure documentation must follow `TEMPLATE.md`:

### Required Sections
1. **Title and Navigation**
   ```markdown
   # /directory_name Directory - Brief Description
   
   [← Back to Documentation Index](../README.md) | [← Previous: /prev](prev.md) | [→ Next: /next](next.md)
   
   ---
   ```

2. **Overview** - Purpose and role in the system
3. **Directory Structure** - Tree view with annotations
4. **Key Components** - Major subdirectories/files
5. **Configuration Files** - Config file details
6. **Scripts and Executables** - Script analysis
7. **Integration Points** - System interactions
8. **Security Considerations** - Security implications
9. **Network Services** - Network-related features
10. **Performance Considerations** - Resource usage/impact
11. **Maintenance Notes** - Operational guidance
12. **Cross-References** - Links to related docs

### Optional Sections
- **Platform-Specific Features**
- **Troubleshooting**
- **Version Information**

## Linking Conventions

### Internal Links
```markdown
# Within same directory
[link text](filename.md)
[link text](filename.md#section-anchor)

# To parent directory
[link text](../README.md)

# Cross-references to structure docs
[/bin/](bin.md)
[/usr/syno/](usr.syno.md)
```

### Anchor Format
- Convert section names to lowercase
- Replace spaces with hyphens
- Remove special characters
- Example: `## Key Components` → `#key-components`

### External Links
- Use full URLs including protocol
- Prefer HTTPS where available
- Avoid linking to potentially unstable resources

## Workflow Process

### 1. Before Starting
- Read existing documentation for consistency
- Check if file already exists
- Review TEMPLATE.md thoroughly
- Understand the directory's purpose

### 2. Analysis Phase
- Use Task Master for task tracking
- Leverage Zen MCP tools for analysis:
  ```bash
  # Use Gemini for comprehensive analysis
  mcp zen analyze --model gemini-2.5-pro
  ```
- Document findings systematically
- Cross-reference with related directories

### 3. Documentation Phase
- Start with TEMPLATE.md structure
- Fill in all required sections
- Add code examples and command outputs
- Include tree views for directory structure
- Document security implications

### 4. Review Phase
- Run validation tools
- Check all links work
- Verify technical accuracy
- Ensure template compliance
- Review with `zen consensus` if needed

### 5. Submission
- Run all validation checks
- Fix any identified issues
- Commit with descriptive message
- Create pull request if applicable

## Quality Checklist

Before submitting documentation:

### Content
- [ ] All required sections present
- [ ] Technical accuracy verified
- [ ] Security implications documented
- [ ] Performance impact assessed
- [ ] Cross-references included

### Formatting
- [ ] Follows TEMPLATE.md structure
- [ ] Proper markdown syntax
- [ ] Code blocks with language tags
- [ ] Consistent heading hierarchy
- [ ] No trailing whitespace

### Links
- [ ] All internal links valid
- [ ] Breadcrumb navigation present
- [ ] Cross-references work
- [ ] No broken links

### Validation
- [ ] Passes `validate_docs.py`
- [ ] No spell check errors
- [ ] Markdown linting clean

## Tools and Validation

### Required Tools
```bash
# Python validation
python _documentation/tools/validate_docs.py

# Fix whitespace
python _documentation/tools/fix_whitespace.py

# Fix broken links
python _documentation/tools/fix_broken_links.py
```

### Optional Tools
```bash
# Markdown link checker
npm install -g markdown-link-check
markdown-link-check _documentation/**/*.md

# Spell checker
npm install -g cspell
cspell _documentation/**/*.md
```

### Pre-commit Hook
Add to `.git/hooks/pre-commit`:
```bash
#!/bin/bash
python _documentation/tools/validate_docs.py
```

## Common Issues and Solutions

### Missing Sections
- Copy structure from TEMPLATE.md
- Ensure all required sections present
- Don't skip sections - mark as "Not applicable" if needed

### Broken Links
- Run `fix_broken_links.py`
- Verify target files exist
- Use relative paths correctly
- Check anchor formatting

### Template Non-compliance
- Compare with TEMPLATE.md
- Check breadcrumb navigation
- Verify section ordering
- Ensure consistent formatting

### Technical Accuracy
- Cross-reference with live system
- Verify version numbers
- Test commands shown
- Validate configuration examples

## Adding Software Package Documentation

### Purpose
Package documentation provides detailed technical analysis of software packages installed on the SRM system, including their structure, technologies, security implications, and integration points.

### Process
1. **Create Package Directory**
   ```bash
   mkdir -p _documentation/packages/[package-name]/
   ```

2. **Use Package Analysis Template**
   - Copy from `_documentation/_templates/package_analysis_template.md`
   - Fill in all sections following the template guidance
   - Use Zen MCP tools for thorough analysis

3. **Analyze Package with Zen Tools**
   ```bash
   # Example commands for package analysis
   mcp zen analyze --model gemini-2.5-pro --path /var/packages/PackageName
   mcp zen secaudit --model gemini-2.5-pro --focus package
   ```

4. **Update Package Index**
   - Add entry to `_documentation/packages/index.md`
   - Include package name, description, status, and version
   - Maintain alphabetical order within categories

5. **Cross-Reference**
   - Link from related system documentation
   - Update security analysis if relevant
   - Add to network services if applicable

### Package Documentation Requirements
- Complete all sections in the template
- Include digital signature verification results
- Document all network ports and services
- Identify security implications and CVEs
- Map integration with system components

## Getting Help

- Review existing documentation for examples
- Use Task Master for task organization
- Leverage Zen MCP tools for analysis
- Check validation tool output
- Refer to this guide

## License and Attribution

All contributions to this documentation project should maintain technical accuracy and objectivity. Focus on documenting the system as it exists, not as it should be.

---

Thank you for contributing to the Synology SRM documentation project!