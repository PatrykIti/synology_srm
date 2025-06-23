#!/usr/bin/env python3
"""
Fix broken cross-reference links in SRM documentation.
This script updates broken links to point to existing usr.md file
or removes them if no suitable target exists.
"""

import os
import re

# Mapping of broken links to their fixes
LINK_FIXES = {
    # Links to usr.syno.md -> point to usr.md with note about Synology tools
    'usr.syno.md': 'usr.md',
    'usr.syno.md#security-tools': 'usr.md#synology-specific-tools',
    'usr.syno.md#update-system': 'usr.md#synology-specific-tools',
    
    # Links to usr.sbin.md -> point to usr.md#system-binaries
    'usr.sbin.md': 'usr.md#system-binaries',
    
    # Links to usr.bin.md -> point to usr.md#user-binaries
    'usr.bin.md': 'usr.md#user-binaries',
    
    # Links to sys.md -> remove or comment out (not documented yet)
    'sys.md': None,
    'sys.md#usb-subsystem': None,
    
    # Links to dev.md -> remove or comment out (not documented yet)
    'dev.md': None,
    
    # Links to init.md -> point to etc.md#upstart-services
    'init.md': 'etc.md#upstart-services',
    
    # Fix relative path issues
    '../sbin.md': 'sbin.md',
    '../lib.md': 'lib.md',
    '../etc.defaults.md': 'etc.defaults.md',
}

def fix_broken_links(directory):
    """Fix broken links in all markdown files in the given directory."""
    fixed_count = 0
    
    for filename in os.listdir(directory):
        if not filename.endswith('.md'):
            continue
            
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Find all markdown links
        link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
        
        def replace_link(match):
            nonlocal fixed_count
            text = match.group(1)
            link = match.group(2)
            
            # Check if this link needs fixing
            for broken_link, fix in LINK_FIXES.items():
                if link == broken_link or link.endswith('/' + broken_link):
                    if fix is None:
                        # Comment out the link but keep the text
                        fixed_count += 1
                        print(f"  {filename}: Commenting out [{text}]({link})")
                        return f"{text} <!-- Link to {broken_link} removed until documented -->"
                    else:
                        # Update the link
                        new_link = link.replace(broken_link, fix)
                        fixed_count += 1
                        print(f"  {filename}: [{text}]({link}) -> [{text}]({new_link})")
                        return f"[{text}]({new_link})"
            
            # Link doesn't need fixing
            return match.group(0)
        
        # Replace all links
        content = re.sub(link_pattern, replace_link, content)
        
        # Write back if changed
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
    
    return fixed_count

def main():
    """Main function."""
    print("Fixing broken cross-reference links in SRM documentation...")
    print("=" * 60)
    
    structure_dir = '/Users/pciechanski/Documents/_moje_projekty/synology_srm/_documentation/structure'
    
    if not os.path.exists(structure_dir):
        print(f"Error: Directory not found: {structure_dir}")
        return
    
    # First, we need to ensure usr.md exists with proper sections
    usr_md_path = os.path.join(structure_dir, 'usr.md')
    if not os.path.exists(usr_md_path):
        print("Creating placeholder usr.md file...")
        usr_content = """# /usr Directory - User Programs and Libraries

[← Back to Documentation Index](../README.md) | [← Previous: /lib](lib.md) | [→ Next: /var](var.md)

---

## Overview
The `/usr` directory contains the majority of user utilities and applications. According to the Filesystem Hierarchy Standard (FHS), this directory holds shareable, read-only data including binaries, libraries, documentation, and source code for the second level of the system hierarchy.

## Directory Structure
```
/usr/
├── bin/                    [User binaries]
├── sbin/                   [System binaries]
├── lib/                    [Libraries]
├── lib64 -> lib           [64-bit libraries symlink]
├── local/                  [Locally installed software]
├── share/                  [Architecture-independent data]
└── syno/                   [Synology-specific tools and libraries]
```

## Key Components

### User Binaries
- **Purpose**: Standard user commands and utilities
- **Location**: `/usr/bin/`
- **Dependencies**: Linked against libraries in `/usr/lib/`
- **Configuration**: Some utilities use config files in `/etc/`
- **Security**: Should be executable by all users

### System Binaries
- **Purpose**: System administration commands not required for boot/repair
- **Location**: `/usr/sbin/`
- **Dependencies**: May require root privileges
- **Configuration**: Often configured via `/etc/` files
- **Security**: Typically restricted to administrative users

### Synology-Specific Tools
- **Purpose**: Proprietary Synology utilities and services
- **Location**: `/usr/syno/`
- **Components**: 
  - Management tools
  - System services
  - Configuration utilities
  - Update mechanisms
- **Security**: Critical for system operation

## Note
This documentation is a placeholder. The `/usr` directory requires comprehensive analysis to document all binaries, libraries, and especially Synology-specific tools that are critical for SRM operation.

## Cross-References
- System binaries: [/bin/](bin.md) and [/sbin/](sbin.md)
- Libraries: [/lib/](lib.md)
- Configuration: [/etc/](etc.md)
- Variable data: [/var/](var.md)

---

[← Back to Documentation Index](../README.md) | [← Previous: /lib](lib.md) | [→ Next: /var](var.md)
"""
        with open(usr_md_path, 'w', encoding='utf-8') as f:
            f.write(usr_content)
        print("Created usr.md placeholder file")
    
    print("\nFixing broken links...")
    fixed = fix_broken_links(structure_dir)
    
    print(f"\nTotal links fixed: {fixed}")
    print("=" * 60)
    
    # List files that still need to be documented
    print("\nFiles that need to be created:")
    print("- sys.md (Kernel interface)")
    print("- dev.md (Device files)")
    print("- Full documentation for usr.md (currently placeholder)")

if __name__ == "__main__":
    main()