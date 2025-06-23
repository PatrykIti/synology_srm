# Configuration Management Guide for Synology SRM

This guide provides system administrators with a comprehensive understanding of the Synology Router Manager (SRM) configuration architecture. Adhering to these principles is critical for maintaining a stable, supportable, and predictable system.

## 1. Configuration Architecture Overview

Synology SRM employs a three-tier, database-driven configuration system designed for stability and consistency. This architecture ensures that user-defined settings are preserved across system updates and can be reliably managed through the web interface.

### The Three Tiers

#### Tier 1: Default Layer (Templates)
- **Location:** `/etc.defaults/` and `/usr/syno/etc.defaults/`
- **Purpose:** Contains factory-default configuration templates for all system services (e.g., `sshd_config.mustache`, `httpd.conf-sys.mustache`). These are the "blueprints" for configuration files.
- **Behavior:** This layer is read-only from an administrator's perspective. System updates may overwrite or change these templates. **Never edit files in this layer.**

#### Tier 2: Database Layer (User Modifications)
- **Location:** Configuration files and SQLite databases. The primary key-value store is `/etc/synoinfo.conf`, with complex settings stored in SQLite databases.
- **Purpose:** This is the "source of truth" for all user-modified settings. When you change a setting in the SRM Web UI, the change is written to this database layer.
- **Behavior:** This layer is persistent. It is the target of the built-in "Configuration Backup" feature.

#### Tier 3: Active Layer (Runtime Configuration)
- **Location:** `/etc/` and other runtime paths (e.g., `/var/etc/`).
- **Purpose:** Contains the actual configuration files that running services use (e.g., `/etc/ssh/sshd_config`).
- **Behavior:** This layer is **ephemeral and auto-generated**. On boot or service restart, SRM reads the templates from the Default Layer, merges them with user settings from the Database Layer, and writes the resulting file to the Active Layer.

### How They Interact & Why Manual Editing Fails

The system is designed to treat the Active Layer (`/etc/`) as a disposable artifact. Any direct manual edit to a file in `/etc/` will be **overwritten** the next time its managing service is restarted or the router is rebooted. The system will always regenerate it from the database and templates, causing your changes to disappear.

**Analogy:** Think of it like this: The Default Layer is the car's factory design. The Database Layer is your custom order (leather seats, bigger engine). The Active Layer is the physical car delivered to you. You can't change the engine by spray-painting the hood; you must go back to the ordering system.

### Visual Representation

```text
┌─────────────────────┐
│   Web UI Changes    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐     ┌─────────────────────┐
│   Database Layer    │ ←──→│   Default Layer     │
│ (User Modifications)│     │    (Templates)      │
└──────────┬──────────┘     └─────────────────────┘
           │                           │
           └───────────┬───────────────┘
                       │
                       ▼
              ┌─────────────────────┐
              │   Active Layer      │
              │ (Generated Configs) │
              └─────────────────────┘
                       │
                       ▼
              ┌─────────────────────┐
              │   Running Services  │
              └─────────────────────┘
```

## 2. Configuration Flow

Understanding the end-to-end flow is key to troubleshooting.

```text
UI Change → Web API → synoconf library → SQLite DB → synoservice → Template → Config File → Service
```

### Detailed Flow Steps

1. **UI Change:** An admin modifies a setting in the SRM web interface and clicks "Apply".
2. **Web API:** The browser sends a request to SRM's web server, which executes a backend process.
3. **`synoconf` library:** The backend process calls the `libsynoconf.so` library functions to write the new value. This is the only supported programmatic way to alter configuration.
4. **SQLite DB Write:** `synoconf` updates the appropriate key in the configuration database.
5. **`synoservice` command:** The backend process then calls `synoservice` to apply the change (e.g., `synoservice --restart sshd`).
6. **Template & DB Read:** The `synoservice` utility reads the service's template file and fetches all required values from the configuration database.
7. **Config Generation:** It merges the values into the template, creating the final, active config file in `/etc/`.
8. **Service Restart:** `synoservice` stops and starts (or reloads) the actual service daemon, which now reads the newly generated configuration file.

## 3. Configuration Hierarchy & Precedence

The hierarchy is simple and strict:

1. **User-Defined Settings (Database Layer):** Always take highest precedence.
2. **Default Settings (Default Layer):** Used only when no user-defined value exists for a given key.

