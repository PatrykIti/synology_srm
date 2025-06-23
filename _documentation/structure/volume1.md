# /volume1 Directory - Primary Data Storage Volume

## Overview
The `/volume1` directory is the primary data storage volume on Synology SRM devices. It serves as the root for user-installed applications, system-wide databases, and temporary files. Its modular structure, centered around the `@appstore` and `@db` directories, allows for package-based functionality, but its operational characteristics present significant scalability and maintenance considerations.

## Directory Structure
```
/volume1/
├── @appstore/                       # Installed package applications
│   ├── SafeAccess/                  # Parental control & web filtering
│   │   ├── app/                     # Application binaries
│   │   ├── conf/                    # Configuration files
│   │   ├── etc/                     # Service configurations
│   │   │   ├── apparmor/           # Security profiles
│   │   │   └── httpd/              # Block page web servers
│   │   ├── lib/                     # Shared libraries
│   │   ├── scripts/                 # Management scripts
│   │   │   ├── dnsfilter-iptables.sh
│   │   │   └── start-service.sh
│   │   ├── ui/                      # Web interface files
│   │   ├── upstart/                 # Service definitions
│   │   ├── var/                     # Variable data
│   │   │   ├── db/                  # Databases
│   │   │   │   ├── access_log.sqlite
│   │   │   │   └── safe_access.db
│   │   │   └── xapian/              # Search indexes (20+ languages)
│   │   └── webapi/                  # API definitions
│   └── Traffic/                     # Network monitoring package
│       ├── app/                     # Application files
│       ├── conf/                    # Configuration
│       ├── lib/                     # Libraries
│       ├── scripts/                 # Management scripts
│       ├── ui/                      # Web interface
│       └── var/
│           └── db/
│               └── traffic.sqlite   # Traffic metrics database
├── @db/                            # System-wide databases
│   └── var/db/
│       ├── syno-domain-lists/
│       │   └── domain_category_db.sqlite  # 114MB+ domain categorization
│       ├── syno-doh-server-lists/
│       │   └── server_lists.db            # DNS-over-HTTPS blocklist
│       ├── syno-geoip/
│       │   ├── GeoLite2-City.mmdb        # GeoIP city database
│       │   └── GeoLite2-Country.mmdb     # GeoIP country database
│       ├── syno-ip-blocklist/
│       │   ├── blocklist                  # IP blocklist (Git conflicts found)
│       │   ├── blocklist_enable_map
│       │   ├── firehol_level1.netset     # FireHOL threat intelligence
│       │   └── firehol_level2.netset
│       ├── syno-device-identity-database/
│       │   └── dhcpFingerPrints          # Device fingerprinting
│       └── syno-safebrowsing/
│           └── goog_*                     # Google Safe Browsing data
├── @tmp/                           # Temporary package data
│   ├── pkglist.tmp/               # Package lists (multi-language)
│   └── pkgicon/                   # Package icons
└── lost+found/                    # ext4 filesystem recovery

Note: srm-backup-fixed.tar.gz excluded as temporary backup file
```

## Key Components

### Application Package: SafeAccess
- **Purpose**: Provides parental control, web filtering, and security threat mitigation
- **Location**: `/volume1/@appstore/SafeAccess/`
- **Dependencies**: 
  - Local SQLite databases (`safe_access.db`, `access_log.sqlite`)
  - Shell scripts interpret database entries to modify `iptables` ruleset
  - System-wide databases in `/volume1/@db/` (domain categorization, GeoIP)
- **Configuration**: Managed via local SQLite databases and configuration files within `conf/` and `var/` directories
- **Security**: Leverages AppArmor profiles for process sandboxing. Interacts directly with kernel's `iptables` netfilter framework

### Application Package: Traffic
- **Purpose**: Network traffic monitoring, analysis, and reporting on per-device and per-application basis
- **Location**: `/volume1/@appstore/Traffic/`
- **Dependencies**: Relies on data collected from kernel's networking stack
- **Configuration**: Primary data store is `traffic.sqlite` with highly granular metrics
- **Security**: Operates as data collection and reporting tool with no direct policy enforcement

### System Databases (@db)
- **Purpose**: Centralized databases providing threat intelligence and categorization data
- **Location**: `/volume1/@db/`
- **Dependencies**: Critical dependencies for IP-based, GeoIP, or domain-based filtering
- **Configuration**: Typically read-only data sources updated by system processes
- **Security**: Integrity critical for system security functions

## Configuration Files

### SafeAccess Configuration
- **access_control.conf**: Device and profile management
- **safe_access.sc**: Service configuration
- **schema.sql**: Database schema definitions
- **Multiple HTTP configurations**: For block page services (webfilter.httpd.conf, security.httpd.conf, etc.)

