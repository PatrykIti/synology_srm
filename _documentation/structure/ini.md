# /ini Directory - WiFi Hardware Configuration

[← Back to Documentation Index](../README.md) | [← Previous: /etc.defaults](etc.defaults.md) | [→ Next: /initrd](initrd.md)

---

## Overview
The `/ini` directory contains critical WiFi hardware configuration files for Synology SRM's wireless subsystem. This directory stores initialization parameters for Qualcomm Atheros WiFi chipsets (QCA6018 and QCN9000) used in the RT6600ax router. The configuration files control hardware-level WiFi operations, 802.11ax (WiFi 6) features, network subsystem offloading, and advanced wireless capabilities.

## Directory Structure
```
/ini/
├── global.ini              # Global WiFi configuration parameters
├── QCA6018.ini            # QCA6018 chipset-specific configuration
├── QCN9000.ini            # QCN9000 chipset-specific configuration
├── wifi_module_param.ini   # WiFi module loading parameters
└── internal/              # Internal/advanced configurations
    ├── global_i.ini       # Internal global parameters
    ├── QCA6018_i.ini      # Internal QCA6018 parameters
    └── QCN9000_i.ini      # Internal QCN9000 parameters
```

## Key Components

### Global Configuration (global.ini)
- **Purpose**: System-wide WiFi parameters applicable to all chipsets
- **Content**: General wireless settings, feature flags, debugging options
- **Features**:
  - 802.11ax (WiFi 6) global settings
  - System-wide offload configurations
  - Debug and logging parameters
  - Memory allocation settings

### Chipset-Specific Configurations

#### QCA6018.ini
- **Purpose**: Configuration for Qualcomm QCA6018 chipset (5GHz band)
- **Hardware**: IPQ6018 integrated WiFi 6 solution
- **Features**:
  - Support for 2x2 MIMO
  - 80MHz channel width
  - MU-MIMO and OFDMA
  - Target Wake Time (TWT) support

#### QCN9000.ini
- **Purpose**: Configuration for Qualcomm QCN9000 chipset (5GHz/6GHz bands)
- **Hardware**: High-performance external WiFi 6E chip
- **Features**:
  - Support for 4x4 MIMO
  - 160MHz channel width
  - 6GHz band support (WiFi 6E)
  - Advanced beamforming

### Module Parameters (wifi_module_param.ini)
- **Purpose**: Kernel module loading parameters for WiFi drivers
- **Content**:
  - Module initialization options
  - Hardware detection parameters
  - Resource allocation settings
  - Performance tuning flags

### Internal Configurations (/internal/)
- **Purpose**: Advanced/low-level hardware configurations
- **Naming**: "_i" suffix indicates internal parameters
- **Usage**: Used by firmware and low-level drivers
- **Content**:
  - Datapath configurations (ring buffers, descriptors)
  - Control path settings (vdev limits, peer management)
  - Hardware acceleration parameters
  - Memory management details

## Configuration Categories

### 1. Hardware Operation Modes
- DBS (Dual Band Simultaneous) mode
- SBS (Single Band Simultaneous) mode
- Hardware queue configurations
- Interrupt handling modes

### 2. WiFi 6/6E Features
- OFDMA (Orthogonal Frequency Division Multiple Access)
- MU-MIMO (Multi-User MIMO) settings
- BSS Coloring for interference reduction
- Target Wake Time (TWT) for power saving
- Spatial Reuse parameters

### 3. Network Subsystem (NSS) Offload
- Hardware acceleration settings
- Checksum offloading
- TSO (TCP Segmentation Offload)
- LRO (Large Receive Offload)
- Flow acceleration parameters

### 4. Memory Management
- Ring buffer sizes
- Descriptor counts
- DMA configurations
- Memory pool allocations

### 5. Advanced Features
- Mesh networking support
- WDS (Wireless Distribution System)
- Smart antenna configurations
- Beamforming parameters
- Band steering settings

