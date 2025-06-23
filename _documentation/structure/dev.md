# /dev Directory - Device Files

[← Back to Documentation Index](../README.md) | [← Previous: /sys](sys.md) | [→ Next: /proc](proc.md)

---

## Overview
The `/dev` directory contains device files (also called device nodes) that provide interfaces to kernel drivers. These special files allow user-space programs to interact with hardware devices and kernel subsystems through standard file I/O operations. In Synology SRM, this directory is populated dynamically by udev based on detected hardware and loaded kernel modules.

## Directory Structure
```
/dev/                          [Device filesystem - tmpfs]
├── block/                     [Block device links]
├── bus/                       [Bus device links]
├── char/                      [Character device links]
├── disk/                      [Disk device links]
│   ├── by-id/                [Persistent names by ID]
│   ├── by-path/              [Persistent names by path]
│   └── by-uuid/              [Persistent names by UUID]
├── input/                     [Input devices]
│   ├── event0                [Power button]
│   └── event1                [Reset button]
├── mapper/                    [Device mapper]
├── net/                       [Network devices]
│   └── tun                   [TUN/TAP device]
├── pts/                       [Pseudo-terminals]
├── shm/                       [Shared memory]
└── snd/                       [Sound devices (unused)]

## Common Device Files
├── console                    [System console]
├── full                       [Always full device]
├── kmsg                       [Kernel messages]
├── log                        [Syslog socket]
├── mem                        [Physical memory]
├── null                       [Null device]
├── port                       [I/O ports]
├── ptmx                       [PTY master]
├── random                     [Random numbers]
├── sda, sdb                   [SCSI/SATA disks]
├── sg0, sg1                   [SCSI generic]
├── tty                        [Current terminal]
├── tty0-63                    [Virtual consoles]
├── ttyS0-3                    [Serial ports]
├── urandom                    [Pseudo-random]
├── vcs, vcsa                  [Virtual console memory]
├── watchdog                   [Hardware watchdog]
└── zero                       [Zero device]
```

## Key Components

### Block Devices
- **Purpose**: Devices that transfer data in blocks
- **Storage Devices**:
  - `/dev/sda`, `/dev/sdb`: SATA/USB drives
  - `/dev/sda1`, `/dev/sda2`: Partitions
  - `/dev/mmcblk0`: eMMC storage
  - `/dev/mtdblock0-9`: MTD flash partitions
- **Virtual Block Devices**:
  - `/dev/loop0-7`: Loop devices
  - `/dev/ram0-15`: RAM disks
  - `/dev/md0-9`: Software RAID
- **Device Mapper**:
  - `/dev/mapper/*`: LVM/encrypted volumes

### Character Devices
- **Purpose**: Devices that transfer data character by character
- **Terminal Devices**:
  - `/dev/tty`: Current terminal
  - `/dev/ttyS0-3`: Hardware serial ports
  - `/dev/tty1-63`: Virtual terminals
  - `/dev/pts/*`: Pseudo-terminals
- **Special Devices**:
  - `/dev/null`: Discards all data
  - `/dev/zero`: Provides null bytes
  - `/dev/random`: Cryptographic RNG
  - `/dev/urandom`: Pseudo-RNG

### Network Devices
- **Purpose**: Network-related device files
- **TUN/TAP**: `/dev/net/tun` for VPN
- **Packet Socket**: Raw network access
- **Note**: Most network devices accessed via sysfs/netlink

### Input Devices
- **Purpose**: Hardware input interfaces
- **Event Devices**:
  - `/dev/input/event0`: Power button
  - `/dev/input/event1`: Reset button
  - `/dev/input/event2`: WPS button
- **Integration**: Monitored by system daemons

## Configuration Files

### udev Rules
Located in `/etc/udev/rules.d/`:
- Device naming policies
- Permission settings
- Symlink creation
- Event triggers

### Device Permissions
Default permissions set by udev:
- Block devices: 660 (root:disk)
- TTY devices: 620 (root:tty)
- Input devices: 640 (root:input)
- Special devices: 666 (world-writable)

## Scripts and Executables

### Device Creation
```bash
# Manual device creation (rarely needed)
mknod /dev/mydevice c 250 0

# udev typically handles this automatically
udevadm trigger
udevadm settle
```

### Device Management Commands
- `lsblk`: List block devices
- `blkid`: Show block device attributes
- `udevadm`: udev administration
- `mdev`: BusyBox device manager

## Integration Points

### Kernel Integration
- Device files created based on kernel drivers
- Major/minor numbers map to drivers
- ioctl() calls for device-specific operations

### udev System
- Monitors kernel uevents
- Creates/removes device files
- Manages permissions and ownership
- Creates convenience symlinks

### System Services
- Init scripts wait for devices
- Mount operations use block devices
- Logging uses /dev/log socket
- Console output to /dev/console

## Security Considerations

### Access Control
- Device permissions critical for security
- Group membership controls access
- Some devices extremely sensitive

### Sensitive Devices
- `/dev/mem`: Direct memory access
- `/dev/kmem`: Kernel memory (disabled)
- `/dev/port`: I/O port access
- Block devices: Raw disk access

### Security Best Practices
1. Restrict device permissions
2. Use groups for access control
3. Monitor device creation
4. Audit device access

## Network Services
While /dev doesn't directly provide network services:
- `/dev/net/tun`: Used by VPN services
- Network devices managed separately
- Raw sockets for packet capture

## Performance Considerations

### Resource Usage
- **Disk Space**: Minimal (tmpfs)
- **Memory**: Small tmpfs overhead
- **CPU**: Negligible
- **I/O**: Depends on device usage

### Performance Impact
- Device files are just interfaces
- Actual I/O performance device-dependent
- udev rules can impact boot time
- Too many devices slow enumeration

### Optimization Notes
- tmpfs backed for speed
- Minimal memory footprint
- Dynamic creation reduces waste
- Symlinks for convenience

## Maintenance Notes

### Common Tasks
1. **Check Device Presence**:
   ```bash
   ls -la /dev/sda*
   ls -la /dev/ttyS*
   ```

2. **Monitor Device Events**:
   ```bash
   udevadm monitor
   ```

3. **Debug Device Issues**:
   ```bash
   dmesg | grep -i "device"
   udevadm info /dev/sda
   ```

### Troubleshooting
- Missing devices: Check kernel modules
- Permission denied: Verify group membership
- Device busy: Check with lsof/fuser
- Symlinks broken: Run udevadm trigger

### Best Practices
1. Never manually modify while system running
2. Use udev rules for customization
3. Back up custom udev rules
4. Test changes in recovery mode

## Cross-References
- Kernel interface: [/sys/](sys.md)
- Process information: [/proc/](proc.md)
- udev configuration: [/etc/udev/](etc.md#udev-rules)
- Mount points: [/mnt/](mnt.md)
- System logs: [/var/log/](var.md#system-logs)

---

[← Back to Documentation Index](../README.md) | [← Previous: /sys](sys.md) | [→ Next: /proc](proc.md)