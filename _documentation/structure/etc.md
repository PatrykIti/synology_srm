# /etc - Active System Configuration

[← Back to Documentation Index](../README.md) | [← Previous: /sbin](sbin.md) | [→ Next: /lib](lib.md)

---

## Overview
The `/etc` directory is the nerve center of the Synology SRM system, containing all active system configuration files, service definitions, and security policies. This directory controls network behavior, system services, user authentication, and security features. It represents the runtime configuration state of the router and is critical for system operation.

## Directory Structure
```
/etc/
├── apparmor.d/         # AppArmor security profiles
├── cups/               # Printing system configuration
├── dhcpc/              # DHCP client configuration
├── dhcpd/              # DHCP server configuration
├── firewall/           # Firewall rules (empty, rules in dumps)
├── fw_security/        # Security firewall settings
├── hostapd/            # WiFi access point configuration
├── httpd/              # Web server configuration
├── init/               # Upstart service definitions
├── iproute2/           # Advanced routing configuration
├── logrotate.d/        # Log rotation policies
├── pam.d/              # Authentication modules
├── php/                # PHP configuration
├── ppp/                # PPP/PPPoE configuration
├── ssh/                # SSH server configuration
├── ssl/                # SSL certificates and settings
├── sysconfig/          # System configuration files
└── syslog-ng/          # System logging configuration
```

## Key Components

### System Configuration Files
- **Purpose**: Core system behavior and identity
- **Location**: `/etc/`
- **Dependencies**: Used by all system services
- **Configuration**: Text-based configuration files
- **Security**: Contains sensitive system parameters

### Network Configuration
- **Purpose**: Network interfaces, routing, and services
- **Location**: `/etc/dhcpc/`, `/etc/dhcpd/`, `/etc/iproute2/`
- **Dependencies**: Network stack, kernel modules
- **Configuration**: Interface definitions, DHCP settings
- **Security**: Exposed passwords in WiFi configs

### Security Components
- **Purpose**: Firewall, AppArmor, authentication
- **Location**: `/etc/firewall/`, `/etc/fw_security/`, `/etc/apparmor.d/`
- **Dependencies**: Kernel security modules
- **Configuration**: Rule-based policies
- **Security**: Critical - DoS protection disabled

### Service Management
- **Purpose**: System service definitions and startup
- **Location**: `/etc/init/`
- **Dependencies**: Upstart init system
- **Configuration**: Service dependency chains
- **Security**: Services running with elevated privileges

## Configuration Files

### synoinfo.conf
**Path**: `/etc/synoinfo.conf`
**Purpose**: Central Synology system configuration defining device identity, features, and limits
**Format**: Key-value pairs

#### Key Parameters
| Parameter | Default Value | Description | Security Impact |
|-----------|---------------|-------------|-----------------|
| admin_port | 8000 | HTTP admin port | Should use HTTPS only |
| secure_admin_port | 8001 | HTTPS admin port | Secure management access |
| support_wireless | yes | WiFi support enabled | Increases attack surface |
| dos_protect_enable | no | DoS protection | CRITICAL - disabled |
| maxlanport | 4 | LAN port count | Physical security boundary |

### dhcpd.conf
**Path**: `/etc/dhcpd/dhcpd.conf`
**Purpose**: DHCP server configuration for LAN and guest networks
**Format**: ISC DHCP configuration

#### Key Parameters
| Parameter | Default Value | Description | Security Impact |
|-----------|---------------|-------------|-----------------|
| lbr0 range | 192.168.1.2-254 | Main LAN DHCP pool | Network segmentation |
| gbr0 range | 192.168.2.2-254 | Guest DHCP pool | Isolated network |
| lease-time | 86400 | 24-hour lease | Reasonable default |
| option routers | Interface IP | Default gateway | Trust boundary |

### fw_security/global.conf
**Path**: `/etc/fw_security/global.conf`
**Purpose**: Global firewall security settings
**Format**: INI-style configuration

```ini
[SETTINGS]
l2tp_passthrough_enable=yes
pptp_passthrough_enable=yes
dos_protect_enable=no
ipsec_passthrough_enable=yes
```