### System Blocklists
- **blocklist**: Plaintext, newline-delimited IP addresses for system-wide blocking
  - Analyzed file contained Git merge conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`)
  - These non-IP strings will cause parsing errors in scripts expecting clean IP lists
- **blocklist_enable_map**: Controls which blocklists are active
- **FireHOL netsets**: Level 1 & 2 threat intelligence feeds

### Domain Categorization
- **domain_category_db.sqlite**: 114MB+ SQLite database
  - Contains 116,359 categorized web pages
  - Used for content filtering decisions
  - WAL mode enabled for performance

## Scripts and Executables

### SafeAccess Scripts
- **dnsfilter-iptables.sh**: Translation layer reading policy configurations from databases and converting to `iptables` commands
  - Creates necessary chains and rules for DNS/web filtering
  - Direct manipulation creates tight coupling with kernel networking stack
- **start-service.sh**: Initializes SafeAccess services and block page servers
- **stop-service.sh**: Cleanup script for service shutdown

### Traffic Scripts
- **start-stop-status**: Standard Synology package management script
- **Database maintenance scripts**: For traffic data collection

## Integration Points

### SafeAccess & iptables
- Integrates directly with Linux kernel's netfilter subsystem
- Scripts dynamically generate and apply `iptables` rules
- Virtual IPs (10.254.x.x, fc00:eeee:x::x) used for redirection

### Packages & System DBs
- Packages perform lookups against central databases in `/volume1/@db`
- Domain categorization enriches filtering decisions
- GeoIP databases enable location-based filtering

### WebAPI Architecture
- `.lib`/`.so` pairs enable modular service exposure
- RESTful APIs for UI and external integration
- Authentication handled by SRM framework

## Security Considerations

### Defense in Depth Architecture
- Multiple filtering layers: application-level (SafeAccess) + network-level (`iptables`)
- Large externally-sourced databases (GeoIP, domain categories)
- AppArmor profiles for process isolation
- Integrity of databases and scripts critical to system function

### Security Architecture Characteristics
- Script-based `iptables` manipulation creates tight coupling
- No apparent rate limiting on block page access (ports 5012-5053)
- Multiple exposed HTTP services increase attack surface
- Direct firewall manipulation requires elevated privileges

## Network Services

### SafeAccess Block Pages
Multiple HTTP services on high ports serve different block pages:
- Port 5012: Web filter blocks
- Port 5013: Security threat blocks
- Port 5014: Time quota exceeded
- Ports 5015-5053: Various other block types
- `iptables` rules redirect offending traffic to appropriate port

### API Services
- WebAPI endpoints for configuration management
- Real-time traffic monitoring APIs
- Device management interfaces

## Maintenance Notes

### Critical: Unbounded Data Growth
- `Traffic` package's `traffic.sqlite` database collects per-minute metrics
- `SafeAccess` `access_log.sqlite` stores high-granularity access logs
- No native data lifecycle management (aggregation, rotation, purging)
- Continuous operation leads to unbounded file growth
- Manual monitoring of `/volume1` disk usage required to prevent:
  - Storage exhaustion
  - Performance degradation
  - Service failures

### Configuration Brittleness
- Network policy enforcement is not atomic
- Shell scripts apply rules sequentially
- Failure during execution (e.g., malformed configuration) leaves firewall inconsistent
- No transactional rollback mechanism for configuration application
- Example: Git conflict markers in production blocklist file

### Package Management
- Packages installed in self-contained directories
- Version-specific patch scripts indicate upgrade complexity
- Mixed configuration formats (SQL, JSON, custom text)
- Dependencies between packages not formally declared

## Platform-Specific Features

### RT6600ax Implementation
- Optimized for ARM64 architecture
- Supports concurrent multi-CPU packet processing
- Hardware acceleration integration points
- Memory constraints influence database sizing

### Synology Package Architecture
- Standard `@appstore` naming convention
- Upstart service integration
- DSM/SRM UI framework compatibility
- Package signing and verification

## Technical Details

### SQLite Performance Characteristics
- Databases operate in Write-Ahead Logging (WAL) mode
- Default checkpoint at 1000 pages (~4MB with 4KB pages)
- On resource-constrained device under heavy logging:
  - WAL file grows significantly between checkpoints
  - Temporary disk usage spikes
  - Checkpoint process impacts system responsiveness

### Xapian Search Indexes
- 20+ language indexes (3.4MB total) for content searching
- Loaded in memory for performance
- Used by SafeAccess for multi-language filtering

### Data Retention Architecture
- Per-minute granularity for traffic monitoring
- No built-in aggregation mechanism
- SQLite file size limited only by filesystem
- Manual intervention required for data management

## Cross-References
- Package management: [/etc/packages/](etc.md#package-management)
- Service definitions: [/etc/init/](etc.md#upstart-services)
- iptables integration: [/etc/firewall/](etc.md#firewall-configuration)
- System logs: [/var/log/](var.md#application-logs)
- Kernel modules: [/lib/modules/](lib.md#network-modules)

## Version Information
- **Document Version**: 2.0
- **Last Updated**: 2025-06-23
- **System**: Synology RT6600ax
- **Firmware**: SRM 5.2-9346
- **Analysis**: Complete volume analysis with operational characteristics

---
*This documentation was created as part of the comprehensive Synology SRM system analysis project.*