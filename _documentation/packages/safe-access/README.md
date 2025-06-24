# Safe Access - Package Analysis

[← Back to Package Index](../index.md) | [← Previous Package](previous-package.md) | [→ Next Package](next-package.md)

---

## Package Identification & Metadata

### Basic Information
- **Package Name**: SafeAccess
- **Version**: 1.3.1-0326
- **Vendor/Author**: Synology Inc.
- **License**: Proprietary
- **Release Date**: May 17, 2022 (20220517-18:17:45)
- **Source**: Synology official
- **Package Manager ID**: com.synology.SafeAccess

### Package Description
Safe Access is a comprehensive parental control and web filtering solution for Synology Router Manager (SRM). It provides time-based access control, web content filtering, safe browsing protection, and detailed usage monitoring for network devices.

## Package Structure & Contents

### Installation Paths
```
Primary installation directory: /var/packages/SafeAccess/
Binary location: /volume1/@appstore/SafeAccess/bin/
Configuration: /var/packages/SafeAccess/etc/
Data storage: /var/packages/SafeAccess/var/
Web components: /volume1/@appstore/SafeAccess/ui/
```

### Directory Structure
```
/var/packages/SafeAccess/
├── INFO                    # Package metadata
├── PACKAGE_ICON.PNG       # Package icon (256x256)
├── PACKAGE_ICON_120.PNG   # Package icon (120x120) 
├── PACKAGE_ICON_144.PNG   # Package icon (144x144)
├── PACKAGE_ICON_24.PNG    # Package icon (24x24)
├── PACKAGE_ICON_256.PNG   # Package icon (256x256)
├── PACKAGE_ICON_48.PNG    # Package icon (48x48)
├── PACKAGE_ICON_64.PNG    # Package icon (64x64)
├── PACKAGE_ICON_72.PNG    # Package icon (72x72)
├── PACKAGE_ICON_90.PNG    # Package icon (90x90)
├── PACKAGE_ICON_96.PNG    # Package icon (96x96)
├── WIZARD_UIFILES/        # Installation wizard UI
├── conf/                  # Package configuration
│   └── privilege         # Permission definitions
├── scripts/               # Installation/maintenance scripts
│   ├── postinst
│   ├── postuninst
│   ├── postupgrade
│   ├── preinst
│   ├── preuninst
│   ├── preupgrade
│   ├── reset
│   ├── start-stop-status
│   └── start-stop-status.bak
├── target -> /volume1/@appstore/SafeAccess/  # Symlink to main installation
└── var/                   # Variable data

/volume1/@appstore/SafeAccess/
├── bin/                   # Executable files
│   ├── migrate_access_control_db.py
│   ├── migrate_all_db.py
│   ├── migrate_conf_file.py
│   ├── migrate_log_db.py
│   ├── migrate_notification_db.py
│   ├── migrate_pc_db.py
│   ├── safe_browsing_client
│   ├── synoaccesscontroltool
│   ├── synoactool
│   ├── synoipblock
│   ├── synopctool
│   ├── synosafeaccessfilterd
│   ├── synosafeaccesslog
│   └── synotimespentd
├── block_page/            # Block page templates
│   ├── blocktime/
│   ├── security/
│   ├── timequota/
│   └── webfilter/
├── conf/                  # Configuration files
├── etc/                   # Service configurations
│   ├── httpd/
│   └── security.settings
├── lib/                   # Shared libraries
│   ├── libpcpp.so.0 -> libpcpp.so.0.0.0
│   ├── libpcpp.so.0.0.0
│   ├── libsynoaccesscontrol.so -> libsynoaccesscontrol.so.1
│   ├── libsynoaccesscontrol.so.1 -> libsynoaccesscontrol.so.1.1.0
│   ├── libsynoaccesscontrol.so.1.1.0
│   ├── libsynoipblock.so -> libsynoipblock.so.1
│   ├── libsynoipblock.so.1 -> libsynoipblock.so.1.0.0
│   ├── libsynoipblock.so.1.0.0
│   ├── libsynoparentalcontrol.so -> libsynoparentalcontrol.so.1
│   ├── libsynoparentalcontrol.so.1 -> libsynoparentalcontrol.so.1.0.0
│   ├── libsynoparentalcontrol.so.1.0.0
│   ├── libsynosafeaccesslog.so -> libsynosafeaccesslog.so.1
│   ├── libsynosafeaccesslog.so.1 -> libsynosafeaccesslog.so.1.0.0
│   ├── libsynosafeaccesslog.so.1.0.0
│   ├── libsynosafebrowsing.so -> libsynosafebrowsing.so.1
│   ├── libsynosafebrowsing.so.1 -> libsynosafebrowsing.so.1.0.0
│   └── libsynosafebrowsing.so.1.0.0
├── ui/                    # Web interface
│   ├── config
│   ├── help/             # Multi-language help files
│   ├── images/
│   ├── index.cgi
│   ├── libs/             # JavaScript libraries
│   ├── modules/          # ExtJS modules
│   ├── scripts/
│   ├── style.css
│   └── texts/            # Localization files
├── var/                   # Variable data
│   └── db/               # Database schemas
└── webapi/               # Web API definitions
    ├── lib/
    └── src/

```

