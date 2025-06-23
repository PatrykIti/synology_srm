# /usr Directory - User Programs and Libraries

[← Back to Documentation Index](../README.md) | [← Previous: /sbin](sbin.md) | [→ Next: /var](var.md)

---
---

## Overview
The `/usr` directory contains user-space applications, libraries, and architecture-independent data for the Synology SRM router system. This directory represents the bulk of the router's feature-rich functionality, dominated by Synology's proprietary Router Manager software suite in `/usr/syno/`. The ARM aarch64-optimized structure reflects deliberate design choices for an embedded router system prioritizing stability, security, and performance.

## Directory Structure
```
/usr/
├── syno/               # Synology Router Manager core
│   ├── bin/            # Router management tools
│   ├── sbin/           # System daemons
│   ├── synoman/        # Web management interface
│   ├── etc/            # Service configurations
│   ├── lib/            # Custom libraries
│   └── [25+ dirs]      # Various services
├── bin/                # User binaries (206 files)
│   ├── [55 BusyBox]    # Basic Unix utilities
│   └── [141 standalone] # Specialized tools
├── sbin/               # System admin tools (85 files)
├── share/              # Architecture-independent data
│   ├── ca-certificates/# 141 Mozilla CA certs
│   ├── captiveportal/  # Guest network portal
│   ├── freeradius/     # 222 RADIUS dictionaries
│   └── [14+ dirs]      # Various shared data
├── libexec/            # Helper executables (147 files)
│   ├── net/            # Network event hooks
│   ├── volume/         # Storage hooks
│   └── [20+ dirs]      # Service integration
├── etc/                # Additional configs
│   └── raddb/          # RADIUS configuration
├── local/              # Local installations
├── var/                # Variable data links
├── lib → ../lib        # Symlink to system libraries
└── lib64 → ../lib64    # Symlink to 64-bit libraries
```

## Key Components

### Synology Router Manager Core (/usr/syno)
- **Purpose**: Complete router management system with enterprise features
- **Location**: `/usr/syno/` (25+ subdirectories)
- **Dependencies**: D-Bus, Upstart, kernel modules
- **Configuration**: JSON-based service definitions, mesh configs
- **Security**: Compiled CGI binaries, token authentication, code signing

#### Major Synology Components
| Component | Directory | Purpose |
|-----------|-----------|---------|
| Web UI | synoman/ | Angular.js management interface |
| Package Manager | synopkg/ | Third-party app management |
| Mesh Network | etc/mesh/ | Mesh WiFi configuration |
| Security Scan | securityscan/ | System integrity verification |
| Backup System | synobackup/ | Configuration backup |
| Traffic Report | traffic_report/ | Network analytics |

### User Binaries (/usr/bin)
- **Total Count**: 206 binaries
- **BusyBox Applets**: 55 (27%) - Basic Unix utilities
- **Standalone Binaries**: 141 (68%) - Specialized tools
- **Security Tools**: 32 - GPG suite, SSH, AppArmor
- **Network Tools**: 36 - iptables, curl, wget, Samba
- **No SUID/SGID**: Excellent security practice

### System Administration Tools (/usr/sbin)
- **Total Count**: 85 binaries
- **Wireless Management**: Qualcomm Atheros tools (wifitool, wlanconfig)
- **Router Services**: synoroutertool, synofirewall, miniupnpd
- **Network Daemons**: dnsmasq, hostapd, pppd
- **System Services**: udevd, syslog-ng, crond

### Architecture-Independent Data (/usr/share)
- **CA Certificates**: 141 Mozilla root certificates
- **Captive Portal**: Complete guest network web application
- **RADIUS Dictionaries**: 222 vendor dictionaries for authentication
- **Documentation**: OpenSSL complete reference
- **Localization**: ICU data, timezone information

### Helper Executables (/usr/libexec)
- **Network Hooks**: 90+ scripts for network events
  - Interface state changes (link up/down)
  - IP address changes (IPv4/IPv6)
  - Topology modifications
  - Gateway updates
- **Service Hooks**: Integration scripts following SDK patterns
  - Volume mount/unmount
  - Share management
  - User/group operations
  - Database updates
- **Synology SDK Pattern**: All scripts support:
  - `--sdk-mod-ver`: Version reporting
  - `--name`: Package identification
  - `--vendor`: Vendor attribution
  - `--pre/--post`: Execution phases

## Configuration Files

### Service Definitions (/usr/syno/etc)
**Purpose**: Define Synology services and dependencies
**Format**: JSON with metadata

