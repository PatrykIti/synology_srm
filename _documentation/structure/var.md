# /var Directory - Variable Data Storage

[← Back to Documentation Index](../README.md) | [← Previous: /usr](usr.md) | [→ Next: /var defaults](var.defaults.md)

---
---

## Overview
The `/var` directory serves as the primary location for variable data in Synology SRM. It contains system logs, runtime information, package data, and temporary files that change during normal system operation. This directory follows the Filesystem Hierarchy Standard (FHS) with some Synology-specific adaptations. The directory contains approximately 397 files across all subdirectories, with the majority in logging (115 files) and package management (172 files).

## Directory Structure
```
/var/
├── cache/                     [Application cache data]
│   ├── data_update/          [System update cache]
│   └── samba/                [SMB/CIFS service cache]
├── db -> /volume1/@db/var/db [Database files symlink]
├── dynlib/                    [Dynamic libraries and security rules]
│   └── securityscan/         [Security scanning framework]
├── empty/                     [Empty directory for chroot]
├── lib/                       [Variable state information]
│   ├── dpkg/                 [Package management database]
│   ├── net-snmp/             [SNMP daemon state]
│   └── usbmodem/             [USB modem configurations]
├── lock -> ../run/lock        [Lock files symlink]
├── log/                       [System and application logs]
│   ├── auth.log              [Authentication logs]
│   ├── kern.log              [Kernel messages]
│   ├── messages              [General system messages]
│   ├── ngfw.log              [Next-Gen Firewall logs]
│   ├── safeaccess.log        [Content filtering logs]
│   ├── httpd/                [Web server logs]
│   ├── mesh/                 [Mesh networking logs]
│   ├── samba/                [SMB service logs]
│   ├── synolog/              [Synology-specific logs]
│   └── upstart/              [Service startup logs - 66 files]
├── packages/                  [Installed package data]
│   └── SafeAccess/           [Parental control package]
├── run -> ../run              [Runtime data symlink]
├── services/                  [Service-specific data]
├── spool/                     [Spool directories]
│   └── cron/                 [Cron job spools]
└── tmp/                       [Temporary files]
```

## Key Components

### System Logs (/var/log)
- **Purpose**: Centralized logging for all system activities
- **Key Files**:
  - `auth.log` - Authentication events (SSH, sudo, PAM)
  - `kern.log` - Kernel messages and hardware events
  - `messages` - General system messages
  - `ngfw.log` - Next-Gen Firewall with nDPI inspection
  - `safeaccess.log` - Content filtering and threat blocking
  - `wifi.log` - Wireless subsystem and DFS events
  - `dhcp-client.log` - DHCP negotiations and IP assignments
- **Specialized Directories**:
  - `mesh/` - Mesh networking logs (CAP/RE topology, HYD system)
    - Tracks synomeshd daemon operations
    - Monitors node connectivity and upgrade checks
    - Records HYD topology on port 7777
    - Logs WebAPI mesh operations
  - `synolog/` - Synology-specific component logs
  - `httpd/` - Web server access and error logs
  - `samba/` - SMB/CIFS service logs
  - `upstart/` - Service initialization logs (66 files)
- **Management**:
  - syslog-ng v3.5.5 for centralized collection
  - logrotate with XZ compression (90% ratio)
  - Size-based rotation: 1M default, 10M for system logs
  - 4 rotations kept for each log
- **Security**: Contains authentication attempts, security events, and system activities

### Package Management (/var/lib/dpkg)
- **Purpose**: Debian package database for installed software
- **Key Files**:
  - `status` - Current package states and versions
  - `available` - Available packages list
  - `info/` - Package metadata and checksums
- **Dependencies**: Based on Debian 12 "Bookworm"
- **Configuration**: Tracks 172+ system packages
- **Security**: Reveals exact software versions for CVE mapping

### Security Scanning Framework (/var/dynlib/securityscan)
- **Purpose**: Comprehensive security rule engine
- **Components**:
  - Python-based rule framework
  - Categories: DirectoryService, FileService, Malware, Network, Security, Terminal, Update, User
  - Multi-language support (21 languages)
  - Rule database with specific security checks
- **Integration**: WebAPI for security policy enforcement
- **Security**: Exposes security monitoring patterns

### Package Data (/var/packages)
- **Purpose**: Installed package configurations and scripts
- **Current Packages**:
  - SafeAccess v1.3.1-0326 - Parental control and security
- **Structure**:
  - Installation scripts (pre/post install, upgrade, uninstall)
  - Service control scripts
  - Configuration symlinks
  - Package metadata (INFO files)

### Runtime Data Links
- **Purpose**: Modern FHS compliance for runtime data
- **Symlinks**:
  - `/var/run` → `/run` (volatile runtime data)
  - `/var/lock` → `/run/lock` (lock files)
  - `/var/tmp` → `/tmp` (temporary files)
  - `/var/db` → `/volume1/@db/var/db` (persistent databases)

