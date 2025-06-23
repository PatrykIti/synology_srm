#!/usr/bin/env python3
import os
import re

# Navigation order mapping
nav_order = {
    "bin.md": {"prev": None, "next": "data.md"},
    "data.md": {"prev": "bin.md", "next": "etc.md"},
    "etc.md": {"prev": "data.md", "next": "etc.defaults.md"},
    "etc.defaults.md": {"prev": "etc.md", "next": "ini.md"},
    "ini.md": {"prev": "etc.defaults.md", "next": "initrd.md"},
    "initrd.md": {"prev": "ini.md", "next": "lib.md"},
    "lib.md": {"prev": "initrd.md", "next": "lib64.md"},
    "lib64.md": {"prev": "lib.md", "next": "libexec.md"},
    "libexec.md": {"prev": "lib64.md", "next": "lost+found.md"},
    "lost+found.md": {"prev": "libexec.md", "next": "mnt.md"},
    "mnt.md": {"prev": "lost+found.md", "next": "root.md"},
    "root.md": {"prev": "mnt.md", "next": "run.md"},
    "run.md": {"prev": "root.md", "next": "sbin.md"},
    "sbin.md": {"prev": "run.md", "next": "usr.md"},
    "usr.md": {"prev": "sbin.md", "next": "var.md"},
    "var.md": {"prev": "usr.md", "next": "var.defaults.md"},
    "var.defaults.md": {"prev": "var.md", "next": "volume1.md"},
    "volume1.md": {"prev": "var.defaults.md", "next": None}
}

