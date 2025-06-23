# Synology SRM: System Architecture & Component Relationships

This document provides a detailed overview of the Synology Router Manager (SRM) operating system architecture. It is based on an analysis of the system's file structure, service inventory, and operational behavior.

## 1. System Architecture Overview

SRM employs a layered architecture, which is typical for modern embedded Linux systems. This design separates hardware abstraction from user-facing applications, promoting modularity and security.

The 6-layer stack can be visualized as follows:

```text
     ┌──────────────────────────────────────────────────┐
     │                     UI Layer                     │  <-- User Interaction
     │ (Web UI: ExtJS Frontend, Nginx, Backend CGIs)    │
     ├──────────────────────────────────────────────────┤
     │                 Application Layer                │  <-- User-Installable Features
     │   (@appstore Packages: VPN Plus, Threat Prev.)   │
     ├──────────────────────────────────────────────────┤
     │                   Service Layer                  │  <-- System & Network Services
     │ (Upstart, synoservice, httpd, dnsmasq, smbd)     │
     ├──────────────────────────────────────────────────┤
     │                    System Layer                  │  <-- Core Userland & Libraries
     │   (/bin, /sbin, /lib*, busybox, glibc, udevd)     │
     ├──────────────────────────────────────────────────┤
     │                    Kernel Layer                  │  <-- OS Core & Drivers
     │ (Linux Kernel, Netfilter, br_netfilter, Drivers) │
     ├──────────────────────────────────────────────────┤
     │                   Hardware Layer                 │  <-- Physical Components
     │    (ARM SoC, RAM, Flash, WiFi/Ethernet Chips)    │
     └──────────────────────────────────────────────────┘
```

*   **Hardware Layer:** The physical foundation, including the ARM-based System-on-a-Chip (SoC), RAM, NAND flash storage, and dedicated chipsets for Ethernet switching and Wi-Fi.
*   **Kernel Layer:** A customized Linux kernel. Its most critical role in a router is networking. This layer includes the `netfilter` framework (which powers `iptables`), network device drivers, and filesystem drivers (e.g., `ext4`, `btrfs`).
*   **System Layer:** The core Linux userland. It contains fundamental binaries (`/bin`, `/sbin`), shared libraries (`/lib`), and low-level system daemons. `busybox` is heavily used to provide many standard utilities in a single binary.
*   **Service Layer:** This is where Synology's management framework lives. `Upstart` is the underlying init system, but most services are controlled via the `synoservice` wrapper. This layer runs essential network daemons like `dnsmasq` (DNS/DHCP), `httpd` (web server), and `sshd`.
*   **Application Layer:** Optional, feature-enhancing packages installed from the `@appstore`. These packages integrate with the Service and UI layers to provide functionality like VPN services, intrusion prevention, and content filtering.
*   **UI Layer:** The user-facing web interface. It consists of a frontend (typically a complex JavaScript application using frameworks like ExtJS) that communicates with backend CGI programs or APIs served by the `httpd` daemon.

## 2. Service Dependency Chains

Service startup is not monolithic; it follows specific dependency chains orchestrated by `Upstart` and `synoservice`. A failure in an early chain can have cascading effects.

### Core Networking & UI Chain
This is the most critical path to bring the router to a basic operational state.

```text
[syslog-ng] --> [syno-net-setting] --> [iptables] --> [dnsmasq] --> [httpd]
     |                 |                  |             |             |
  (Start          (Configure         (Apply        (Start        (Start
   Logging)         Interfaces)        Firewall)      DNS/DHCP)      Web UI)
```
*   **Rationale:** Logging must start first. Network interfaces (`br0`, `eth0`) are then configured. The firewall must be active *before* services are exposed. `dnsmasq` is started to serve the LAN, and finally, the `httpd` web server is started to provide UI access.

### Wi-Fi Service Chain
The Wi-Fi subsystem depends on the core network bridge being available.

```text
[syno-net-setting] --> [syno-wifi-loader] --> [hostapd] --> [Attach to Bridge]
     |                        |                  |                  |
  (br0 is up)           (Load Wi-Fi          (Start AP          (e.g., brctl
                         module/config)        Daemon)            addif br0 wlan0)
```

### VPN Service Chain (Example: VPN Plus Server)
VPN services depend on the firewall and core networking being fully established.

