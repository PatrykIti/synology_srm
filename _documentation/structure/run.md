# /run Directory - Runtime Data

[← Back to Documentation Index](../README.md) | [← Previous: /root](root.md) | [→ Next: /sbin](sbin.md)

---
---

## Overview
The `/run` directory is a standard location for storing volatile runtime data in the Synology SRM system. As a tmpfs (temporary filesystem) mount residing in RAM, it provides fast access to process IDs, lock files, sockets, and service state information that are cleared upon system restart. In the RT6600ax router, this directory orchestrates the runtime coordination of 28+ system services and manages critical inter-process communication.

## Directory Structure
```
/run/
├── *.pid files            # 28 process ID files
├── *.lock files           # 4 main lock files
├── avahi-daemon/          # mDNS service discovery
├── data_update/           # Database update coordination
│   └── [7 lock files]     # Update synchronization
├── ddns/                  # Dynamic DNS results
├── httpd/                 # Web server runtime
├── ipset/                 # Firewall IP sets
│   └── [11 IP sets]       # Policy-based firewall rules
├── lock/                  # System-wide locks
│   └── [15 lock files]    # Service synchronization
├── ngfw/                  # Next-Gen Firewall state
│   └── lock/              # QoS configuration locks
├── ntp/                   # Time synchronization
├── samba/                 # SMB/CIFS state
│   └── [5 TDB files]      # Samba databases
├── sudo/                  # Sudo timestamp directory
├── synodevice/            # Device management
│   └── lock/              # Device DB locks
├── synoservice/           # Service management
│   ├── bootup-fail-job/   # Failed service tracking
│   └── service/           # Service configurations
├── udev/                  # Device manager state
│   └── data/              # Hardware enumeration
└── [various state files]  # Runtime configuration
```

## Key Components

### Process ID (PID) Files
- **Purpose**: Track running daemon process IDs for service management
- **Count**: 28 PID files identified
- **Format**: Single line with process ID, newline terminated
- **Location**: Root of /run and service-specific subdirectories
- **Security**: Enable proper signal handling and prevent duplicate instances

#### Service Categories
| Category | Services | Count |
|----------|----------|-------|
| System Core | crond, syslog-ng, rngd, logrotated | 7 |
| Network Services | sshd, dnsmasq, ntpd, miniupnpd | 8 |
| Synology Services | synodevicecored, synonetd, synoconfd | 11 |
| Third-party | samba/nmbd, httpd, snmpd | 3 |

### Lock Files and Synchronization
- **Purpose**: Prevent race conditions and ensure exclusive resource access
- **Total Count**: 28 lock files across all directories
- **Implementation**: Empty files (0 bytes) using file existence for locking
- **Permissions**: 700 (rwx------) for security

#### Lock Categories
| Location | Purpose | Count |
|----------|---------|-------|
| /run/ | Main service locks | 4 |
| /run/lock/ | System-wide synchronization | 15 |
| /run/data_update/ | Database update coordination | 7 |
| /run/synodevice/lock/ | Device management | 5 |
| /run/ngfw/lock/ | Firewall configuration | 1 |

### Service-Specific Directories