#### Key Configuration Categories
| Category | Files | Purpose |
|----------|-------|---------|
| Firewall | iptables_*, synofirewall.db | Firewall rules and mappings |
| Network | network_policy.conf, miniupnpd.conf | Network behavior |
| Mesh | mesh/*.json | Mesh networking topology |
| WiFi | wifi/*.conf | Wireless configurations |
| Security | strongpassword.conf | Password policies |

### RADIUS Configuration (/usr/etc/raddb)
- **Server Config**: radiusd.conf, proxy.conf
- **Enabled Modules**: 27 authentication modules
- **Available Modules**: 50+ additional modules
- **Policies**: Comprehensive policy definitions

## Scripts and Executables

### Router Management Suite
| Tool | Purpose | Location |
|------|---------|----------|
| synoroutertool | Main router utility | /usr/syno/sbin/ |
| synorouterportfwd | Port forwarding | /usr/syno/bin/ |
| synofirewall | Firewall daemon | /usr/syno/sbin/ |
| synodhcpserver | DHCP server | /usr/syno/sbin/ |
| synowandetectiontool | WAN detection | /usr/syno/bin/ |

### Network Event Handling
**Topology Change Hooks** (highest priority):
- `smartwan_pre.sh` / `smartwan_post.sh` - Dual WAN management
- `firewall_reload_hook.sh` - Firewall rule updates
- `mesh_topology_change.sh` - Mesh network adjustments
- `qosRestart.sh` - QoS reconfiguration
- 25+ additional topology scripts

**IP Change Hooks**:
- DDNS updates
- NAT reconfiguration
- Static route updates
- IPv6 addressing
- Service notifications

## Integration Points

### Service Dependencies
- **Upstart Jobs**: Service startup via /etc/init/
- **D-Bus Communication**: Inter-process messaging
- **Hook Scripts**: Event-driven integration
- **Package System**: Third-party app installation

### Network Services
- **Web Management**: Ports 8000/8001 (HTTP/HTTPS)
- **Mesh Networking**: Ports 7777-8892
- **SSH Management**: Port 22 for mesh nodes
- **RADIUS**: Authentication services
- **VPN**: Multiple protocols supported

## Security Considerations

### Strengths
1. **No SUID/SGID Binaries**: In /usr/bin reduces privilege escalation
2. **Compiled CGI**: Web interface hardened against injection
3. **Comprehensive Tools**: GPG, SSH, AppArmor available
4. **Certificate Store**: 141 trusted CA certificates
5. **Code Signing**: Self-check integrity verification

### Vulnerabilities
1. **Python 2.7**: End-of-life, no security updates
2. **BusyBox v1.16.1**: Multiple known CVEs
3. **OpenSSL Version**: Needs verification for currency
4. **ImageMagick**: Properly restricted via policy.xml

### Security Features
- **Next-Gen Firewall**: Deep packet inspection
- **SafeAccess**: Content filtering/parental controls
- **VPN Support**: L2TP/IPsec, OpenVPN, PPTP
- **Network Isolation**: Guest network separation
- **Traffic Analysis**: Real-time threat detection

## Network Services

### Core Router Services
| Service | Implementation | Features |
|---------|---------------|----------|
| DHCP/DNS | dnsmasq | Integrated caching DNS |
| Firewall | NGFW + iptables | IPS, application control |
| WiFi | hostapd + Atheros | Mesh, band steering |
| VPN | OpenVPN, IPsec | Multiple protocols |
| UPnP | miniupnpd | Port mapping |

### Management Services
- **Web UI**: Angular.js SPA with compiled CGI backend
- **API Gateway**: Comprehensive REST APIs
- **Service Control**: systemd-style job management
- **Package Center**: Third-party app ecosystem

## Performance Considerations

### Optimization Strategies
1. **BusyBox Multi-call**: Reduces binary duplication
2. **Compiled CGI**: Faster than interpreted scripts
3. **Stripped Binaries**: Minimal size throughout
4. **Hardware Acceleration**: QCA platform optimizations
5. **Event-driven Architecture**: Hook-based integration

### Resource Management
- **Memory**: Efficient binary sharing
- **CPU**: ARM64 optimized compilation
- **Storage**: Read-only mount typical
- **Network**: Hardware offload capable

## Maintenance Notes

### Update Mechanism
1. **Firmware Updates**: Replace entire /usr
2. **Package Updates**: Via Package Center
3. **Security Databases**: Auto-update capability
4. **Configuration**: Preserved in /etc

### Troubleshooting Tools
- Service status: `synoservice`
- Network diagnosis: Comprehensive toolset
- Log analysis: Centralized syslog-ng
- Configuration comparison: defaults vs active

### Best Practices
1. Regular firmware updates critical
2. Disable unused services
3. Monitor security advisories
4. Backup configuration regularly
5. Use mesh security features

## Platform-Specific Features

### RT6600ax Optimizations
- **Qualcomm IPQ6018**: Hardware acceleration
- **Mesh Networking**: SON (Self-Organizing Network)
- **WiFi 6**: 802.11ax support
- **Multi-CPU**: Packet processing optimization
- **Hardware Crypto**: Acceleration available

### Synology Ecosystem Integration
- **QuickConnect**: Remote access service
- **DDNS**: Multiple provider support
- **Cloud Sync**: Configuration backup
- **Mobile Apps**: Remote management
- **Package Ecosystem**: Expanding functionality

## Cross-References
- System binaries: [/bin/](bin.md), [/sbin/](sbin.md)
- Libraries: [/lib/](lib.md)
- Configuration: [/etc/](etc.md)
- Variable data: [/var/](var.md)
- Default configs: [/etc.defaults/](etc.defaults.md)

## Version Information
- **Document Version**: 2.0
- **Last Updated**: 2025-06-23
- **System**: Synology RT6600ax
- **Firmware**: SRM 5.2-9346
- **Architecture**: ARM aarch64
- **Analysis**: Complete directory analysis with subagents

---

[← Back to Documentation Index](../README.md) | [← Previous: /sbin](sbin.md) | [→ Next: /var](var.md)

---
*This documentation was created as part of the comprehensive Synology SRM system analysis project.*