## Configuration Files

### Logging Configuration
- **syslog-ng.conf**: Central logging daemon configuration
  - Sources: /dev/log (unix socket), /proc/kmsg (kernel)
  - Extensive filtering by facility/severity
  - Separate destinations for different log types

### Log Rotation
- **logrotate.conf**: Main rotation configuration
  ```
  rotate 4
  size 1M
  compress
  compresscmd /usr/bin/xz
  compressext .xz
  compressoptions -3
  ```

### Package Configurations
- SafeAccess package includes:
  - IP blocking rules
  - DNS filtering settings
  - Web filtering policies
  - SQLite databases for access control

## Scripts and Executables

### SafeAccess Service Control
- **start-stop-status**: Main service control script
  - Installs syslog configurations
  - Sets up WebAPI endpoints
  - Manages IP blocking and DNS filtering
  - Handles network topology changes
  - Migrates settings from SRM 1.1

### Security Scanning Rules
- Python scripts for security checks:
  - Password policy enforcement
  - Firewall configuration validation
  - Service security assessments
  - Update status verification

## Integration Points

### System Services
- **syslog-ng**: Central logging service
- **logrotate**: Log file management
- **dpkg**: Package management
- **cron**: Scheduled task execution

### Security Components
- **NGFW**: Next-Gen Firewall with deep packet inspection
- **SafeAccess**: Content filtering and parental controls
- **Security Scanner**: Automated security assessments
- **PAM**: Authentication framework integration

### Network Services
- Multi-CPU packet filtering (CPU 0-3)
- nDPI for application-layer protocol detection
- Integration with firewall rules and QoS

## Security Considerations

### Strengths
1. **Restrictive Permissions**: All directories use 700 permissions
2. **Comprehensive Logging**: Detailed audit trails for all activities
3. **Multi-layer Security**: Authentication, firewall, and content filtering
4. **Proper Data Separation**: Volatile vs persistent data

### Vulnerabilities Identified
1. **Critical**:
   - Linux kernel 4.4.60 (EOL since Feb 2022)

2. **High Risk**:
   - Failed root login attempts detected (192.168.1.24)
   - No remote syslog forwarding configured

3. **Medium Risk**:
   - Firewall initialization errors (synonet command failures)
   - Software versions exposed in dpkg database
   - SQLite scalability limits for NGFW

4. **Low Risk**:
   - Verbose logging reveals network topology
   - Security rules expose monitoring patterns

### Recommendations
1. **Immediate Actions**:
   - Configure remote syslog for security logs
   - Investigate failed authentication attempts
   - Fix firewall initialization errors

2. **Strategic Improvements**:
   - Implement SIEM integration
   - Enable file integrity monitoring
   - Review log retention policies
   - Consider log encryption for sensitive data

## Network Services
- **Logging Services**: syslog-ng on standard syslog ports
- **Database Services**: SQLite for local data storage
- **Security Services**: Multi-threaded packet inspection

## Performance Considerations

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
- Consider separate partition for /var

## Maintenance Notes

### Log Management
- Monitor log file sizes (especially kern.log, wifi.log)
- Verify rotation is working properly
- Archive old logs to external storage
- Review compression effectiveness

### Package Updates
- Track package versions against CVE databases
- Monitor dpkg status for consistency
- Verify package integrity regularly

### Security Monitoring
- Regular review of auth.log for anomalies
- Monitor firewall logs for attack patterns
- Check security scan results
- Validate service configurations

### Performance Optimization
- Current log compression achieves ~90% reduction
- Multi-CPU packet processing scales to 4 cores
- SQLite heap limited to 42MB for NGFW
- Consider external storage for long-term logs

## Cross-References
- Default templates: [/var.defaults/](var.defaults.md)
- System configuration: [/etc/](etc.md)
- Service definitions: [/etc/init/](etc.md#upstart-services)
- Synology packages: [/volume1/@appstore/](volume1.md#application-packages)
- Security tools: [/usr/syno/bin/](usr.md#synology-specific-tools)
- Log rotation: [/etc/logrotate.d/](etc.md#log-rotation)
- Package binaries: [/usr/bin/](usr.md#user-binaries)

## Version Information
- **Document Version**: 2.1
- **Last Updated**: 2025-06-23
- **System**: Synology RT6600ax
- **Firmware**: SRM 5.2-9346
- **Analysis**: Complete variable data analysis with mesh networking details

---

[← Back to Documentation Index](../README.md) | [← Previous: /usr](usr.md) | [→ Next: /var defaults](var.defaults.md)

---
*This documentation was created as part of the comprehensive Synology SRM system analysis project.*
