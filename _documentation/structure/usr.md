# /usr - User Programs and Libraries

[← Back to Documentation Index](../README.md) | [← Previous: /lib](lib.md) | [→ Next: /var](var.md)

---

## Overview
The `/usr` directory contains user-space applications, libraries, and architecture-independent data for the Synology SRM router system. Occupying 296MB, it represents the bulk of the router's feature-rich functionality. The directory is dominated by Synology's proprietary Router Manager software suite in `/usr/syno` (185MB, 62.5%), while maintaining standard Unix directories for compatibility. This ARM aarch64-optimized structure reflects deliberate design choices for an embedded router system prioritizing stability, security, and performance.

## Directory Structure
```
/usr/
├── syno/               # Synology Router Manager core (185MB, 62.5%)
│   ├── bin/            # Router management tools
│   ├── sbin/           # System daemons
│   ├── synoman/        # Web management interface
│   ├── etc/            # Service configurations
│   ├── lib/            # Custom libraries
│   └── [20+ dirs]      # Various services
├── bin/                # User binaries (66MB, 142 files)
├── sbin/               # System admin tools (15MB, 76 files)
├── share/              # Architecture-independent data (29MB, 4,242 files)
├── libexec/            # Support executables (708KB, 147 files)
├── etc/                # Configuration files (384KB)
├── local/              # Local installations (4KB)
├── var/                # Variable data (empty)
├── lib → ../lib        # Symlink to system libraries
└── lib64 → ../lib64    # Symlink to 64-bit libraries
```

## Key Components

### Synology Router Manager Core
- **Purpose**: Complete router management system with enterprise features
- **Location**: `/usr/syno/` (185MB)
- **Dependencies**: D-Bus, Upstart, kernel modules
- **Configuration**: JSON-based in `/usr/syno/etc/`
- **Security**: Compiled CGI binaries, token-based authentication

### Standard Unix Utilities
- **Purpose**: Basic system and user commands
- **Location**: `/usr/bin/`, `/usr/sbin/`
- **Dependencies**: BusyBox v1.16.1 multi-call binary
- **Configuration**: Various per-tool configs
- **Security**: No SUID/SGID bits (good practice)

### Web Management Interface
- **Purpose**: Browser-based router administration
- **Location**: `/usr/syno/synoman/`
- **Dependencies**: Angular.js, SDS framework
- **Configuration**: API definitions in JSON
- **Security**: Compiled CGI for hardening

### Architecture-Independent Data
- **Purpose**: Shared resources, documentation, configs
- **Location**: `/usr/share/`
- **Dependencies**: Various services and applications
- **Configuration**: Templates and examples
- **Security**: CA certificates, RADIUS dictionaries

## Configuration Files

### Service Definitions
**Path**: `/usr/syno/etc/synoservice.d/`
**Purpose**: Define Synology services and dependencies
**Format**: JSON with service metadata

#### Service Configuration Structure
| Field | Purpose | Example |
|-------|---------|---------|
| init_job_map | Upstart job mapping | "synoconfd" |
| auto_start | Automatic startup | true/false |
| required_synoservice | Dependencies | ["dbus"] |
| firewall_section_map | Firewall rules | "router" |

### Mesh Network Configuration
**Path**: `/usr/syno/etc/mesh/`
**Purpose**: Mesh networking and topology settings
**Format**: JSON configuration files

#### Key Mesh Parameters
- HYD (Hybrid Bridge) system configuration
- Port mappings (7777-8892)
- IEEE 1905.1 standard implementation
- Wireless backhaul settings

## Scripts and Executables

### synoroutertool
**Path**: `/usr/syno/sbin/synoroutertool`
**Purpose**: Main router management utility
**Usage**: Internal use by web interface and services

#### Router Management Suite
| Tool | Purpose | Size |
|------|---------|------|
| synorouterportfwd | Port forwarding management | 103KB |
| synowandetectiontool | WAN detection utility | 12KB |
| synofirewall | Firewall daemon | 37KB |
| synodhcpserver | DHCP server daemon | 20KB |

### Network Management Tools
**Path**: `/usr/sbin/`
**Purpose**: Advanced network configuration
**Usage**: System administration tasks

#### Wireless Management (Qualcomm Atheros)
| Tool | Purpose | Features |
|------|---------|----------|
| wifitool | WiFi configuration | Band steering, TR-069 |
| wlanconfig | WLAN interface config | Flow tagging |
| cfg80211tool | Linux wireless API | Standard compliance |
| athstats | Atheros statistics | Hardware monitoring |

