#!/usr/bin/env python3
"""
Documentation validation tool for Synology SRM documentation.
Checks for:
1. Broken markdown links (internal and external)
2. Template compliance
3. Consistent formatting
"""

import os
import re
import sys
import json
import argparse
import requests
from pathlib import Path
from typing import List, Dict, Tuple, Optional
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

# Configuration
DOCS_ROOT = Path(__file__).parent.parent  # _documentation directory
STRUCTURE_DIR = DOCS_ROOT / "structure"
TEMPLATE_FILE = DOCS_ROOT / "TEMPLATE.md"

# Template requirements
REQUIRED_SECTIONS = [
    "## Overview",
    "## Directory Structure", 
    "## Key Components",
    "## Configuration Files",
    "## Scripts and Executables",
    "## Integration Points",
    "## Security Considerations",
    "## Network Services",
    "## Performance Considerations",
    "## Maintenance Notes",
    "## Cross-References"
]

# Optional but recommended sections
OPTIONAL_SECTIONS = [
    "## Version Information"
]

class ValidationResult:
    """Container for validation results."""
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.info = []
        
    def add_error(self, file: str, message: str, line: int = None):
        self.errors.append({
            'file': file,
            'message': message,
            'line': line,
            'severity': 'error'
        })
        
    def add_warning(self, file: str, message: str, line: int = None):
        self.warnings.append({
            'file': file,
            'message': message,
            'line': line,
            'severity': 'warning'
        })
        
    def add_info(self, file: str, message: str):
        self.info.append({
            'file': file,
            'message': message,
            'severity': 'info'
        })
        
    def has_errors(self) -> bool:
        return len(self.errors) > 0
        
    def to_json(self) -> str:
        return json.dumps({
            'summary': {
                'errors': len(self.errors),
                'warnings': len(self.warnings),
                'info': len(self.info)
            },
            'errors': self.errors,
            'warnings': self.warnings,
            'info': self.info
        }, indent=2)


