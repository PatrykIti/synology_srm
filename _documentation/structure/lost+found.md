# /lost+found Directory - Filesystem Recovery Area

[← Back to Documentation Index](../README.md) | [← Previous: /libexec](libexec.md) | [→ Next: /mnt](mnt.md)

---

## Overview
The `/lost+found` directory is a standard component of ext2/ext3/ext4 filesystems used by Synology SRM. It serves as a recovery area where the filesystem check utility (`fsck`) places recovered file fragments and orphaned inodes after filesystem repairs. An empty lost+found directory indicates a healthy filesystem with no corruption issues.

## Directory Structure
```
/lost+found/
└── [empty]
```

## Key Components

### Recovery Mechanism
- **Purpose**: Storage for recovered filesystem fragments
- **Created by**: `mklost+found` during filesystem creation
- **Used by**: `fsck` during filesystem repair operations
- **Content**: Numbered files (#inode) when recovery occurs
- **Normal state**: Empty (indicates healthy filesystem)

### Filesystem Integration
- Pre-allocated blocks for emergency recovery
- Direct inode allocation for performance
- Protected permissions prevent accidental use
- Standard feature of ext-family filesystems

## Configuration Files
No configuration files - this is a filesystem-level feature managed by the kernel and fsck utilities.

## Scripts and Executables
No scripts - managed entirely by filesystem utilities:
- `fsck` - Performs filesystem checks and recovery
- `e2fsck` - ext-specific filesystem checker
- `mklost+found` - Creates the directory with pre-allocated blocks

## Integration Points

### Filesystem Check Process
1. System detects unclean shutdown or errors
2. `fsck` runs during boot sequence
3. Orphaned inodes/blocks discovered
4. Fragments saved to `/lost+found`
5. Admin reviews and recovers data

### Boot Process Integration
- Checked during `/etc/rc` startup sequence
- Part of filesystem mount verification
- Can delay boot if recovery needed
- Logs to `/var/log/messages`

## Security Considerations

### Access Control
- **Permissions**: 700 (drwx------) - root only
- **Purpose**: Prevent users from accessing fragments
- **Risk**: May contain sensitive data fragments
- **Protection**: Only root can examine contents

### Data Recovery Risks
- Recovered fragments may be partial
- No guarantee of data integrity
- May contain mixed file contents
- Sensitive data exposure possible

## Network Services
Not applicable - filesystem-level feature with no network exposure.

## Performance Considerations

### Resource Usage
- **Disk Space**: Pre-allocated blocks (~12KB minimum)
- **Memory**: No runtime memory usage
- **CPU**: Only during fsck operations
- **I/O**: Heavy I/O during filesystem recovery

### Performance Impact
- **Normal Operation**: Zero performance impact
- **Recovery Mode**: Significant I/O during fsck
- **Boot Time**: Can add minutes/hours if recovery needed
- **Disk Performance**: Recovery can be very slow on large disks

### Optimization Notes
- Empty directory = healthy filesystem
- Regular clean shutdowns prevent issues
- Periodic fsck runs catch problems early
- Consider fsck scheduling during maintenance

## Maintenance Notes

### Monitoring
- Check if directory remains empty
- Non-empty indicates past filesystem issues
- Review recovered files for importance
- Monitor system logs for fsck activity

### Best Practices
- Keep directory empty under normal operation
- Investigate any recovered files promptly
- Back up important recovered data
- Clean out after successful recovery

### Recovery Process
```bash
# If files appear in lost+found:
ls -la /lost+found/
file /lost+found/#*
# Attempt to identify file types
# Move important files to proper locations
# Delete unneeded fragments
```

## Cross-References
- Filesystem mounting: [/etc/fstab](etc.md#fstab)
- Boot process: [/etc/rc](etc.md#boot-scripts)
- System logs: [/var/log/messages](var.md#system-logs)
- Filesystem tools: [/sbin/fsck](sbin.md#filesystem-tools)

## Version Information
- **Document Version**: 2.0
- **Last Updated**: 2025-06-23
- **System**: Synology RT6600ax
- **Firmware**: SRM 5.2-9346
- **Analysis**: Filesystem recovery area documentation

---

[← Back to Documentation Index](../README.md) | [← Previous: /libexec](libexec.md) | [→ Next: /mnt](mnt.md)

---
*This documentation was created as part of the comprehensive Synology SRM system analysis project.*