### Special Cases

- **.override Files:** You may occasionally see `.override` files. These are used by Synology for patching or hotfixes and should **not** be used by administrators. They are injected with high precedence and can create an unpredictable state if misused.
- **Factory Reset:** A "soft" or "hard" factory reset effectively erases the Database Layer, causing the system to revert entirely to the Default Layer settings. This is why a configuration backup is critical.

### Configuration Types and Locations

| Configuration Type | Default Location | Active Location | Database Storage |
|-------------------|------------------|-----------------|------------------|
| System Services | `/etc.defaults/` | `/etc/` | SQLite DB |
| Network Settings | `/usr/syno/etc.defaults/` | `/etc/` | `/etc/synoinfo.conf` |
| Package Configs | `@appstore/*/etc.defaults/` | `@appstore/*/etc/` | Package-specific DB |
| Hardware Configs | N/A | `/ini/` | Read-only |

## 4. Making Configuration Changes

### Supported Method: Web UI
- Use the SRM Web UI for all changes. This is the only way to ensure changes are written to the persistent Database Layer and applied correctly.
- All changes made through the UI are validated, persisted, and properly applied.

### Advanced Method: Command Line (Use with Caution)
For advanced scripting, use the `synoconf` command-line utility to modify the database directly, followed by a `synoservice` call to apply the changes.

```bash
# Example: Programmatically change the SSH port
# 1. Set the new value in the database
synoconf --set "sshd_port" "2222"

# 2. Apply the change by restarting the service
synoservice --restart sshd
```

**Warning:** This bypasses UI validation. Use with extreme caution.

### Forbidden Method: Direct File Editing
- **Never** directly edit files in `/etc/`
- These changes are temporary and will be lost
- Can cause service failures if syntax is incorrect

### How to Verify Changes

1. **Primary:** Check the Web UI. It reads from the database and should reflect the current state.
2. **Secondary (CLI):** Use `synoconf --get [key]` to query the database directly.
   ```bash
   synoconf --get "sshd_port"
   ```
3. **Tertiary (CLI):** Inspect the generated file in `/etc/` to confirm the `synoservice` process worked as expected.

## 5. Service Configuration Management

`synoservice` is the master utility for controlling system services.

### Common Commands

| Command | Description |
|---------|-------------|
| `synoservice --status [service]` | Check if a service is running |
| `synoservice --status-all` | Check all services status |
| `synoservice --stop [service]` | Stop a service |
| `synoservice --start [service]` | Start a service and generate config |
| `synoservice --restart [service]` | Stop, then start a service |
| `synoservice --reload [service]` | Gracefully reload config (if supported) |
| `synoservice --why [service]` | Show why service is in current state |

### Dependency Handling
`synoservice` understands service dependencies. For example, restarting a core networking service may trigger restarts of dependent services like DNS or DHCP. Be aware of this when working on the CLI.

### Troubleshooting Service Issues
If a service fails to start after a configuration change:
1. Run its restart command directly from SSH to see live error output
2. Check system logs:
   - `/var/log/messages` for general system activity
   - Service-specific logs in `/var/log/`
3. Use `synoservice --why [service]` to understand the failure

## 6. Best Practices

### Backup Strategy
- **Regular Backups:** Use **Control Panel > Update & Restore > Configuration Backup** feature regularly
- **What to Backup:**
  - Configuration database (via UI backup)
  - `/etc/synoinfo.conf`
  - Package configurations in `/volume1/@appstore/*/etc/`
  - Custom scripts in Task Scheduler
- **Storage:** Store backups off-router on multiple locations

### Documentation Requirements
- Keep a changelog of modifications made in the UI, including the "why"
- Document any custom scripts or scheduled tasks
- Note any non-standard port configurations
- Track package installations and their configurations

### Update Handling
1. Before applying a major SRM update, ensure you have a recent configuration backup
2. Review release notes for configuration changes
3. Test updates in off-hours if possible
4. Be prepared to restore from backup if issues arise

### Testing Changes
- Make significant changes during maintenance windows
- Test one change at a time
- Verify service functionality after each change
- Have a rollback plan ready

## 7. Advanced Configuration Topics