# Performance section templates based on directory type
perf_templates = {
    "initrd.md": """## Performance Considerations

### Resource Usage
- **Disk Space**: Zero (empty mount point)
- **Memory**: ~5.5MB during boot (freed after)
- **CPU**: Minimal during early boot phase
- **I/O**: RAM-based operations only

### Performance Impact
- **Boot Time**: Critical path - affects total boot duration
- **Module Loading**: Early driver initialization overhead
- **Memory Footprint**: Temporary 5.5MB allocation
- **Hardware Detection**: USB enumeration time

### Optimization Notes
- Initramfs size directly impacts boot speed
- Smaller initramfs = faster decompression
- Module selection affects boot time
- Early boot cannot be optimized by users""",

    "lib64.md": """## Performance Considerations

### Resource Usage
- **Disk Space**: ~100MB for 64-bit libraries
- **Memory**: Libraries loaded on-demand
- **CPU**: No direct CPU usage
- **I/O**: Initial library loading only

### Performance Impact
- **Application Startup**: 64-bit library loading time
- **Memory Usage**: Shared libraries reduce total memory
- **Cache Efficiency**: Better performance with 64-bit code
- **Binary Compatibility**: Native 64-bit execution

### Optimization Notes
- Prelinked libraries improve load times
- Shared libraries reduce memory footprint
- Library cache maintained by ldconfig
- Symbol resolution overhead minimal""",

    "libexec.md": """## Performance Considerations

### Resource Usage
- **Disk Space**: Varies by installed helpers
- **Memory**: Helper programs loaded on-demand
- **CPU**: Only when helpers are invoked
- **I/O**: Minimal - program loading only

### Performance Impact
- **Service Startup**: Helper execution adds overhead
- **System Calls**: Additional process creation cost
- **Security Checks**: Authentication helper latency
- **Resource Limits**: Per-helper resource consumption

### Optimization Notes
- Helpers should be lightweight and fast
- Avoid unnecessary helper invocations
- Cache helper results when possible
- Monitor helper execution times""",

    "lost+found.md": """## Performance Considerations

### Resource Usage
- **Disk Space**: Zero under normal operation
- **Memory**: No memory usage
- **CPU**: Only during fsck operations
- **I/O**: Heavy I/O during filesystem recovery

### Performance Impact
- **Normal Operation**: Zero performance impact
- **Recovery Mode**: Significant I/O during fsck
- **Boot Time**: Delays if fsck recovery needed
- **Disk Performance**: Recovery can take hours

### Optimization Notes
- Empty directory = healthy filesystem
- Regular fsck prevents accumulation
- Clean shutdowns avoid recovery needs
- Monitor for unexpected entries""",

    "mnt.md": """## Performance Considerations

### Resource Usage
- **Disk Space**: Zero (empty mount point)
- **Memory**: No memory usage
- **CPU**: No CPU usage
- **I/O**: No I/O activity

### Performance Impact
- **Mount Operations**: Manual mounts only
- **External Storage**: Not used by auto-mount
- **System Performance**: Zero impact
- **Resource Usage**: Completely passive

### Optimization Notes
- Directory exists for compatibility only
- Auto-mounts use /volumeUSB{N} instead
- No optimization needed or possible
- Consider removing if never used""",

    "root.md": """## Performance Considerations

### Resource Usage
- **Disk Space**: Minimal (~1MB)
- **Memory**: No runtime memory usage
- **CPU**: No CPU usage
- **I/O**: Minimal - only during updates

### Performance Impact
- **System Updates**: GPG verification overhead
- **HTTPS Connections**: HSTS cache improves speed
- **Shell Startup**: .profile parsing negligible
- **Security Operations**: GPG operations when needed

### Optimization Notes
- GPG keyring kept minimal
- HSTS cache reduces SSL handshakes
- Profile kept simple for fast login
- No user customization overhead""",

    "run.md": """## Performance Considerations

### Resource Usage
- **Disk Space**: Zero (tmpfs mount)
- **Memory**: Variable based on runtime state
- **CPU**: No direct CPU usage
- **I/O**: RAM-based, very fast

### Performance Impact
- **PID Files**: Fast process lookups
- **Lock Files**: Efficient resource locking
- **Socket Files**: High-performance IPC
- **State Files**: Quick status checks

### Optimization Notes
- tmpfs provides fastest possible I/O
- No disk writes improves performance
- Cleared on reboot prevents cruft
- Size limits prevent memory exhaustion""",

    "usr.md": """## Performance Considerations

### Resource Usage
- **Disk Space**: Largest directory (~500MB+)
- **Memory**: Binaries/libraries loaded on-demand
- **CPU**: No direct CPU usage
- **I/O**: Read-heavy during program execution

### Performance Impact
- **Binary Loading**: Affects all program starts
- **Library Sharing**: Reduces memory usage
- **Path Lookups**: Can impact command execution
- **Cache Efficiency**: Frequently used files cached

### Optimization Notes
- Organized structure aids caching
- Shared libraries reduce duplication
- Preloading can improve performance
- Consider SSD for faster access""",

    "var.defaults.md": """## Performance Considerations

### Resource Usage
- **Disk Space**: ~50MB for default logs/data
- **Memory**: No runtime memory usage
- **CPU**: No CPU usage
- **I/O**: Read-only reference data

### Performance Impact
- **Factory Reset**: Fast restoration source
- **Template Access**: Quick configuration reset
- **Update Operations**: Efficient defaults update
- **Recovery Time**: Reduces downtime

### Optimization Notes
- Read-only prevents fragmentation
- Organized structure for fast access
- Minimal size reduces update time
- No runtime overhead""",

    "var.md": """## Performance Considerations

### Resource Usage
- **Disk Space**: Grows over time (logs, databases)
- **Memory**: Database caches, log buffers
- **CPU**: Log rotation, database operations
- **I/O**: Heavy write activity

### Performance Impact
- **Logging**: Can impact system under load
- **Databases**: Query performance critical
- **Temp Files**: Can cause I/O contention
- **Cache Files**: Improve application speed

### Optimization Notes
- Regular log rotation essential
- Database maintenance improves speed
- Monitor disk space usage
- Consider separate partition for /var""",

    "volume1.md": """## Performance Considerations

### Resource Usage
- **Disk Space**: Primary storage consumption
- **Memory**: Application and database caches
- **CPU**: Package-specific processing
- **I/O**: Highest I/O activity location

### Performance Impact
- **Database Growth**: Unbounded growth affects speed
- **SQLite Performance**: Degrades with size
- **Search Indexes**: Xapian can be resource-intensive
- **Concurrent Access**: Lock contention issues

### Optimization Notes
- Regular database maintenance critical
- Monitor Traffic/SafeAccess DB growth
- Consider database size limits
- Implement data retention policies"""
}

def get_breadcrumb(filename, position="top"):
    """Generate breadcrumb navigation for a file"""
    nav = nav_order.get(filename, {})
    prev_file = nav.get("prev")
    next_file = nav.get("next")
    
    parts = ["[← Back to Documentation Index](../README.md)"]
    
    if prev_file:
        prev_name = prev_file.replace(".md", "").replace(".", " ")
        parts.append(f"[← Previous: /{prev_name}]({prev_file})")
    
    if next_file:
        next_name = next_file.replace(".md", "").replace(".", " ")
        parts.append(f"[→ Next: /{next_name}]({next_file})")
    
    return " | ".join(parts)