## Scripts and Executables
No executable scripts in this directory - purely configuration files loaded by:
- WiFi kernel modules during initialization
- `qsdk` daemon for runtime management
- `synowifi` service for high-level control

## Integration Points

### Kernel Modules
- `ath11k` driver reads chipset configurations
- `qca_nss_wifi` loads NSS offload parameters
- Module parameters applied during `insmod`

### System Services
- `/etc/init/wifi-module.conf` - Loads modules with parameters
- `synowifid` - Manages WiFi configurations
- `qsdk` - Qualcomm SDK integration layer

### Runtime Management
- Configurations loaded once at boot
- Some parameters can be modified via `debugfs`
- Changes typically require module reload

## Security Considerations

### Access Control
- Directory permissions: 700 (owner only)
- File permissions: 700 (read/write by owner only)
- Owner: root user in production

### Configuration Security
- Parameters control hardware behavior
- Incorrect settings can cause instability
- Some debug features could expose sensitive data
- Production systems should disable verbose debugging

## Network Services
These configurations enable:
- 2.4GHz and 5GHz WiFi networks
- Guest network isolation
- Mesh networking capabilities
- WPS (WiFi Protected Setup)
- Band steering between radios

## Performance Considerations

### Resource Usage
- **Disk Space**: Minimal (~1MB for all INI files)
- **Memory**: Configuration cached in driver memory (~10MB)
- **CPU**: One-time parsing during module load
- **I/O**: Single read operation per boot

### Performance Impact
- **WiFi Throughput**: NSS offload settings directly impact max speeds
- **Latency**: Buffer configurations affect packet processing time
- **Concurrent Clients**: Queue depths determine connection limits
- **Channel Efficiency**: OFDMA/MU-MIMO settings affect airtime usage

### Optimization Notes
- NSS offload parameters critical for gigabit speeds
- Ring buffer sizes balance memory vs performance
- Interrupt coalescing reduces CPU overhead
- Proper DBS/SBS mode selection optimizes dual-band performance

## Maintenance Notes

### Configuration Updates
- Updates typically come with firmware upgrades
- Manual editing not recommended
- Backup before firmware updates
- Test changes in controlled environment

### Troubleshooting
- Check `/var/log/wifi.log` for configuration errors
- Use `iw` and `iwconfig` for runtime verification
- Monitor `dmesg` for module loading issues
- Review `/sys/kernel/debug/ath11k/` for debug info

### Performance Tuning
- NSS offload parameters affect throughput
- Buffer sizes impact latency
- Queue depths affect concurrent connections
- Monitor with `cat /proc/net/nss-wifi/stats`

## Platform-Specific Features

### RT6600ax Implementation
- Tri-band router (2.4GHz + 2x 5GHz)
- QCA6018 for integrated 5GHz radio
- QCN9000 for high-performance 5GHz radio
- Hardware supports WiFi 6 (802.11ax)

### Synology Customizations
- Enhanced mesh networking parameters
- SRM-specific feature flags
- Integration with Safe Access
- Traffic Control optimizations

## Cross-References
- WiFi service configuration: [/etc/init/wifi-module.conf](etc.md#wifi-configuration)
- Runtime WiFi logs: [/var/log/wifi.log](var.md#wifi-logs)
- WiFi management daemon: [/usr/sbin/synowifid](usr.md#synology-daemons)
- Kernel modules: [/lib/modules/](lib.md#kernel-modules)

## Version Information
- **Document Version**: 2.0
- **Last Updated**: 2025-06-23
- **System**: Synology RT6600ax
- **Firmware**: SRM 5.2-9346
- **Analysis**: Complete WiFi configuration analysis

---

[← Back to Documentation Index](../README.md) | [← Previous: /etc.defaults](etc.defaults.md) | [→ Next: /initrd](initrd.md)

---
*This documentation was created as part of the comprehensive Synology SRM system analysis project.*
