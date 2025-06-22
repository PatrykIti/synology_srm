# /var.defaults Directory - Variable Data Templates

## Overview
The `/var.defaults` directory serves as a factory reset template for the `/var` directory structure in Synology SRM. It contains pristine default versions of directories and files that initialize the system's variable data storage. This separation between immutable defaults and mutable runtime data enhances system reliability and enables clean factory resets.

## Directory Structure
```
/var.defaults/
├── cache/                     [Application cache templates]
│   ├── data_update/          [System update cache structure]
│   └── samba/                [SMB/CIFS cache structure]
├── dynlib/                    [Dynamic libraries and security rules]
│   └── securityscan/         [Complete security scanning framework]
│       ├── INFO              [Security scan metadata]
│       ├── ruleDB/           [Security rule database - 99 files]
│       │   ├── DBList.json   [Rule database manifest]
│       │   ├── DBVersion.json [Rule version tracking]
│       │   ├── security_scan.so [Core scanning engine]
│       │   └── [Categories]/ [Python security rules by domain]
│       └── texts/            [21 language translations]
├── empty/                     [Empty directory for chroot/privilege separation]
├── lib/                       [Variable state templates]
│   ├── dpkg/                 [Package management templates]
│   │   ├── available         [Empty template]
│   │   ├── status            [Empty template]
│   │   ├── info/             [Package info directory]
│   │   └── parts/            [Partial package directory]
│   └── [other services]/     [Service state templates]
├── lock -> ../run/lock        [Runtime lock files symlink]
├── log/                       [Log directory structure]
│   ├── httpd/                [Web server logs - empty]
│   ├── samba/                [File sharing logs - empty]
│   └── upstart/              [Service logs - empty]
├── packages/                  [Package data directory - empty]
├── run -> ../run              [Runtime data symlink]
├── services/                  [Service-specific data]
│   └── tmp/                  [Service temporary files]
├── spool/                     [Spool directories - empty]
└── tmp/                       [Temporary files - empty]
```

## Key Components

### Security Scanning Framework (/dynlib/securityscan)
- **Purpose**: Comprehensive security assessment system
- **Components**:
  - Python-based modular rule engine
  - 99 security rule files organized by category
  - Multi-language support (21 languages)
  - Compiled scanning engine (security_scan.so)
- **Categories**:
  - DirectoryService: Domain/LDAP security checks
  - FileService: FTP/SMB/WebDAV security
  - Malware: Binary/profile/self-check rules
  - Network: DSM network settings security
  - Security: Firewall/AutoBlock/CSRF checks
  - Terminal: SSH/Telnet/SNMP security
  - Update: System/package update checks
  - User: Guest/password policy enforcement
- **Security**: Password dictionary (pwd.list.gz) for strength validation

### Package Management Templates (/lib/dpkg)
- **Purpose**: Debian package system initialization
- **Structure**:
  - Empty `status` file - populated during runtime
  - Empty `available` file - filled with package data
  - `info/` directory for package metadata
  - `parts/` directory for partial downloads
- **Integration**: Foundation for tracking 172+ system packages

### Directory Structure Templates
- **Purpose**: Ensure correct filesystem hierarchy
- **Key Directories**:
  - `/cache` - Application cache structures
  - `/log` - Logging directory hierarchy
  - `/spool` - Job queue directories
  - `/packages` - Package installation data
  - `/services` - Service runtime data
- **Configuration**: All directories have 700 permissions

### Symbolic Links
- **Purpose**: Connect to volatile runtime directories
- **Links**:
  - `lock` → `../run/lock` (lock files)
  - `run` → `../run` (runtime data)
- **Security**: Maintains FHS compliance

## Configuration Files

### Security Rule Configuration
- **DBList.json**: Manifest of security rules
- **DBVersion.json**: Version tracking for rule updates
- **Rule Format**: Python scripts with standardized classes
- **Localization**: String files for each language

### Package Templates
- **dpkg/status**: Empty template for package states
- **dpkg/available**: Empty template for package list
- **Purpose**: Clean slate for package management

## Scripts and Executables

### Security Scanning Engine
- **security_scan.so**: Compiled scanning core
- **Python Rules**: Individual check scripts
  - Each implements standardized rule interface
  - Returns pass/fail with remediation info
  - Integrates with WebAPI for fixes

### Rule Examples
- `check_password_strength_rule_home.py`
- `autoBlockEnableCheck.py`
- `httpsEnableCheck.py`
- `telnetEnableCheck.py`

## Integration Points

### System Initialization
1. **First Boot**: Contents copied to `/var`
2. **Factory Reset**: `/var` restored from defaults
3. **Recovery**: Missing structures recreated
4. **Updates**: New defaults may be added

### Service Integration
- Security scanner uses rules at runtime
- Package manager initializes from templates
- Log rotation expects directory structure
- Services create runtime data in provided dirs

### Synology Customizations
- Security scanning framework unique to Synology
- Package naming scheme (*-cypress-bin)
- Multi-language support for all regions
- Integration with SRM/DSM management

## Security Considerations

### Strengths
1. **Immutable Defaults**: Cannot be corrupted by runtime
2. **Clean Recovery**: Factory reset always possible
3. **Permission Model**: Restrictive 700 permissions
4. **Comprehensive Rules**: 99 security checks included

### Design Benefits
1. **Separation of Concerns**: Runtime vs defaults
2. **Resilience**: System can self-heal
3. **Auditability**: Easy to verify defaults
4. **Upgradability**: New defaults in updates

## Network Services
- No active network services in defaults
- Templates ready for service activation
- Security rules check network configurations

## Maintenance Notes

### Usage Patterns
1. **System Install**: Initial population of `/var`
2. **Factory Reset**: Complete restoration
3. **Partial Recovery**: Recreate missing dirs
4. **Update Process**: May add new defaults

### Comparison with /var
| Aspect | /var.defaults | /var |
|--------|---------------|------|
| Files | 101 | 397 |
| Size | ~5MB | ~50MB |
| Logs | Empty dirs | Active logs |
| Packages | Empty | SafeAccess installed |
| dpkg | Templates | 172+ packages tracked |
| State | Immutable | Constantly changing |

### Best Practices
1. **Never Modify**: Keep defaults pristine
2. **Regular Checks**: Verify structure integrity
3. **Update Awareness**: New defaults in firmware
4. **Recovery Testing**: Validate reset procedures

## Synology-Specific Features

### Platform Integration
- **Architecture**: Cypress (RT6600ax specific)
- **Firmware**: Version 5.2-9346 base
- **Kernel**: References for 4.4.60
- **Services**: SRM-specific daemons

### Custom Components
1. **Security Scanner**: Unique to Synology
2. **Package Format**: Modified Debian system
3. **Service Names**: syno* prefixed services
4. **Mesh Support**: Router-specific features

### Factory Reset Mechanism
1. User initiates factory reset
2. System stops all services
3. `/var` contents cleared
4. `/var.defaults` copied to `/var`
5. Services restart with clean state
6. User data preserved on `/volume1`