def fix_file(filepath, filename):
    """Fix a single documentation file"""
    print(f"\nProcessing {filename}...")
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"  Error reading file: {e}")
        return False
    
    # Check if already has top breadcrumb
    has_top_breadcrumb = content.startswith("[← Back to Documentation Index]")
    
    # Add top breadcrumb if missing
    if not has_top_breadcrumb:
        lines = content.split('\n')
        if lines[0].startswith('#'):
            # Insert breadcrumb after title
            breadcrumb = get_breadcrumb(filename, "top")
            lines.insert(1, '')
            lines.insert(2, breadcrumb)
            lines.insert(3, '')
            lines.insert(4, '---')
            content = '\n'.join(lines)
            print(f"  Added top breadcrumb")
    
    # Check if has Performance Considerations
    if "## Performance Considerations" not in content:
        # Get template or use default
        perf_content = perf_templates.get(filename, """## Performance Considerations

### Resource Usage
- **Disk Space**: [Specify typical disk usage]
- **Memory**: [Specify memory requirements]
- **CPU**: [Specify CPU usage patterns]
- **I/O**: [Specify I/O characteristics]

### Performance Impact
- **System Performance**: [Describe impact on system]
- **Service Performance**: [Describe service-specific impacts]
- **Scalability**: [Describe scalability characteristics]
- **Bottlenecks**: [Identify potential bottlenecks]

### Optimization Notes
- [List optimization strategies]
- [Performance tuning options]
- [Monitoring recommendations]
- [Best practices]""")
        
        # Find where to insert (before Maintenance Notes)
        if "## Maintenance Notes" in content:
            content = content.replace("## Maintenance Notes", f"{perf_content}\n\n## Maintenance Notes")
            print(f"  Added Performance Considerations section")
        else:
            # Insert before Cross-References or at end
            if "## Cross-References" in content:
                content = content.replace("## Cross-References", f"{perf_content}\n\n## Cross-References")
            else:
                # Add at end before footer
                lines = content.split('\n')
                # Find footer line
                footer_idx = -1
                for i in range(len(lines)-1, -1, -1):
                    if lines[i].startswith('*This documentation was created'):
                        footer_idx = i
                        break
                
                if footer_idx > 0:
                    lines.insert(footer_idx-1, perf_content)
                    lines.insert(footer_idx, '')
                content = '\n'.join(lines)
            print(f"  Added Performance Considerations section")
    
    # Check and add bottom breadcrumb
    breadcrumb_bottom = get_breadcrumb(filename, "bottom")
    
    # Remove any existing bottom breadcrumb to avoid duplicates
    lines = content.split('\n')
    
    # Find and remove existing bottom breadcrumb if present
    for i in range(len(lines)-1, -1, -1):
        if lines[i].startswith("[← Back to Documentation Index]"):
            # Remove this line and surrounding empty lines
            lines.pop(i)
            if i < len(lines) and lines[i] == '':
                lines.pop(i)
            if i > 0 and lines[i-1] == '':
                lines.pop(i-1)
            break
    
    # Now add the bottom breadcrumb properly
    # Find where to insert (before footer line or at end)
    footer_idx = -1
    for i in range(len(lines)-1, -1, -1):
        if lines[i].startswith('*') and 'documentation' in lines[i].lower():
            footer_idx = i
            break
    
    if footer_idx > 0:
        # Insert breadcrumb before footer
        insert_idx = footer_idx
        # Check if there's a --- separator before footer
        if footer_idx > 1 and lines[footer_idx-2] == '---':
            insert_idx = footer_idx - 2
        elif footer_idx > 0 and lines[footer_idx-1] == '---':
            insert_idx = footer_idx - 1
        
        # Insert breadcrumb with proper spacing
        if insert_idx > 0 and lines[insert_idx-1] != '':
            lines.insert(insert_idx, '')
            insert_idx += 1
        lines.insert(insert_idx, '---')
        lines.insert(insert_idx+1, '')
        lines.insert(insert_idx+2, breadcrumb_bottom)
        if footer_idx > 0:
            lines.insert(insert_idx+3, '')
    else:
        # No footer found, add at end
        if lines and lines[-1] != '':
            lines.append('')
        lines.append('---')
        lines.append('')
        lines.append(breadcrumb_bottom)
    
    content = '\n'.join(lines)
    print(f"  Added bottom breadcrumb")
    
    # Write back
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ Successfully updated {filename}")
        return True
    except Exception as e:
        print(f"  Error writing file: {e}")
        return False

# Files that need fixing
files_to_fix = [
    "initrd.md", "lib64.md", "libexec.md", "lost+found.md",
    "mnt.md", "root.md", "run.md", "usr.md", 
    "var.defaults.md", "var.md", "volume1.md"
]

# Process each file
base_dir = "/Users/pciechanski/Documents/_moje_projekty/synology_srm/_documentation/structure"
success_count = 0

for filename in files_to_fix:
    filepath = os.path.join(base_dir, filename)
    if os.path.exists(filepath):
        if fix_file(filepath, filename):
            success_count += 1
    else:
        print(f"\n✗ File not found: {filename}")

print(f"\n\nSummary: Successfully updated {success_count}/{len(files_to_fix)} files")