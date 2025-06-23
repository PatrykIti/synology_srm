#!/usr/bin/env python3
"""
Fix trailing whitespace in documentation files.
"""

import os
from pathlib import Path

DOCS_ROOT = Path(__file__).parent.parent
STRUCTURE_DIR = DOCS_ROOT / "structure"

def fix_trailing_whitespace(directory):
    """Remove trailing whitespace from all .md files."""
    fixed_count = 0
    
    for md_file in directory.glob('*.md'):
        with open(md_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        modified = False
        new_lines = []
        
        for line in lines:
            new_line = line.rstrip() + '\n' if line.strip() else line.rstrip() + '\n'
            if new_line != line:
                modified = True
                fixed_count += 1
            new_lines.append(new_line)
        
        # Remove trailing newline if exists
        if new_lines and new_lines[-1] == '\n':
            new_lines[-1] = new_lines[-1].rstrip()
        
        if modified:
            with open(md_file, 'w', encoding='utf-8') as f:
                f.writelines(new_lines)
            print(f"Fixed trailing whitespace in {md_file.name}")
    
    return fixed_count

if __name__ == "__main__":
    print("Fixing trailing whitespace in documentation files...")
    count = fix_trailing_whitespace(STRUCTURE_DIR)
    print(f"Fixed {count} lines with trailing whitespace")