```text
[iptables] --> [synovpn-load-config] --> [openvpn-server] --> [syno-iptables-update]
     |                  |                      |                      |
  (Base FW         (Read VPN user         (Start VPN             (Add VPN-specific
   is ready)         and server conf)      process)               NAT/Firewall rules)
```

### Security Services Chain
Security services form a critical defense layer that depends on base networking.

```text
[iptables] --> [SafeAccess-DB] --> [Suricata IDS/IPS] --> [syno-threat-intel-update]
     |              |                    |                        |
  (Firewall    (Load domain         (Start deep            (Update threat
   ready)       categories)          packet inspection)      intelligence feeds)
```

## 3. Data Flow Diagrams

### Configuration Flow
This flow is central to SRM's architecture and a source of its complexity. A user change in the UI propagates through multiple layers to the running service.

```text
[UI Change] -> [Web API] -> [synoconf lib] -> [SQLite DB] -> [synoservice] -> [Template] -> [Config File] -> [Service]
    (1)           (2)           (3)             (4)             (5)           (6)           (7)             (8)
```
1.  **User Action:** Admin changes a setting in the web UI (e.g., changes a DHCP reservation).
2.  **Web API:** The browser sends the change to a backend CGI/API endpoint.
3.  **synoconf:** The backend logic uses a library (e.g., `libsynoconf.so`) to write the new value.
4.  **SQLite DB:** The setting is saved to the central configuration database (e.g., `/etc/synoinfo.conf` or a similar DB file).
5.  **synoservice:** The backend triggers `synoservice --restart <servicename>`.
6.  **Template:** The `synoservice` script reads a configuration template (e.g., from `/usr/syno/etc.defaults/`).
7.  **Config File:** The script populates the template with values from the SQLite DB and writes the final config file (e.g., `/etc/dnsmasq.conf`).
8.  **Service:** The service (`dnsmasq`) is restarted and reads its updated configuration file.

### Network Packet Flow (WAN to LAN)
A simplified view of how an incoming packet is processed.

```text
[Internet] <> [ethX (WAN)] -> [iptables:PREROUTING] -> [Routing Decision] -> [iptables:FORWARD] -> [iptables:POSTROUTING] -> [br0 (LAN)] <> [LAN Client]
                                (DNAT)                                       (Firewall Rules)       (SNAT/Masquerade)
```

### System Logging Flow
Most services do not write to log files directly. They write to `stdout`/`stderr` or send to syslog, which is then managed centrally.

```text
┌───────────┐      ┌───────────┐      ┌──────────────┐      ┌───────────────────┐
│ Service A │─────▶│           │      │              │      │ /var/log/messages │
├───────────┤      │           │      │              ├─────▶├───────────────────┤
│ Service B │─────▶│ syslog-ng │─────▶│ Filter Rules │      │ /var/log/synopkg.log │
├───────────┤      │           │      │              ├─────▶├───────────────────┤
│ Kernel    │─────▶│           │      │              │      │ ... (other files) │
└───────────┘      └───────────┘      └──────────────┘      └───────────────────┘
```

### Security Data Flow
Security-related data flows through multiple layers for threat detection and mitigation.

```text
[Network Traffic] -> [Netfilter] -> [Suricata IDS] -> [Threat Detection] -> [SafeAccess Actions]
                         |               |                   |                      |
                    (Packet         (Deep packet       (Match against         (Block/Alert/
                     filtering)      inspection)        threat intel)          Update firewall)
```

## 4. Component Relationships

### Directory Dependencies
*   **`/usr/syno/`:** Contains the core Synology binaries, scripts, and default configuration templates. This is the "factory" state.
*   **`/etc/`:** Contains the *generated* runtime configuration files that services actually read.
*   **`/etc.defaults/`:** A symlink often pointing to `/usr/syno/etc.defaults`, containing the base templates.
*   **`/var/`:** Writable space for logs, package data, and other stateful information.
*   **`/volume1/@appstore/`:** Installation directory for user-installed packages.
*   **`/volume1/@db/`:** Central location for system-wide databases (threat intel, domain categories, GeoIP).
*   **`/ini/`:** Hardware-specific configuration files, particularly for WiFi chipsets.
*   **`/data/`:** Vendor-specific binary data (WiFi calibration files).

### Configuration Hierarchy
The 3-tier system is key:
1.  **Defaults:** In `/usr/syno/etc.defaults` and `/etc.defaults/`.
2.  **Database:** The "source of truth" for user changes, stored in SQLite databases.
3.  **Live Configs:** The generated files in `/etc/` used by daemons.