#### synoservice/ - Service Management
- **bootup_time**: Total boot time 177.55 seconds
- **bootup_time_detail**: Detailed boot stage timing
- **bootup-fail-job/**: Tracks failed services (dhcp-client, ipsec, synoneteventd_reinit)
- **service/**: Runtime service configurations

#### synodevice/ - Device Discovery
- **avahi_response**: mDNS/Bonjour device responses
- **mdns_cache**: Cached service discovery data
- **Device tracking**: MAC addresses, vendor mapping
- **Integration**: DHCP fingerprinting for device identification

#### ipset/ - Firewall IP Sets
Dynamic firewall rule management:
- **FIREWALL_LAN_V4/V6**: LAN-specific rules
- **POLICY_ALLOW_ACCESS_SRM_V4/V6**: SRM access control
- **POLICY_ISOLATION_LAN_V4/V6**: Network isolation
- **POLICY_DISABLE_NAT_LAN**: NAT bypass list
- **POLICY_PRIVATE_ADDRESS_V4**: RFC1918 addresses

#### udev/data/ - Hardware Enumeration
- **Device count**: 400+ hardware devices tracked
- **Platform**: Cypress (Qualcomm IPQ6018)
- **Components**: CPUs, network interfaces, USB, GPIO, thermal zones
- **Modules**: Kernel modules loaded (WiFi, crypto, networking)

## Runtime Files and State

### Network State Files
| File | Purpose | Content Type |
|------|---------|--------------|
| access_srm_rules_v4/v6 | Firewall access rules | iptables rules |
| isolate_rules_v4/v6 | Network isolation rules | iptables rules |
| nat_rules | NAT configuration | iptables NAT |
| device.dhcp | DHCP lease information | Text |
| topology_state | Network topology | JSON-like |
| pmk.txt/ptk.txt | WiFi security keys | Temporary keys |

### Boot State Tracking
```
Boot Timeline:
- rootfs_ready: 76.78s
- runlevel1: 125.99s
- network_ready: 134.49s
- service_ready: 171.60s
- package_ready: 177.24s
```

### Interface Timing
- **Purpose**: Track interface state changes with microsecond precision
- **Files**: interface_up_down_time_record_*
- **Interfaces**: ppp100 (PPP), usbnet0 (USB networking)
- **Format**: Microsecond timestamps

## Integration Points

### Service Startup
- **Init System**: Upstart (not systemd)
- **Dependencies**: Clear service dependency chains
- **Respawn**: Automatic restart with limits (5 times in 10 seconds)
- **Logging**: Console output and syslog-ng integration

### Inter-Process Communication
- **PID Files**: Enable signaling (SIGHUP, SIGTERM)
- **Lock Files**: Coordinate resource access
- **Sockets**: Unix domain sockets for IPC (not visible in backup)
- **Shared Memory**: Via /dev/shm (separate from /run)

### Hardware Integration
- **udev**: Device detection and enumeration
- **hotplugd**: Dynamic device addition/removal
- **GPIO/LED**: Hardware control interfaces
- **Thermal**: Temperature monitoring zones

## Security Considerations

### Access Control
- **Directory**: 755 permissions on /run
- **PID Files**: 644 or 600 permissions
- **Lock Files**: 700 permissions (exclusive access)
- **Service Isolation**: Per-service subdirectories

### Sensitive Data
- **WiFi Keys**: Temporary PMK/PTK in plaintext
- **Service Credentials**: Not stored in /run
- **Firewall Rules**: Dynamic rule sets visible
- **Device Information**: MAC addresses and fingerprints

### Security Features
1. **Process Tracking**: Prevents service duplication
2. **Lock Mechanisms**: Prevents race conditions
3. **Failed Service Tracking**: Boot failure detection
4. **Timestamp Recording**: Audit trail capability

## Network Services

### Active Services
| Service | Port | Protocol | Purpose |
|---------|------|----------|---------|
| SSH | 22 | TCP | Remote administration |
| DNS/DHCP | 53/67 | UDP | Network services |
| HTTP | 80 | TCP | Web interface |
| HTTPS | 443 | TCP | Secure web interface |
| NTP | 123 | UDP | Time synchronization |
| SNMP | 161 | UDP | Network monitoring |
| SMB | 445 | TCP | File sharing |
| UPnP | 1900 | UDP | Service discovery |

### Service Coordination
- **miniupnpd/minissdpd**: UPnP/SSDP services
- **avahi-daemon**: mDNS/Bonjour broadcasting
- **dnsmasq**: Integrated DNS/DHCP server
- **ngfw**: Next-Generation Firewall with QoS

## Performance Considerations

### tmpfs Characteristics
- **Storage**: RAM-based filesystem
- **Speed**: No disk I/O latency
- **Volatility**: Cleared on reboot
- **Size**: Limited by available RAM

### Resource Usage
- **PID Files**: Minimal (few bytes each)
- **Lock Files**: Zero bytes (existence-based)
- **State Files**: Variable, typically small
- **udev Data**: Largest consumer (~1MB)

## Maintenance Notes

### Runtime State in Backups
- **Snapshot Nature**: Point-in-time capture
- **Incompleteness**: Active changes during backup
- **Restoration**: Not directly restorable
- **Analysis Value**: System state forensics

### Service Management
```bash
# Check service status via PID
kill -0 $(cat /run/sshd.pid)

# Reload service configuration
kill -HUP $(cat /run/dnsmasq.pid)

# Stop service gracefully
kill -TERM $(cat /run/crond.pid)
```

### Lock File Handling
- **Creation**: Touch or open with O_CREAT|O_EXCL
- **Removal**: Unlink after operation
- **Stale Locks**: Check process existence
- **Timeout**: Implement lock timeouts

## Platform-Specific Features

### RT6600ax Specifics
- **Hardware**: Qualcomm IPQ6018 (4-core ARM)
- **Kernel**: Linux 4.4.60
- **Init**: Upstart (Ubuntu-style)
- **Architecture**: ARM aarch64

### Synology Customizations
1. **Service Prefix**: syno* for custom services
2. **Device Management**: Proprietary synodevice system
3. **Boot Tracking**: Detailed timing analysis
4. **Failed Job Tracking**: Boot failure recovery

## Best Practices

### For Developers
1. Always use PID files for daemons
2. Implement proper lock file handling
3. Clean up runtime files on exit
4. Use service-specific subdirectories

### For Administrators
1. Monitor failed service jobs
2. Check lock files for stale entries
3. Review boot timing for issues
4. Verify service dependencies

## Cross-References
- Service configurations: [/etc/init/](etc.md#init-scripts)
- Variable data: [/var/run/](var.md#run-symlink)
- System binaries: [/sbin/](sbin.md)
- Lock mechanisms: [/var/lock/](var.md#lock)

## Version Information
- **Document Version**: 2.0
- **Last Updated**: 2025-06-23
- **System**: Synology RT6600ax
- **Firmware**: SRM 5.2-9346
- **Analysis**: Complete runtime state analysis

---

[← Back to Documentation Index](../README.md) | [← Previous: /root](root.md) | [→ Next: /sbin](sbin.md)

---
*This documentation was created as part of the comprehensive Synology SRM system analysis project.*