## Integration Points

### Incoming Dependencies
- Kernel loads firmware from `/usr/lib/firmware/`
- Services started by Upstart read from `/usr/syno/etc/`
- Web UI served by nginx/lighttpd from `/usr/syno/synoman/`
- Package Center installs to `/usr/syno/synopkg/`

### Outgoing Dependencies
- Binaries link to libraries in `/lib/`
- Services communicate via D-Bus system bus
- Configuration reads from `/etc/` at runtime
- Logs write to `/var/log/`

### Network Communication
- Web management: HTTP/HTTPS on ports 8000/8001
- Mesh networking: Custom ports 7777-8892
- Service APIs: D-Bus and Unix sockets
- External updates: HTTPS to Synology servers

## Security Considerations

### Access Control
- Directory permissions: 755 (standard)
- Binary permissions: 755 or 700
- No SUID/SGID binaries (excellent security practice)
- Web interface uses token-based authentication

### Sensitive Operations
- Router configuration changes
- Firewall rule modifications
- Port forwarding setup
- Mesh network topology changes
- Package installation

### Known Vulnerabilities
- **CRITICAL**: Python 2.7 (EOL 2020) - no security updates
- **HIGH**: BusyBox v1.16.1 (2011) - multiple known CVEs
- **MEDIUM**: Potential unpatched Synology components
- **NOTE**: Compiled CGI binaries reduce script injection risks

### Security Best Practices
- Immediate Python 2.7 removal/upgrade required
- BusyBox update to current version critical
- Regular firmware updates essential
- Disable unused services
- Implement network segmentation

## Network Services

### Core Router Services
- **DHCP Server**: dnsmasq-based with DNS integration
- **Firewall**: Next-Gen Firewall (ngfw) with IPS
- **VPN**: OpenVPN, L2TP/IPsec, PPTP support
- **Mesh**: Self-Organizing Network (SON) with HYD

### Management Services
- **Web UI**: Angular.js SPA on 8000/8001
- **API Gateway**: RESTful APIs via CGI
- **Service Control**: D-Bus service mesh
- **Update Service**: Auto-update security databases

## Performance Considerations

### Resource Usage
- Total footprint: 296MB (efficient for feature set)
- Memory: Compiled binaries minimize RAM usage
- CPU: ARM64 optimized for QCA platform
- Storage: Read-only mount typical for /usr

### Optimization
- BusyBox multi-call reduces binary duplication
- Compiled CGI vs interpreted scripts
- Stripped binaries throughout
- Hardware acceleration for crypto/networking

### Monitoring
- Service status via synoservice
- Resource usage in /proc
- Network stats via kernel interfaces
- Web UI performance dashboard

## Maintenance Notes

### Logging
- Service logs: `/var/log/`
- Web access logs: `/var/log/synoman/`
- System events: syslog-ng aggregation
- Debug modes available per service

### Backup Considerations
- `/usr/` typically read-only, restored from firmware
- Custom packages in `/usr/syno/synopkg/`
- Configuration overrides in `/usr/syno/etc.defaults/`
- No user data stored in `/usr/`

### Updates and Patches
- Firmware updates replace entire `/usr/`
- Package updates via Package Center
- Security database updates automatic
- Version checks against Synology servers

### Troubleshooting
- Compare `/etc/` with `/usr/syno/etc.defaults/`
- Check service status with servicetool
- Review logs for service failures
- Verify library dependencies with ldd

## Cross-References
- System binaries: [/bin/](bin.md), [/sbin/](sbin.md)
- Libraries: [/lib/](lib.md)
- Runtime config: [/etc/](etc.md)
- Variable data: [/var/](var.md)
- Default configs: [/etc.defaults/](etc.defaults.md)

## Version Information
- **Document Version**: 1.0
- **Last Updated**: 2025-06-21
- **Component Versions**:
  - SRM: 11.x
  - Python: 2.7 (EOL - CRITICAL)
  - BusyBox: v1.16.1 (2011 - OUTDATED)
  - Architecture: ARM aarch64
- **Analysis Tools Used**: MCP Zen with Gemini Pro, parallel subagents

---

[← Back to Documentation Index](../README.md) | [← Previous: /lib](lib.md) | [→ Next: /var](var.md)

---
*This documentation was created as part of the comprehensive Synology SRM system analysis project.*