*Never edit files in `/etc/` directly, as they will be overwritten on the next service restart.*

### Package Interactions
AppStore packages install their files into `/volume1/@appstore/[PackageName]`. They register with `synoservice` and provide UI components (JSON files) that integrate into the main web interface.

### Cross-Component Dependency Matrix

| Component | Depends On | Used By | Critical Path |
|-----------|------------|---------|---------------|
| syslog-ng | kernel | all services | Yes |
| syno-net-setting | syslog-ng | network services | Yes |
| iptables | syno-net-setting | all network services | Yes |
| dnsmasq | iptables, br0 | LAN clients | Yes |
| httpd | dnsmasq, iptables | Web UI users | Yes |
| hostapd | syno-net-setting | WiFi clients | No |
| SafeAccess | iptables, @db | Security features | No |
| VPN services | iptables | VPN clients | No |

## 5. Key Architectural Patterns

### 3-Tier Configuration System (Defaults → Database → Generated Files)
*   **Benefit:** Allows for clean factory resets (by clearing the database) and atomic configuration changes.
*   **Drawback:** Obfuscates the final state of a service's configuration, making manual debugging difficult.

### Template-Based Config Generation
*   **Benefit:** Decouples the core services (like `dnsmasq`) from Synology's specific configuration schema. Synology can change its database schema without having to recompile `dnsmasq`.
*   **Drawback:** Adds another layer of indirection and requires careful scripting to ensure templates are rendered correctly.

### Read-Only Base with Overlays
*   **Benefit:** The core OS on the flash storage is often mounted read-only. This enhances system stability and makes firmware updates safer, as the core system can be replaced atomically. Writable data is stored on a separate partition.
*   **Drawback:** Can complicate development or manual system modification.

### Bridge-Based Networking
*   **Benefit:** All LAN-side interfaces (Ethernet ports, Wi-Fi SSIDs) are unified into a single logical interface (`br0`). This dramatically simplifies routing, firewall rules, and service binding. Services only need to listen on `br0` to be available to all LAN clients.
*   **Drawback:** Can introduce complexity with certain advanced networking features like VLANs if not managed carefully by the abstraction layer.

### Event-Driven Service Management
*   **Benefit:** Upstart's event-based model allows for flexible service dependencies and parallel startup where possible.
*   **Drawback:** Complex dependency chains can be difficult to debug when services fail to start.

## 6. Critical Issues and Considerations

### Unbounded Database Growth
*   **Problem:** The central SQLite databases (particularly in Traffic and SafeAccess packages) may store historical data without proper rotation or pruning mechanisms. This database can grow very large over time.
*   **Impact:** Can lead to slow UI performance (as queries take longer), slow service restarts (as config generation slows), and in extreme cases, exhaustion of the storage partition.
*   **Recommendation:** Implement automated database maintenance tasks using `synosched` or custom scripts to prune old records. Monitor database sizes in `/volume1/@appstore/*/var/db/`.

### Configuration Complexity
*   **Problem:** The 3-tier configuration model makes it difficult to answer a simple question: "What is the exact value of `setting_X` being used by `service_Y`?" You have to check defaults, the database, and the generation script's logic.
*   **Impact:** Increases debugging time and the risk of misconfiguration. Manual changes are strongly discouraged and prone to being overwritten.
*   **Recommendation:** Create debug scripts that trace settings from the database to final configuration files. Document the specific database keys and template files for critical services.

### Service Dependency Brittleness
*   **Problem:** While `Upstart` provides a robust dependency framework, the heavy reliance on imperative shell scripts within `synoservice` can create hidden or fragile dependencies. A script might fail for an unexpected reason (e.g., a temporary network issue), causing a cascading failure of dependent services.
*   **Impact:** Can lead to a partially-functional state that is difficult to diagnose. For example, the UI might be up, but Wi-Fi might be down because a script failed silently.
*   **Recommendation:** Implement better error handling and logging in service control scripts. Use `synoservice --status-all` regularly to detect partially-failed states.

### Production Code Quality Issues
*   **Problem:** Git conflict markers found in production blocklist files indicate inadequate code review and testing processes.
*   **Impact:** Can cause service failures or security vulnerabilities if malformed configuration files are deployed.
*   **Recommendation:** Implement automated validation of configuration files before deployment. Add pre-commit hooks to prevent conflict markers from entering the codebase.