### Key Files and Components
| File/Directory | Purpose | Type |
|----------------|---------|------|
| synosafeaccessfilterd | Main filtering daemon | Binary |
| synotimespentd | Time tracking daemon | Binary |
| safe_browsing_client | Safe browsing service client | Binary |
| synoactool | Access control management tool | Binary |
| synopctool | Parental control management tool | Binary |
| synoipblock | IP blocking utility | Binary |
| libsynoaccesscontrol.so | Access control library | Library |
| libsynoparentalcontrol.so | Parental control library | Library |
| libsynosafebrowsing.so | Safe browsing library | Library |
| block_page/* | Blocked content pages | Web/CGI |
| webapi/* | REST API definitions | Config |

## Digital Signatures & Integrity

### Package Signature
- **Signed**: No
- **Signature Type**: Not found
- **Signing Authority**: N/A
- **Certificate Details**: N/A

⚠️ **Security Warning**: No digital signatures found for package verification. The package integrity cannot be cryptographically verified.

### File Integrity
| File | Permissions | Owner | Size |
|------|-------------|-------|------|
| synosafeaccessfilterd | 700 | root | Binary executable |
| synotimespentd | 700 | root | Binary executable |
| safe_browsing_client | 700 | root | Binary executable |
| libsynoaccesscontrol.so.1.1.0 | 700 | root | Shared library |
| libsynoparentalcontrol.so.1.0.0 | 700 | root | Shared library |

### Verification Commands
```bash
# Check file permissions
ls -la /volume1/@appstore/SafeAccess/bin/

# Verify library dependencies
ldd /volume1/@appstore/SafeAccess/bin/synosafeaccessfilterd

# Check for signatures (none found)
file /var/packages/SafeAccess/*
```

## Technologies Used

### Programming Languages
- **Primary Language**: C/C++
  - Evidence: ELF 64-bit LSB pie executables, ARM aarch64 architecture
  - Components: All core binaries and libraries
  - Compiler: GCC 10.3.0 (aarch64-unknown-linux-gnu)
  
- **Secondary Languages**: 
  - **Python**: Migration scripts (migrate_*.py)
  - **JavaScript**: Web UI (ExtJS framework)
  - **Shell Script**: Installation and service management scripts
  - **CGI**: Block page rendering

### Frameworks and Libraries
| Framework/Library | Version | Purpose | Components Using |
|-------------------|---------|---------|------------------|
| Boost C++ | 1.57.0 | System programming, networking | Core binaries |
| SQLite3 | Unknown | Database storage | Access control profiles |
| libpcap++ | Unknown | Packet capture/analysis | Network filtering |
| ExtJS/Sencha | Unknown | Web UI framework | Web interface |
| pthread | System | Multi-threading | All daemons |
| libstdc++ | GCC 10.3.0 | C++ standard library | All C++ components |

### External Dependencies
```bash
# System libraries (from ldd output)
linux-vdso.so.1
libpthread.so.0
libstdc++.so.6
libgcc_s.so.1
libc.so.6
/lib/ld-linux-aarch64.so.1

# Package-specific libraries
libsynoaccesscontrol.so.1
libsynoparentalcontrol.so.1
libsynosafebrowsing.so.1
libsynosafeaccesslog.so.1
libsynoipblock.so.1
libpcpp.so.0
```

### Databases and Storage
- **Database Type**: SQLite3
- **Location**: /var/packages/SafeAccess/var/db/
- **Schema Files**:
  - access_control_custom_profile.sql
  - access_control_interface_profile.sql
  - access_control_device.sql
  - access_control_exception.sql
  - log.sql
  - notification.sql
  - parental_control.sql
- **Data Types**: User profiles, device configurations, access rules, logs

## Core Functionality

### Primary Features
1. **Web Filtering**
   - Description: Blocks inappropriate websites based on categories
   - Implementation: DNS/HTTP filtering with category database
   - User Interface: Web UI, block pages

2. **Time Management**
   - Description: Sets internet access schedules and time quotas
   - Implementation: synotimespentd daemon tracks usage
   - User Interface: Profile-based configuration

3. **Safe Browsing**
   - Description: Protects against malicious websites
   - Implementation: safe_browsing_client with real-time checks
   - User Interface: Automatic protection, security block pages

4. **Access Control**
   - Description: Device-based internet access management
   - Implementation: MAC address tracking, profile assignment
   - User Interface: Device management interface

5. **Reward System**
   - Description: Grant additional internet time as rewards
   - Implementation: Time quota extensions
   - User Interface: Parent/admin controls

### Services and Daemons
| Service Name | Binary Path | Purpose | Auto-start |
|--------------|-------------|---------|------------|
| synosafeaccessfilterd | /volume1/@appstore/SafeAccess/bin/synosafeaccessfilterd | Main filtering daemon | Yes |
| synotimespentd | /volume1/@appstore/SafeAccess/bin/synotimespentd | Time tracking daemon | Yes |
| safe_browsing_client | /volume1/@appstore/SafeAccess/bin/safe_browsing_client | Safe browsing service | Yes |

### User Interaction Points
- **Web Interface**: http://router:8000/webman/3rdparty/SafeAccess/
- **Command Line**: 
  - `synoactool` - Access control management
  - `synopctool` - Parental control management
  - `synoipblock` - IP blocking management
- **API Endpoints**: 
  - /webapi/entry.cgi?api=SYNO.SafeAccess.*
  - Multiple API modules for different features
- **Block Pages**: 
  - http://router:5012/ (blocktime)
  - http://router:5022/ (safe-browsing)
  - http://router:5032/ (security)
  - http://router:5042/ (timequota)
  - http://router:5052/ (webfilter)

## Package Dependencies

### Software Dependencies
```
Required packages:
- SRM >= 5.2-9283
- System libraries (glibc, libstdc++)

Optional packages:
- None identified
```

### System Dependencies
- **Kernel Modules**: iptables/netfilter modules
- **System Services**: 
  - httpd (Apache web server)
  - upstart (service management)
  - syslog-ng (logging)
- **Minimum DSM/SRM Version**: 5.2-9283
- **Architecture**: cypress (ARM aarch64)

### External Service Dependencies
- **Network Services**: DNS resolution
- **Cloud Services**: Safe browsing database updates
- **License Servers**: None

## Security Analysis

### Permissions and Access Control
```bash
# File permissions
-rwx------ 1 root root synosafeaccessfilterd
-rwx------ 1 root root synotimespentd
-rwx------ 1 root root safe_browsing_client

# Process privileges
# Services run as root (from upstart configs)

# AppArmor profiles
/etc/apparmor.d/synosafeaccess-profile
- Capability: chown
- Network: raw, packet
- File access: restricted to package directories
```

### Network Security
| Port | Protocol | Purpose | Authentication | Encryption |
|------|----------|---------|----------------|------------|
| 5012 | HTTP | Block time page | None | No |
| 5013 | HTTPS | Block time page | None | Yes |
| 5022 | HTTP | Safe browsing filter | None | No |
| 5023 | HTTPS | Safe browsing filter | None | Yes |
| 5032 | HTTP | Security filter | None | No |
| 5033 | HTTPS | Security filter | None | Yes |
| 5042 | HTTP | Time quota | None | No |
| 5043 | HTTPS | Time quota | None | Yes |
| 5052 | HTTP | Web filter | None | No |
| 5053 | HTTPS | Web filter | None | Yes |

### Data Security
- **Sensitive Data Locations**:
  - /var/packages/SafeAccess/var/db/*.db - User profiles and logs - No encryption
  - /etc/security.settings - Security configuration - Plain text
- **Data Transmission**: HTTP/HTTPS for block pages
- **Storage Encryption**: None
- **Access Logging**: Comprehensive logging to SQLite databases

### Known Vulnerabilities
| CVE ID | Severity | Status | Description |
|--------|----------|--------|-------------|
| N/A | HIGH | Open | No package digital signatures |
| N/A | MEDIUM | Open | XSS vulnerabilities in block pages |
| N/A | MEDIUM | Open | Security bypass enabled by default |
| N/A | LOW | Open | Outdated Boost library (1.57.0) |

### Security Best Practices
1. **Configuration Hardening**:
   - Disable allowBypass in security.settings
   - Enable HTTPS-only for block pages
   - Implement rate limiting

2. **Access Control**:
   - Review and restrict AppArmor profiles
   - Implement least privilege for services
   - Add authentication to block pages

3. **Monitoring**:
   - Monitor /var/log/synosafeaccess.log
   - Track bypass attempts
   - Alert on service failures

### Potential Attack Vectors
- **Package Tampering**: No signature verification allows modification
- **XSS Attacks**: Unescaped user input in block pages
- **Filter Bypass**: allowBypass=yes enables circumvention
- **Service Disruption**: No rate limiting on requests

## Configuration Management

### Configuration Files
| File Path | Purpose | Format | Reload Method |
|-----------|---------|--------|---------------|
| /etc/security.settings | Security configuration | Key=Value | Service restart |
| /etc/httpd/sites-enabled/safe_access_*.conf | Apache configs | Apache format | Apache reload |
| /etc/init/synosafeaccessfilterd.conf | Upstart service | Upstart format | Service restart |

### Key Configuration Options
```
# /etc/security.settings
allowBypass=yes  # SECURITY RISK: Allows filter bypass
logLevel=info
updateInterval=3600

# Apache configurations for each service
# Define ports and SSL settings for block pages
```

### Environment Variables
| Variable | Default | Purpose | Security Impact |
|----------|---------|---------|-----------------|
| None documented | - | - | - |

## Integration with SRM System

### System Hooks
- **Installation Hooks**: 
  - preinst/postinst scripts for setup
  - Database initialization
  - Service registration
- **Startup Integration**: 
  - Upstart configuration with respawn
  - Auto-start on boot
- **Shutdown Procedures**: 
  - Graceful service stop
  - Database cleanup
- **Update Mechanisms**: 
  - Migration scripts for database updates
  - Configuration migration tools

### Interactions with Other Components
- **Firewall Integration**: iptables/ip6tables rules
- **Network Topology**: Hooks for network changes
- **Web Server**: Apache integration for block pages
- **Logging System**: syslog-ng integration
- **Package Management**: Standard Synology package framework

### Resource Sharing
- **Shared Libraries**: Uses system libraries only
- **Shared Configurations**: Apache sites-enabled
- **Shared Data**: None identified

## Performance Considerations

### Resource Usage
- **CPU**: Moderate - packet inspection and filtering
- **Memory**: ~50-100MB per daemon (estimated)
- **Disk I/O**: High - minute-level database writes (1.4M records/device/year)
- **Network**: Minimal overhead for filtering

### Scalability Limitations
- **Current Capacity**: 10-50 devices (SOHO market)
- **Architectural Limit**: ~100 devices before performance degradation
- **Primary Bottlenecks**:
  1. SQLite single-writer limitation
  2. Linear O(n) iptables rule matching
  3. Minute-level time tracking creating excessive data
  4. No caching layer for frequent queries

### Bottlenecks and Optimization
- **Database Bottleneck**: 
  - SQLite write locks with multiple daemons
  - 525,600 time tracking records per device per year
  - Solution: Migrate to PostgreSQL, aggregate data
  
- **Packet Filtering**: 
  - iptables rules scale linearly with devices
  - Solution: Use ipset for O(1) lookups, consider eBPF
  
- **Missing Abstractions**:
  - Hard-coded ports (5012-5053) and IPs
  - Direct iptables manipulation in shell scripts
  - Solution: Create abstraction layer

### Architectural Assessment
- **Strengths**: Clean layered design, proper security integration, modular components
- **Weaknesses**: Not designed for enterprise scale, brittle system integration
- **Overengineering**: 20+ language-specific databases for simple keyword matching
- **Technical Debt**: 500+ lines of shell scripts with hard-coded values

## Operational Notes

### Logging
| Log File | Purpose | Rotation | Important Entries |
|----------|---------|----------|-------------------|
| /var/log/synosafeaccess.log | Main service log | logrotate | Service start/stop, errors |
| /var/packages/SafeAccess/var/db/log.db | Access logs | Manual | Blocked attempts, bypasses |

### Maintenance Tasks
- **Regular Tasks**: 
  - Database cleanup (old logs)
  - Safe browsing database updates
- **Cleanup**: 
  - Temporary block page files
  - Old log entries
- **Backup**: 
  - User profiles and settings
  - Access control rules

### Troubleshooting
| Issue | Symptoms | Solution |
|-------|----------|----------|
| Service won't start | No filtering active | Check logs, verify database integrity |
| False positives | Sites incorrectly blocked | Review category settings, add exceptions |
| Time tracking issues | Incorrect time quotas | Restart synotimespentd, check NTP |

### Useful Commands
```bash
# Check package status
synopkg status SafeAccess

# View service logs
tail -f /var/log/synosafeaccess.log

# Restart package services
synopkg restart SafeAccess

# Verify database integrity
sqlite3 /var/packages/SafeAccess/var/db/access_control.db "PRAGMA integrity_check;"
```

## Legal and Compliance

### License Terms
Proprietary Synology software - usage restricted to Synology hardware

### Export Restrictions
Contains cryptographic components (HTTPS support)

### Privacy Considerations
- Logs user browsing attempts
- Stores device MAC addresses
- Tracks time spent online per device
- No apparent data transmission to Synology

## Cross-References
- Related packages: None identified
- System components: 
  - [/etc - System Configuration](../../structure/etc.md)
  - [/var - Variable Data](../../structure/var.md)
- Security reports: See Security Analysis section
- Configuration guides: [Configuration Management Guide](../../configuration_management_guide.md)

## Version History
| Version | Date | Changes | Security Updates |
|---------|------|---------|------------------|
| 1.3.1-0326 | 2022-05-17 | Current version | Unknown |

## Strategic Analysis Summary

### Executive Overview
Safe Access is a well-engineered parental control solution for the SOHO market (10-50 devices) with solid architecture for its intended use case. However, fundamental scalability limitations prevent enterprise deployment without major architectural changes.

### Critical Findings (Immediate Action Required)

1. **No Package Signatures** (CRITICAL)
   - Impact: Package integrity cannot be verified, vulnerable to supply chain attacks
   - Solution: Implement .spk package signing immediately

2. **Database Scalability Wall** (CRITICAL)  
   - Impact: SQLite single-writer blocks at 100+ devices
   - Evidence: All daemons compete for database writes
   - Solution: Migrate to PostgreSQL for concurrent operations

3. **Security Bypass Enabled** (HIGH)
   - Impact: Users can circumvent all filtering with allowBypass=yes
   - Solution: Change default to "no" in security.settings

### Architectural Recommendations

#### Quick Wins (1 month)
1. Disable bypass by default
2. Fix XSS vulnerabilities in block pages
3. Batch time tracking writes (5-15 minute intervals)
4. Implement basic monitoring metrics

#### Phase 1: Stabilize (3 months)
1. Add ipset for O(1) packet filtering
2. Create abstraction layer for system integration
3. Implement structured logging
4. Document all hardcoded values

#### Phase 2: Scale (6 months)  
1. Migrate to PostgreSQL
2. Add Redis caching layer
3. Replace minute tracking with smart aggregation
4. Implement connection pooling

#### Phase 3: Modernize (12 months)
1. Microservices architecture
2. Message queue integration
3. eBPF for packet filtering
4. Horizontal scaling support

### Business Impact
- **Current**: 10-50 devices (home users)
- **Potential**: 100-1000+ devices (enterprise)
- **Investment**: 6-12 months engineering
- **Alternative**: License enterprise solution if time-critical

## Analysis Metadata
- **Analysis Date**: 2025-06-24
- **Analyzed By**: SRM Documentation Team with Zen MCP Analysis
- **SRM Version**: 5.2-9346
- **Tools Used**: Zen MCP with Gemini Pro, file analysis, strings, security audit, architectural analysis
- **Limitations**: 
  - Binary analysis limited to strings output
  - No runtime analysis performed
  - Some internal APIs undocumented
  - Performance metrics estimated based on architecture

---

[← Back to Package Index](../index.md) | [← Previous Package](previous-package.md) | [→ Next Package](next-package.md)

---
*This documentation was created as part of the comprehensive Synology SRM system analysis project.*