## Scripts and Executables

### rc.network
**Path**: `/etc/rc.network`
**Purpose**: Network initialization script
**Usage**: Called during system startup

#### Security Considerations
- Enables IP forwarding
- Sets up initial firewall rules
- Configures network interfaces

### rc.firewall
**Path**: `/etc/rc.firewall`
**Purpose**: Firewall initialization
**Usage**: Sets up iptables rules

#### Security Considerations
- Creates security chains
- Loads saved rules
- Must run before network services

## Integration Points

### Incoming Dependencies
- Kernel network stack depends on network configs
- Services depend on `/etc/init/` definitions
- Authentication system uses `/etc/pam.d/`

### Outgoing Dependencies
- Requires `/lib/` libraries
- Depends on kernel modules in `/lib/modules/`
- Uses binaries from `/bin/` and `/sbin/`

### Network Communication
- DHCP server: UDP 67/68
- SSH: TCP 22
- HTTP/HTTPS: TCP 80/443, 8000/8001
- DNS: UDP/TCP 53

## Security Considerations

### Access Control
- Most files owned by root:root
- Configuration files typically 644 or 600
- SSH keys properly protected (600)
- Some configs world-readable (security risk)

### Sensitive Data
- **CRITICAL**: WiFi passwords in plaintext
  - SSID: PatrykITI
  - Password: Cosik007Pc@
- SSH host keys properly protected
- DHCP leases contain client MACs

### Known Vulnerabilities
- DoS protection disabled
- WPS enabled on WiFi
- PPTP VPN (deprecated protocol) enabled
- No management frame protection (802.11w)
- UPnP service active (security risk)

### Security Best Practices
- Enable DoS protection immediately
- Disable WPS
- Use WPA3 if supported
- Disable PPTP, use modern VPN protocols
- Implement proper firewall rules
- Regular security updates

## Network Services

### DHCP Service
**Port**: UDP 67/68
**Protocol**: DHCP/BOOTP
**Purpose**: Dynamic IP assignment

#### Configuration
- Server config: `/etc/dhcpd/dhcpd.conf`
- Client config: `/etc/dhcpc/`
- Separate pools for LAN/guest

#### Security
- No DHCP snooping protection
- No ARP inspection
- Basic isolation between networks

### SSH Service
**Port**: TCP 22
**Protocol**: SSH v2
**Purpose**: Secure remote administration

#### Configuration
- Main config: `/etc/ssh/sshd_config`
- Host keys in `/etc/ssh/`
- PAM integration enabled

#### Security
- Key-based auth supported
- Root login status unknown
- Should implement fail2ban

## Performance Considerations

### Resource Usage
- Multiple service daemons
- Firewall processing overhead
- Log rotation prevents disk fill

### Optimization
- Service prioritization (nice values)
- Connection tracking limits
- Log level tuning

### Monitoring
- System logs in `/var/log/`
- Service status via init system
- Network statistics available

## Maintenance Notes

### Logging
- Centralized logging via syslog-ng
- Log rotation configured per service
- Remote syslog supported

### Backup Considerations
- Entire `/etc/` should be backed up
- Exclude generated files (*.bkp)
- Include custom configurations

### Updates and Patches
- Configuration may change with updates
- Backup before system updates
- Test changes in maintenance window

### Troubleshooting
- Check service logs first
- Verify configuration syntax
- Use init system for service control
- Network issues: check routing tables

## Cross-References
- Service definitions: [/etc/init/](etc.md#upstart-services)
- Network scripts: [/sbin/](sbin.md)
- Libraries: [/lib/](lib.md)
- Defaults: [/etc.defaults/](etc.defaults.md)

## Version Information
- **Document Version**: 1.0
- **Last Updated**: 2025-06-21
- **Component Version**: SRM 1.3.x
- **Analysis Tools Used**: MCP Zen with Gemini Pro

---

[← Back to Documentation Index](../README.md) | [← Previous: /sbin](sbin.md) | [→ Next: /lib](lib.md)

---
*This documentation was created as part of the comprehensive Synology SRM system analysis project.*
