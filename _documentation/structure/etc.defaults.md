# /etc.defaults Directory - Default Configuration Templates

[← Back to Documentation Index](../README.md) | [← Previous: /etc](etc.md) | [→ Next: /ini](ini.md)

---

## Overview
The `/etc.defaults` directory contains pristine default configuration templates for the Synology SRM system. These files serve as factory defaults that can be used to restore system settings, as fallback configurations, or as templates for creating new configurations. This directory follows a structure parallel to `/etc` but contains only the original, unmodified versions of configuration files.

## Directory Structure
```
/etc.defaults/
├── apparmor/               [AppArmor security module configs]
├── apparmor.d/             [AppArmor profiles and abstractions]
│   ├── abstractions/       [Reusable AppArmor policy snippets]
│   ├── cache/              [Cached AppArmor profiles]
│   ├── httpd/              [Apache-specific profiles]
│   └── tunables/           [AppArmor variables]
├── cups/                   [CUPS printing system]
├── debsig/                 [Debian package signatures]
├── default/                [Service environment defaults]
├── dhclient/               [ISC DHCP client configs]
├── dhcpc/                  [DHCP client utilities]
├── dhcpd/                  [DHCP server configs]
├── dpkg/                   [Debian package manager]
├── firewall/               [Firewall rules - empty]
├── fw_security/            [Firewall security features]
├── hostapd/                [Wi-Fi access point daemon]
├── httpd/                  [Apache HTTP Server]
│   ├── conf/               [Main Apache configs]
│   ├── sites-enabled/      [Enabled virtual hosts]
│   └── sites-enabled-user/ [User virtual hosts]
├── init/                   [Upstart service configs - 268 files]
├── iproute2/               [Network configuration utilities]
├── ipsec.d/                [IPsec VPN configs - empty]
├── logrotate.d/            [Log rotation rules]
├── netatalk/               [Apple Filing Protocol - empty]
├── nfs/                    [Network File System]
├── pam.d/                  [PAM authentication modules]
├── php/                    [PHP configuration]
├── portforward/            [Port forwarding - empty]
├── postgresql/             [PostgreSQL database]
├── ppp/                    [PPP/PPPoE configuration]
├── rc.d/                   [System V init scripts]
├── security/               [Security configurations]
├── ssh/                    [SSH daemon configuration]
├── ssl/                    [SSL/TLS certificates and configs]
│   ├── certs/              [CA certificates bundle]
│   └── private/            [Private keys - empty]
├── ssmtp/                  [Simple SMTP agent]
├── sudoers.d/              [sudo rules - empty]
├── synosyslog/             [Synology syslog configs]
├── sysconfig/              [System configuration]
│   ├── network-scripts/    [Network interface configs]
│   └── networking/         [Additional network configs]
├── sysctlconf/             [Kernel parameters]
├── syslog-ng/              [Advanced logging daemon]
│   └── patterndb.d/        [Log parsing patterns]
└── tc/                     [Traffic control/QoS]
```

## Key Components

### System Configuration Files
- **Purpose**: Core system configuration templates
- **Key Files**:
  - `synoinfo.conf` - Central Synology configuration (289 lines)
  - `VERSION` - System version information
  - `hostname` - Default device hostname
  - `fstab` - File system mount table
  - `hosts` - Static hostname mappings
  - `passwd/shadow/group` - User account templates
- **Configuration**: Defines system identity, hardware parameters, feature flags
- **Security**: Contains default admin accounts and system users

### Network Configuration
- **Purpose**: Default network settings and services
- **Components**:
  - DHCP client/server configurations
  - PPPoE connection templates
  - Network interface definitions (eth0-4, wlan0-1, lbr0, gbr0)
  - DNS resolver settings
  - Traffic control rules
- **Dependencies**: Used by network initialization scripts
- **Configuration**: Bridge interfaces for LAN/Guest networks pre-configured

### Service Initialization (/init)
- **Purpose**: Upstart service definitions (268 .conf files)
- **Categories**:
  - Core system services (crond, syslog-ng, dbus)
  - Network services (dhcp, dns, firewall, wifi)
  - Synology services (syno*, dsm*)
  - Storage services (samba, nfs, afp)
  - Web services (httpd, php-fpm, webdav)
- **Integration**: Defines service dependencies and startup order
- **Security**: Controls service privileges and capabilities

### Security Framework
- **AppArmor Profiles**:
  - Mandatory access control for applications
  - Abstractions for common access patterns
  - Cached profiles for Synology services
  - Disabled by default (SUBDOMAIN_ENABLE_OWLSM="no")
  
- **PAM Configuration**:
  - Authentication stacks for system services
  - Includes webui, sshd, ftpd, samba, sudo
  - Winbind integration for AD domains
  
- **SSL/TLS**:
  - CA certificates bundle (138 root CAs)
  - OpenSSL configuration templates
  - Certificate Transparency log configuration

### Web Services (/httpd)
- **Purpose**: Apache HTTP Server default configuration
- **Structure**:
  - System-level config (httpd.conf-sys)
  - User-level config (httpd.conf-user)
  - WebDAV config (httpd.conf-webdav)
  - SSL/TLS configurations
  - Virtual host templates
