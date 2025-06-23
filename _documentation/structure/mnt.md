# /mnt Directory

## Overview

The `/mnt` directory is a traditional Unix mount point that exists in Synology SRM RT6600ax but is **not actively used** by the system's automatic mount functionality. While present for compatibility and potential manual administrative use, all dynamically mounted external storage devices are handled by Synology's proprietary storage management system, which mounts devices to `/volumeUSB{N}` or `/volumeSATA{N}` directories instead. This architectural decision ensures consistent naming, proper integration with Synology services, and centralized management of external storage.

## Directory Structure

```
/mnt/
    (empty)
```

The directory remains empty in both the backup and running system under normal operation, serving only as a legacy mount point for manual administrative tasks.

## Key Components

### Mount Point Architecture
- **Primary Purpose**: Legacy compatibility and manual mount operations
- **Actual External Storage**: Handled by `/volumeUSB{N}` and `/volumeSATA{N}`
- **Filesystem Support**: FAT32, NTFS, EXT3/4, exFAT
- **Device Detection**: Block device events via kernel and udev

### Userspace Tools
- **mount.vfat**: FAT32 filesystem mounting
- **mount.exfat**: exFAT filesystem mounting (optimized for flash media)
- **ntfs-3g**: NTFS read/write support via FUSE
- **mount.ecryptfs**: Encrypted folder support
- **blkid**: Block device identification and UUID extraction
- **fsck**: Filesystem consistency checking

### Kernel Modules
- **vfat**: FAT32 kernel driver
- **exfat**: exFAT kernel driver
- **ext4**: EXT3/4 filesystem driver
- **ntfs**: Basic NTFS support (read-only)
- **fuse**: Filesystem in Userspace for ntfs-3g
- **ecryptfs**: Stacked cryptographic filesystem

### Synology Services
- **Storage Management Daemon**: Proprietary service responding to hotplug events
- **synostgmond**: Likely candidate for storage monitoring and management
- **udev Integration**: Rules triggering Synology-specific mount workflows

## Configuration Files

### udev Rules
- **Primary Location**: `/etc/udev/rules.d/`
- **System Rules**: `/usr/lib/udev/rules.d/`
- **Example Rule Pattern**:
  ```
  SUBSYSTEM=="block", KERNEL=="sd[a-z][0-9]*", ACTION=="add", RUN+="/usr/syno/bin/hotplug_storage.sh add %k"
  ```

### Mount Configuration
- **Static Mounts**: Not used for external devices (no `/etc/fstab` entries)
- **Runtime Configuration**: Likely generated in `/run/` or `/tmp/`
- **Mount Options**: Stored in Synology's configuration database

## Scripts and Executables

This section describes the likely workflow based on standard Linux practices and analysis of Synology's architecture. The exact script names and IPC mechanisms are hypothesized and require direct system inspection to verify.

### Hypothesized Hotplug Script Workflow
1. **Device Detection**: Kernel detects USB/SATA device insertion
2. **udev Event**: Generates add event with device properties
3. **Synology Script Execution**: (e.g., `/usr/syno/bin/hotplug_storage.sh`)
   - Reads device information via `blkid`
   - Determines filesystem type
   - Performs filesystem check if enabled
   - Creates mount point directory
   - Executes mount with appropriate options
4. **Service Notification**: Informs File Station, Media Server, etc.
5. **User Interface Update**: Reflects new volume availability

### Common Mount Options
```bash
# Performance optimizations
noatime,nodiratime

# Security hardening (should be default for external media)
noexec,nosuid,nodev

# NTFS-specific
uid=1024,gid=100,dmask=000,fmask=111
```

## Integration Points

### Service Notification Mechanisms
- **D-Bus**: Standard Linux IPC for device events
- **Custom Socket/IPC**: Proprietary Synology messaging
- **Directory Watchers**: Services monitoring `/volume*` changes
- **Database Updates**: SQLite entries for volume metadata

### Integrated Services
- **File Station**: File management interface
- **Media Server**: DLNA/UPnP media sharing
- **Download Station**: Torrent/download management
- **Surveillance Station**: Security camera storage
- **SMB/AFP**: Network file sharing protocols

## Security Considerations

### Mount Security
- **Secure Mount Options**: External media should always be mounted with `noexec,nosuid,nodev` to prevent execution of malicious code and privilege escalation attacks
- **Automount Risks**: Automatic mounting of unknown devices poses inherent security risks
- **Filesystem Trust**: External media may contain malicious filesystem structures

### Filesystem Driver Vulnerabilities
- **Attack Surface**: Complex filesystem drivers (especially NTFS via ntfs-3g and exFAT) can contain vulnerabilities
- **Kernel Exposure**: Native kernel drivers run in privileged context
- **FUSE Security**: ntfs-3g runs in userspace, limiting damage from exploits
- **Mitigation**: Keep SRM firmware updated for latest driver patches

### eCryptfs Key Management
When using encrypted folders, the security of the encryption is entirely dependent on the management of the passphrase/key. A critical point for investigation is where SRM stores the unwrapped file encryption key. If the key is stored in plaintext on the device's internal flash, it may offer a false sense of security against an attacker with physical access or root privileges on the device. True security relies on the key being derived from a user-provided passphrase at runtime and never stored at rest.

### Access Control
- **Permission Enforcement**: Standard Unix permissions apply
- **Shared Folder ACLs**: Additional Synology-specific access controls
- **USB Device Filtering**: Potential for device whitelist/blacklist

## Network Services

While `/mnt` itself doesn't expose network services, external storage mounted via the system becomes available through:

- **SMB/CIFS**: Windows file sharing on ports 139, 445
- **AFP**: Apple Filing Protocol on port 548
- **NFS**: Network File System on port 2049
- **WebDAV**: HTTP-based file access on ports 5005/5006
- **FTP/SFTP**: File transfer protocols on ports 21/22

## Maintenance and Troubleshooting

The `/mnt` directory can be used for manual, temporary mounts during diagnostics (e.g., `mount -o ro /dev/sdb1 /mnt`).

To debug issues with the automatic mounting of external drives, follow this sequence:

1. **Check Kernel-Level Detection**: Connect the device and run `dmesg | tail -n 20`. Look for messages from `usb-storage` or `scsi` indicating the device and its partitions (e.g., `sdb: sdb1`) were recognized.

2. **Monitor udev Events**: Run `udevadm monitor --property` and then connect the device. This will show the event being created and the properties `udev` is assigning (like `ID_FS_TYPE`, `ID_FS_UUID`). This confirms the handoff from kernel to userspace.

3. **Inspect System Logs**: Check the main system log for entries from Synology's services. The exact log file may vary, but `/var/log/messages` is a common location. Use a command like `tail -f /var/log/messages | grep -iE 'syno|usb|mount'` to watch for relevant events from storage-related daemons (e.g., `synostgmond`). This should reveal how the storage daemon is reacting to the udev event.

4. **Verify Mounts**: Once mounted, use `mount | grep /volume` to see the actual device, mount point (e.g., `/volumeUSB1`), filesystem type, and mount options applied by SRM.