### Limited Horizontal Scalability
*   **Problem:** The monolithic architecture with heavy reliance on single SQLite databases creates bottlenecks that cannot be easily scaled horizontally.
*   **Impact:** Performance degrades as the number of managed devices or security rules increases.
*   **Recommendation:** Consider implementing data partitioning strategies or migration to more scalable data stores for high-volume data.

## 7. Security Architecture

### Defense in Depth
SRM implements multiple layers of security:

```text
┌─────────────────────────────────────────────────────┐
│                  Physical Access                    │
├─────────────────────────────────────────────────────┤
│              Secure Boot (if supported)             │
├─────────────────────────────────────────────────────┤
│            Read-Only Root Filesystem                │
├─────────────────────────────────────────────────────┤
│          Kernel Security (SELinux/AppArmor)         │
├─────────────────────────────────────────────────────┤
│         Network Security (iptables/netfilter)       │
├─────────────────────────────────────────────────────┤
│      Application Security (Suricata IDS/IPS)        │
├─────────────────────────────────────────────────────┤
│         Service Isolation (User/Group perms)        │
├─────────────────────────────────────────────────────┤
│            Encrypted Communications (TLS)           │
└─────────────────────────────────────────────────────┘
```

### Key Security Components
1. **Firewall (iptables):** Stateful packet filtering at kernel level
2. **IDS/IPS (Suricata):** Deep packet inspection for threat detection
3. **SafeAccess:** Content filtering and parental controls
4. **Threat Intelligence:** Regular updates from multiple sources (FireHOL, Google Safe Browsing)
5. **Certificate Management:** Centralized SSL/TLS certificate handling

## 8. Performance Considerations

### Bottlenecks
1. **SQLite Database Operations:** Single-threaded writes can become a bottleneck
2. **Configuration Generation:** Template rendering can be CPU-intensive
3. **Packet Processing:** Deep packet inspection impacts throughput
4. **Logging:** Excessive logging can impact I/O performance

### Optimization Opportunities
1. **Database Indexing:** Ensure proper indexes on frequently-queried columns
2. **Service Parallelization:** Where possible, start independent services in parallel
3. **Caching:** Implement caching for frequently-accessed configuration data
4. **Log Rotation:** Aggressive log rotation to prevent disk space issues

## 9. Maintenance and Operations

### Key Operational Commands
```bash
# Service Management
synoservice --status-all          # Check all service states
synoservice --restart <service>   # Restart a specific service
synoservice --why <service>       # Show why a service is in its current state

# System Information
synogear list                     # List installed packages
cat /etc/VERSION                  # Show firmware version
df -h                            # Check disk usage

# Network Diagnostics
iptables-save                    # View current firewall rules
ip route show                    # Display routing table
brctl show                       # Show bridge configuration

# Log Analysis
tail -f /var/log/messages        # Monitor system logs
grep -i error /var/log/*         # Search for errors
```

### Backup Considerations
Critical items to backup:
1. `/etc/` - All active configurations
2. `/volume1/@appstore/*/etc/` - Package configurations
3. SQLite databases - User settings and historical data
4. `/usr/syno/etc/` - Custom scripts or modifications

### Monitoring Recommendations
1. **Resource Monitoring:** CPU, memory, disk usage, network throughput
2. **Service Monitoring:** All critical services should be monitored for availability
3. **Log Monitoring:** Automated alerts for error patterns
4. **Database Size Monitoring:** Track growth of SQLite databases
5. **Security Monitoring:** Failed login attempts, firewall blocks, IDS alerts

## 10. Conclusion

The Synology SRM architecture represents a sophisticated embedded Linux system optimized for router functionality. Its layered design provides good separation of concerns, while the template-based configuration system offers flexibility at the cost of complexity.

Key strengths include:
- Modular, package-based extensibility
- Comprehensive security features
- Unified networking model (bridge-based)
- Robust service management framework

Key challenges include:
- Configuration complexity and opacity
- Database scalability limitations
- Service dependency brittleness
- Limited horizontal scaling options

Understanding these architectural patterns and relationships is essential for effective system administration, troubleshooting, and development on the SRM platform.

---

## Version Information
- **Document Version**: 1.0
- **Last Updated**: 2025-06-23
- **System**: Synology RT6600ax
- **Firmware**: SRM 5.2-9346
- **Analysis Scope**: Complete system architecture

---
*This documentation was created as part of the comprehensive Synology SRM system analysis project.*