class MarkdownLinkChecker:
    """Checks markdown links for validity."""
    
    def __init__(self, timeout: int = 5):
        self.timeout = timeout
        self.external_cache = {}
        
    def check_file(self, filepath: Path, result: ValidationResult):
        """Check all links in a markdown file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Find all markdown links
        link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
        
        for line_num, line in enumerate(content.splitlines(), 1):
            for match in re.finditer(link_pattern, line):
                link_text = match.group(1)
                link_url = match.group(2)
                
                if link_url.startswith('#'):
                    # Anchor link - check if anchor exists
                    self._check_anchor(filepath, content, link_url, link_text, line_num, result)
                elif link_url.startswith('http://') or link_url.startswith('https://'):
                    # External link
                    self._check_external_link(filepath, link_url, link_text, line_num, result)
                else:
                    # Internal file link
                    self._check_internal_link(filepath, link_url, link_text, line_num, result)
                    
    def _check_anchor(self, filepath: Path, content: str, anchor: str, text: str, line: int, result: ValidationResult):
        """Check if anchor exists in the document."""
        anchor_name = anchor[1:]  # Remove #
        # Convert heading to anchor format (lowercase, spaces to hyphens)
        heading_pattern = rf'^#+\s+{re.escape(anchor_name.replace("-", " "))}$'
        
        if not re.search(heading_pattern, content, re.MULTILINE | re.IGNORECASE):
            result.add_error(
                str(filepath.name),
                f"Broken anchor link [{text}]({anchor}) - anchor not found",
                line
            )
            
    def _check_internal_link(self, filepath: Path, link: str, text: str, line: int, result: ValidationResult):
        """Check if internal file link is valid."""
        # Remove anchor if present
        file_part = link.split('#')[0]
        
        # Resolve relative path
        if file_part.startswith('../'):
            target = filepath.parent.parent / file_part[3:]
        else:
            target = filepath.parent / file_part
            
        if not target.exists():
            result.add_error(
                str(filepath.name),
                f"Broken internal link [{text}]({link}) - file not found",
                line
            )
            
    def _check_external_link(self, filepath: Path, url: str, text: str, line: int, result: ValidationResult):
        """Check if external URL is reachable."""
        # Skip checking external links in CI to avoid flakiness
        if os.environ.get('CI'):
            return
            
        # Use cache to avoid repeated checks
        if url in self.external_cache:
            if not self.external_cache[url]:
                result.add_warning(
                    str(filepath.name),
                    f"External link may be broken [{text}]({url})",
                    line
                )
            return
            
        try:
            response = requests.head(url, timeout=self.timeout, allow_redirects=True)
            self.external_cache[url] = response.status_code < 400
            
            if response.status_code >= 400:
                result.add_warning(
                    str(filepath.name),
                    f"External link returned {response.status_code} [{text}]({url})",
                    line
                )
        except Exception as e:
            self.external_cache[url] = False
            result.add_warning(
                str(filepath.name),
                f"Could not check external link [{text}]({url}) - {str(e)}",
                line
            )


class TemplateComplianceChecker:
    """Checks if documentation follows the template."""
    
    def __init__(self, template_path: Path):
        self.template_path = template_path
        self.required_sections = REQUIRED_SECTIONS
        self.optional_sections = OPTIONAL_SECTIONS
        
    def check_file(self, filepath: Path, result: ValidationResult):
        """Check if file follows template structure."""
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Check for required sections
        for section in self.required_sections:
            if section not in content:
                result.add_error(
                    str(filepath.name),
                    f"Missing required section: {section}"
                )
                
        # Check for breadcrumb navigation
        if not re.search(r'\[← Back to Documentation Index\]', content):
            result.add_error(
                str(filepath.name),
                "Missing breadcrumb navigation"
            )
            
        # Check heading structure
        lines = content.splitlines()
        if lines and not lines[0].startswith('# '):
            result.add_error(
                str(filepath.name),
                "Document should start with # (H1) heading",
                1
            )
            
        # Check for consistent formatting
        self._check_formatting(filepath, content, result)
        
    def _check_formatting(self, filepath: Path, content: str, result: ValidationResult):
        """Check for consistent formatting."""
        lines = content.splitlines()
        
        # Check for tabs (should use spaces)
        for i, line in enumerate(lines, 1):
            if '\t' in line and not line.strip().startswith('│'):  # Allow tabs in tree diagrams
                result.add_warning(
                    str(filepath.name),
                    "Line contains tabs, use spaces for indentation",
                    i
                )
                
        # Check for trailing whitespace
        for i, line in enumerate(lines, 1):
            if line.endswith(' '):
                result.add_warning(
                    str(filepath.name),
                    "Line has trailing whitespace",
                    i
                )


def validate_documentation(docs_dir: Path, 
                         check_links: bool = True,
                         check_template: bool = True,
                         check_external: bool = False) -> ValidationResult:
    """Run all validation checks on documentation."""
    result = ValidationResult()
    
    # Initialize checkers
    link_checker = MarkdownLinkChecker()
    template_checker = TemplateComplianceChecker(TEMPLATE_FILE)
    
    # Find all markdown files
    md_files = list(docs_dir.glob('*.md'))
    
    print(f"Validating {len(md_files)} documentation files...")
    
    for md_file in md_files:
        # Skip template itself
        if md_file.name == 'TEMPLATE.md':
            continue
            
        result.add_info(str(md_file.name), "Validating file")
        
        if check_links:
            link_checker.check_file(md_file, result)
            
        if check_template:
            template_checker.check_file(md_file, result)
            
    return result


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description='Validate SRM documentation')
    parser.add_argument('--no-links', action='store_true', 
                       help='Skip link checking')
    parser.add_argument('--no-template', action='store_true',
                       help='Skip template compliance checking')
    parser.add_argument('--check-external', action='store_true',
                       help='Check external URLs (slow)')
    parser.add_argument('--json', action='store_true',
                       help='Output results as JSON')
    parser.add_argument('--dir', type=str, default=str(STRUCTURE_DIR),
                       help='Documentation directory to validate')
    
    args = parser.parse_args()
    
    # Run validation
    result = validate_documentation(
        Path(args.dir),
        check_links=not args.no_links,
        check_template=not args.no_template,
        check_external=args.check_external
    )
    
    # Output results
    if args.json:
        print(result.to_json())
    else:
        # Human-readable output
        print("\n" + "="*60)
        print("VALIDATION RESULTS")
        print("="*60)
        
        if result.errors:
            print(f"\n❌ ERRORS ({len(result.errors)}):")
            for error in result.errors:
                line_info = f":{error['line']}" if error['line'] else ""
                print(f"  {error['file']}{line_info}: {error['message']}")
                
        if result.warnings:
            print(f"\n⚠️  WARNINGS ({len(result.warnings)}):")
            for warning in result.warnings:
                line_info = f":{warning['line']}" if warning['line'] else ""
                print(f"  {warning['file']}{line_info}: {warning['message']}")
                
        if not result.errors and not result.warnings:
            print("\n✅ All checks passed!")
        else:
            print(f"\nSummary: {len(result.errors)} errors, {len(result.warnings)} warnings")
            
    # Exit with error code if errors found
    sys.exit(1 if result.has_errors() else 0)


if __name__ == '__main__':
    main()