# /data Directory - Vendor-Specific Application Data

[← Back to Documentation Index](../README.md) | [← Previous: /bin](bin.md) | [→ Next: /etc](etc.md)

---

## Overview
The `/data` directory serves as persistent storage for vendor-specific and application-specific data in Synology SRM. This directory contains proprietary binary firmware files required for hardware initialization and calibration, particularly for the WiFi subsystem. The architectural separation of vendor data from the core operating system ensures maintainability, update safety, and hardware modularity.

## Directory Structure
```
/data/
└── vendor/                      # Vendor-specific data and firmware
    └── wifi/                    # WiFi hardware calibration files
        ├── wlfw_cal_01.bin      # Base WiFi calibration firmware
        └── wlfw_cal_01_qcn9000_pci0.bin  # QCN9000-specific calibration
```

## Key Components

### Vendor WiFi Calibration Files
- **Purpose**: Provide radio frequency (RF) calibration data for WiFi chipsets
- **Location**: `/data/vendor/wifi/`
- **Dependencies**: Required by WiFi kernel drivers (ath11k) during initialization
- **Configuration**: Referenced by WiFi driver configuration in `/ini/` directory
- **Security**: Binary "black box" files - cannot be audited or modified

### File Descriptions
| File Name | Description | Chipset | Purpose |
|-----------|-------------|---------|---------|
| `wlfw_cal_01.bin` | Generic/base calibration firmware | Generic | Fallback or common calibration data for chipset family |
| `wlfw_cal_01_qcn9000_pci0.bin` | Device-specific calibration | QCN9000 | Hardware-specific values for QCN9000 on PCI bus 0 |

## Configuration Files
No configuration files in this directory - contains only binary calibration data. Configuration is handled by:
- `/ini/QCN9000.ini` - Chipset configuration parameters
- `/ini/wifi_module_param.ini` - Module loading parameters
- Driver device tree overlays - Hardware detection and firmware paths

## Scripts and Executables
No scripts or executables - directory contains only binary firmware blobs loaded by kernel drivers.

## Integration Points

### WiFi Driver Loading Sequence
1. **Boot Process**: Kernel loads WiFi driver modules
2. **Hardware Detection**: Driver detects QCN9000 chipset on PCI bus
3. **Firmware Request**: Driver requests calibration firmware from `/data/vendor/wifi/`
4. **Calibration Load**: Binary data loaded onto chipset hardware
5. **Interface Creation**: WiFi interfaces (wlan0, wlan1) become available

### Related Components
- **Kernel Modules**: `ath11k_pci`, `qca_nss_wifi` - Load calibration data
- **Configuration**: `/ini/` directory - Defines firmware paths and parameters
- **Runtime**: `/sys/kernel/debug/ath11k/` - Debug interface for loaded firmware
- **Logs**: `/var/log/wifi.log` - Firmware loading status and errors

## Security Considerations

### Access Control
- **Directory Permissions**: 700 (rwx------) - Owner access only
- **File Permissions**: Should be 644 or 600 - Read-only for security
- **Integrity**: Files must not be modified - will cause WiFi failure

### Operational Security
- **Black Box Nature**: Cannot audit firmware for vulnerabilities
- **Vendor Dependency**: Security depends on Qualcomm/Synology updates
- **Critical Asset**: Corruption prevents WiFi functionality
- **Backup Essential**: Must be included in system backup procedures

## Network Services
These calibration files enable:
- 2.4GHz WiFi network (802.11b/g/n/ax)
- 5GHz WiFi networks (802.11a/n/ac/ax)
- WiFi 6 (802.11ax) features
- MU-MIMO and OFDMA capabilities
- Mesh networking functionality

## Performance Considerations

### Resource Usage
- **Disk Space**: Minimal (~100KB for calibration files)
- **Memory**: No runtime memory usage (loaded once to hardware)
- **CPU**: No CPU impact after initial loading
- **I/O**: Single read operation during boot

### Performance Impact
- **WiFi Throughput**: Calibration quality directly affects maximum speeds
- **Range**: Proper calibration ensures optimal transmission power
- **Stability**: Correct calibration prevents connection drops
- **Channel Efficiency**: Affects spectral efficiency and interference

### Optimization Notes
- Files are pre-optimized at manufacturing
- No user-serviceable performance tuning
- Performance degradation indicates corruption
- Monitor WiFi metrics for calibration health

## Maintenance Notes

### Critical Operational Requirements
- **Do Not Delete**: Removal causes total WiFi failure
- **Do Not Modify**: Any change corrupts calibration data
- **Backup Required**: Include in factory reset preservation
- **Device-Specific**: Cannot use files from different devices

### Troubleshooting
- **WiFi Down**: Check `dmesg` for "firmware load failed"
- **Performance Issues**: May indicate corrupted calibration
- **Recovery**: Restore from backup or factory defaults
- **Logs**: Check `/var/log/wifi.log` for calibration errors

### Failure Indicators
```bash
# Common error messages in logs:
"ath11k_pci: failed to load calibration file"
"wlfw: calibration file not found"
"QCN9000: firmware request failed"
```

## Platform-Specific Features

### RT6600ax Implementation
- **QCN9000 Chipset**: High-performance WiFi 6E capable
- **Dual Calibration**: Supports multiple radio configurations
- **PCI Interface**: Connected via PCIe for high bandwidth
- **Persistent Storage**: Survives firmware updates

### Architectural Benefits
1. **Separation of Concerns**: Isolates vendor data from OS
2. **Update Safety**: OS updates don't affect calibration
3. **Hardware Modularity**: Supports different chipset variants
4. **Manufacturing Flexibility**: Per-device calibration

## Technical Details

### Calibration Data Purpose
- **RF Parameter Correction**: Compensates for manufacturing variations
- **Power Level Tuning**: Ensures regulatory compliance
- **Frequency Accuracy**: Maintains channel precision
- **Temperature Compensation**: Adjusts for thermal variations

### Integration with /ini Configuration
1. INI files define which calibration to load
2. Driver reads INI parameters during initialization
3. Firmware path constructed from INI + hardware detection
4. Calibration loaded based on chipset identification

### Filesystem Characteristics
- **Partition**: Typically on persistent read-write partition
- **Filesystem**: Usually ext4 or similar
- **Mount Options**: Should be mounted with noexec for security
- **Backup**: Included in configuration backup

## Cross-References
- WiFi configuration: [/ini/](ini.md) - Hardware configuration files
- WiFi drivers: [/lib/modules/](lib.md#kernel-modules) - Kernel modules
- WiFi logs: [/var/log/wifi.log](var.md#wifi-logs) - Runtime logs
- Boot process: [/etc/rc](etc.md#boot-scripts) - System initialization

## Version Information
- **Document Version**: 2.0
- **Last Updated**: 2025-06-23
- **System**: Synology RT6600ax
- **Firmware**: SRM 5.2-9346
- **Analysis**: Complete vendor data analysis

---

[← Back to Documentation Index](../README.md) | [← Previous: /bin](bin.md) | [→ Next: /etc](etc.md)

---
*This documentation was created as part of the comprehensive Synology SRM system analysis project.*
