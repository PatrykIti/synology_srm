# /sys Directory - Kernel Interface (sysfs)

[← Back to Documentation Index](../README.md) | [← Previous: /usr](usr.md) | [→ Next: /dev](dev.md)

---

## Overview
The `/sys` directory is a virtual filesystem (sysfs) that provides a structured view into the kernel's device model. Created dynamically at boot time by the Linux kernel, it exposes kernel data structures, device attributes, and driver parameters as a hierarchy of files and directories. For the Synology RT6600ax router, this interface is crucial for hardware management, network device configuration, and system monitoring.

## Directory Structure
```
/sys/                          [Virtual filesystem - kernel 4.4.60]
├── block/                     [Block devices]
│   ├── sda/                  [Primary storage device]
│   └── mtdblock*/            [MTD flash partitions]
├── bus/                       [System buses]
│   ├── usb/                  [USB subsystem]
│   ├── pci/                  [PCI devices]
│   ├── platform/             [Platform devices]
│   └── spi/                  [SPI bus devices]
├── class/                     [Device classes]
│   ├── net/                  [Network interfaces]
│   │   ├── eth0-4/           [Ethernet ports]
│   │   ├── wlan0-1/          [WiFi interfaces]
│   │   └── br0/              [Bridge interface]
│   ├── gpio/                 [GPIO pins]
│   ├── leds/                 [LED controls]
│   ├── thermal/              [Temperature sensors]
│   └── rtc/                  [Real-time clock]
├── devices/                   [Device hierarchy]
│   ├── platform/             [Platform-specific devices]
│   ├── system/               [System devices]
│   └── virtual/              [Virtual devices]
├── firmware/                  [Firmware interfaces]
│   ├── devicetree/           [Device tree]
│   └── qcom/                 [Qualcomm firmware]
├── fs/                        [Filesystem information]
├── kernel/                    [Kernel parameters]
│   ├── debug/                [Debug interfaces]
│   └── security/             [Security modules]
├── module/                    [Loaded kernel modules]
│   ├── ath11k/               [WiFi 6 driver]
│   ├── nf_*/                 [Netfilter modules]
│   └── synobios/             [Synology hardware]
└── power/                     [Power management]
```

## Key Components

### Network Interfaces (/sys/class/net)
- **Purpose**: Network device management and statistics
- **Ethernet Ports**: eth0-eth4 (5 Gigabit ports)
  - `address`: MAC address
  - `carrier`: Link status (0/1)
  - `speed`: Link speed in Mbps
  - `statistics/`: RX/TX counters
  - `queues/`: Multi-queue configuration
- **WiFi Interfaces**: wlan0 (5GHz), wlan1 (2.4GHz)
  - Qualcomm ath11k driver attributes
  - Regulatory domain settings
  - Power management controls
- **Bridge Interface**: br0 (LAN bridge)
  - Bridge port membership
  - STP parameters
  - Forwarding database size

### Block Devices (/sys/block)
- **Purpose**: Storage device information
- **MTD Devices**: Flash memory partitions
  - mtdblock0-9: Bootloader, kernel, config
  - Read-only vs read-write partitions
  - Erase block information
- **USB Storage**: When connected
  - Device identification
  - Partition information
  - Queue parameters

### Hardware Platform (/sys/devices/platform)
- **Purpose**: SoC-specific device management
- **Qualcomm IPQ6018 Devices**:
  - CPU frequency scaling
  - Memory controllers
  - Hardware crypto engine
  - Network accelerators
- **Synology Hardware**:
  - LED controllers
  - Fan control
  - Button inputs
  - Hardware monitor

### Thermal Management (/sys/class/thermal)
- **Purpose**: Temperature monitoring and control
- **Thermal Zones**:
  - CPU temperature sensors
  - WiFi chip temperatures
  - System board sensors
- **Cooling Devices**:
  - Fan speed control
  - CPU frequency throttling
  - Trip points configuration

## Configuration Files