### Package Configurations
Installed packages follow the same architecture but within their own directory:
- **Location:** `/volume1/@appstore/[PackageName]/etc/`
- **Templates:** Package-specific templates in `etc.defaults/`
- **Active Configs:** Generated in `etc/`
- **Management:** Use Package Center or package-specific CLI tools

### Hardware Configurations (`/ini/`)
- Contains low-level hardware parameters
- **Critical:** Do not modify anything here
- Used for WiFi chipset configurations
- Changes can render hardware non-functional

### Custom Scripts Integration
The correct way to run custom scripts:
1. Use **Control Panel > Services > Task Scheduler**
2. If a script needs to modify system settings:
   ```bash
   # Use synoconf to make persistent changes
   synoconf --set "setting_name" "value"
   synoservice --restart affected_service
   ```
3. Log script actions for troubleshooting

### Emergency Recovery Procedures

#### Physical RESET Button
- **Mode 1 (Soft Reset - 4 seconds):**
  - Resets admin password to default
  - Network settings revert to DHCP
  - Most configurations preserved
  
- **Mode 2 (Hard Reset - 10 seconds):**
  - Wipes all system configurations
  - Erases the Database Layer
  - Reinstalls SRM
  - User data on attached storage preserved

#### Recovery via SSH
If UI is inaccessible but SSH works:
```bash
# Check service status
synoservice --status-all

# Restart web interface
synoservice --restart httpd

# Check for configuration errors
tail -f /var/log/messages
```

## 8. Common Pitfalls & Solutions

### Pitfall: Manual Config Changes Disappeared
- **Cause:** Direct editing of files in `/etc/`
- **Solution:** Make all changes through Web UI or use `synoconf`/`synoservice`
- **Prevention:** Never edit `/etc/` files directly

### Pitfall: Service Fails After UI Change
- **Cause:** Invalid configuration value or conflicts
- **Solution:**
  1. Revert change in UI if accessible
  2. Use SSH: `synoconf --set [key] [old_value]`
  3. Restart service: `synoservice --restart [service]`
  4. Check `/var/log/messages` for errors

### Pitfall: System Erratic After Package Install
- **Cause:** Package conflicts or misconfiguration
- **Solution:**
  1. Stop package via Package Center
  2. Review package configuration
  3. Check for port conflicts
  4. Uninstall if necessary

### Pitfall: Configuration Database Corruption
- **Cause:** Power loss during write, failing storage
- **Solution:**
  1. Restore from configuration backup
  2. If unavailable, perform Mode 2 reset
  3. Implement UPS to prevent future occurrences

### Pitfall: Changes Not Persisting Across Reboots
- **Cause:** Making changes at wrong layer
- **Solution:**
  1. Verify changes via `synoconf --get`
  2. Ensure using UI or synoconf for changes
  3. Check if package overwrites settings

## 9. Configuration Reference

### Key Configuration Files

| File/Directory | Purpose | Edit Safe? |
|----------------|---------|------------|
| `/etc/synoinfo.conf` | System information store | No - Use synoconf |
| `/etc/*.conf` | Active service configs | No - Auto-generated |
| `/etc.defaults/*` | Configuration templates | No - Read-only |
| `/ini/*.ini` | Hardware configurations | No - Critical |
| `/volume1/@appstore/*/etc/` | Package configs | Via package UI |

### Essential synoconf Keys

| Key | Description | Example |
|-----|-------------|---------|
| `sshd_port` | SSH port number | 22 |
| `admin_port` | Web UI HTTP port | 8000 |
| `admin_https_port` | Web UI HTTPS port | 8001 |
| `timezone` | System timezone | "Europe/Berlin" |
| `ntpd_enable` | NTP service state | "yes" |

## 10. Conclusion

The Synology SRM configuration management system prioritizes stability and consistency over flexibility. By understanding and working within its constraints—using the Web UI for changes, avoiding direct file edits, and maintaining proper backups—administrators can maintain a reliable and supportable router configuration.

Remember: **The Web UI is the way.** When in doubt, make changes there.

---

## Version Information
- **Document Version**: 1.0
- **Last Updated**: 2025-06-23
- **System**: Synology RT6600ax
- **Firmware**: SRM 5.2-9346
- **Scope**: Configuration Management

---
*This documentation was created as part of the comprehensive Synology SRM system analysis project.*