- **Security**: Default SSL redirection rules
- **Integration**: PHP-FPM for dynamic content

## Configuration Files

### Critical System Files
- **synoinfo.conf**: Master configuration with hardware specs, feature flags, limits
- **sysctl.conf**: Kernel parameters for performance and security
- **logrotate.conf**: System-wide log rotation (4 rotations, 1MB size, XZ compression)
- **nsswitch.conf**: Name service resolution order
- **resolv.conf**: DNS resolver configuration

### Service-Specific Configs
- **sshd_config**: SSH daemon settings
- **syno_sshd_config**: Synology SSH customizations
- **cupsd.conf**: CUPS printing service
- **postgresql.conf**: Database server settings
- **php.ini**: PHP interpreter configuration

## Scripts and Executables

### System Scripts
- **rc.*** scripts: System initialization and service management
  - `rc.network` - Network initialization
  - `rc.wifi` - Wireless configuration
  - `rc.volume` - Storage volume management
  - `rc.fan` - Thermal management
  
### Installation Scripts
- **synogrinst.sh**: Generic installation framework
- **installer.sh**: Package installation handler
- **upgrade.sh**: System upgrade procedures
- **newdisk.sh**: New disk initialization

### Utility Scripts
- **pppoe-generate-config.py**: Dynamic PPPoE configuration
- **dhclient-script**: DHCP client hooks

## Integration Points

### Configuration Hierarchy
1. System reads defaults from `/etc.defaults`
2. Applies overrides from `/etc`
3. Runtime modifications stored in `/etc`
4. Factory reset restores from `/etc.defaults`

### Service Dependencies
- Upstart manages service lifecycle
- PAM handles authentication
- AppArmor provides MAC
- syslog-ng centralizes logging

### Package Management
- dpkg tracks installed packages
- Package-specific configs in subdirectories
- Synology packages use .override files

## Security Considerations

### Default Security Posture
1. **Restrictive Permissions**: All files 700 (owner-only)
2. **Disabled Services**: Many security features off by default
3. **Template Keys**: No actual private keys in defaults
4. **Basic Authentication**: PAM stacks pre-configured

### Vulnerabilities
1. **Known Defaults**: Predictable initial configurations
2. **Weak Protocols**: Some legacy protocols enabled
3. **Information Disclosure**: Hardware details in synoinfo.conf

### Hardening Opportunities
1. Enable AppArmor profiles
2. Restrict service configurations
3. Update SSL/TLS settings
4. Implement stricter PAM policies

## Network Services
- **DHCP**: Client and server configurations
- **DNS**: Resolver and DDNS settings
- **Firewall**: iptables/ebtables templates
- **VPN**: IPsec/PPP configurations ready
- **Wi-Fi**: hostapd for access point mode

## Performance Considerations

### Resource Usage
- **Disk Space**: ~50MB for complete default configurations
- **Memory**: No runtime memory usage (reference only)
- **CPU**: No CPU impact (passive storage)
- **I/O**: Minimal - only during factory reset or template access

### Performance Impact
- **Boot Time**: No impact unless factory reset triggered
- **Runtime**: Zero performance overhead
- **Updates**: Fast system updates due to template separation
- **Recovery**: Quick factory reset capability

### Optimization Notes
- Files are read-only, preventing fragmentation
- Organized directory structure enables fast lookups
- Template approach reduces configuration parsing overhead
- Separation from `/etc` prevents accidental modifications

## Maintenance Notes

### Configuration Management
- Always backup `/etc` before applying defaults
- Use diff to compare active vs default configs
- Version control custom modifications
- Document deviations from defaults

### Update Considerations
- System updates may modify defaults
- Preserve custom configurations separately
- Review new defaults after updates
- Test restoration procedures

### Best Practices
1. **Minimal Modifications**: Change only necessary settings
2. **Documentation**: Record all customizations
3. **Regular Audits**: Compare with defaults periodically
4. **Backup Strategy**: Include both `/etc` and `/etc.defaults`

## Relationship with /etc

### Usage Patterns
1. **Initial Setup**: Copies from defaults to active
2. **Factory Reset**: Restores from defaults
3. **Fallback**: Uses defaults if active config missing
4. **Templates**: Reference for new configurations

### Key Differences Found
- `/etc` has 145 unique files (runtime-generated)
- `/etc.defaults` has 3 unique files (updater configs)
- 583 files exist in both directories
- `/etc` contains .override files for customization
- Runtime state (PIDs, caches) only in `/etc`

### Configuration Flow
```
/etc.defaults → [Copy/Reference] → /etc → [Runtime Modifications] → Active Config
                        ↑                            ↓
                   [Factory Reset]           [User Customization]
```

## Cross-References
- Active configurations: [/etc/](etc.md)
- Service executables: [/usr/sbin/](usr.sbin.md)
- Synology scripts: [/usr/syno/](usr.syno.md)
- System libraries: [/lib/](lib.md)
- Kernel modules: [/lib/modules/](lib.md#kernel-modules)
- Log files: [/var/log/](var.md#system-logs)
- Runtime data: [/var/](var.md)

---

[← Back to Documentation Index](../README.md) | [← Previous: /etc](etc.md) | [→ Next: /ini](ini.md)