### Network Device Tuning
Located in `/sys/class/net/*/`:
- `tx_queue_len`: Transmit queue length
- `mtu`: Maximum transmission unit
- `gro_flush_timeout`: Generic receive offload
- `napi_weight`: Interrupt mitigation

### CPU Performance
Located in `/sys/devices/system/cpu/`:
- `cpu*/cpufreq/`: Frequency scaling
- `cpu*/online`: CPU hotplug
- `cpu*/cache/`: Cache parameters

### Memory Management
Located in `/sys/kernel/mm/`:
- `transparent_hugepage/`: THP settings
- `ksm/`: Kernel same-page merging
- Page allocation statistics

## Scripts and Executables

### sysfs Access Patterns
Common operations via shell:
```bash
# Read attribute
cat /sys/class/net/eth0/carrier

# Write attribute
echo 1 > /sys/class/leds/status/brightness

# Monitor changes
inotifywait -m /sys/class/net/eth0/carrier
```

### Synology Integration
- Network scripts read/write sysfs
- Hardware monitor polls thermal zones
- LED management via sysfs interface
- Power management through sysfs

## Integration Points

### udev Integration
- udev rules triggered by sysfs events
- Device naming based on sysfs attributes
- Hotplug handling via sysfs notifications

### Driver Interfaces
- Network drivers expose tuning parameters
- Storage drivers provide statistics
- Platform drivers control hardware

### Monitoring Tools
- System monitors read from sysfs
- Performance tools use sysfs counters
- Hardware status from sysfs attributes

## Security Considerations

### Access Control
- Most files readable by all users
- Write access restricted to root
- Some files in debugfs require root even to read

### Information Disclosure
- Hardware details exposed
- Network statistics visible
- Kernel addresses in some files

### Attack Surface
- sysfs parameters can affect stability
- Incorrect values may crash drivers
- Some attributes control security features

## Network Services
While /sys itself doesn't provide network services, it exposes:
- Network interface configuration
- Traffic statistics and counters
- Hardware offload capabilities
- Wireless regulatory settings
- Bridge and VLAN configuration

## Performance Considerations

### Resource Usage
- **Disk Space**: 0 (virtual filesystem)
- **Memory**: Minimal kernel memory
- **CPU**: Low overhead for reads
- **I/O**: No disk I/O

### Performance Impact
- Reading sysfs files may block
- Some attributes expensive to compute
- Polling sysfs can impact performance
- Writing triggers kernel actions

### Optimization Notes
- Cache frequently read values
- Avoid polling in tight loops
- Use inotify for change detection
- Batch reads when possible

## Maintenance Notes

### Common Tasks
1. **Network Debugging**:
   - Check link status: `/sys/class/net/*/carrier`
   - View statistics: `/sys/class/net/*/statistics/`
   - Monitor errors: `/sys/class/net/*/statistics/*_errors`

2. **Hardware Monitoring**:
   - CPU temperature: `/sys/class/thermal/thermal_zone*/temp`
   - Fan speed: `/sys/class/hwmon/*/fan*_input`
   - LED control: `/sys/class/leds/*/brightness`

3. **Performance Tuning**:
   - CPU governor: `/sys/devices/system/cpu/cpu*/cpufreq/scaling_governor`
   - Network queues: `/sys/class/net/*/queues/*/`

### Troubleshooting
- Missing files indicate missing drivers
- Permission errors usually mean root required
- Values of 4294967295 often mean "not applicable"
- Some files only appear when hardware present

## Cross-References
- Device files: [/dev/](dev.md)
- Process information: [/proc/](proc.md)
- Kernel modules: [/lib/modules/](lib.md#kernel-modules)
- Network configuration: [/etc/network/](etc.md#network-configuration)
- Hardware initialization: [/etc/init/](etc.md#upstart-services)

---

[← Back to Documentation Index](../README.md) | [← Previous: /usr](usr.md) | [→ Next: /dev](dev.md)