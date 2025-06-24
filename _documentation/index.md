# Synology SRM Documentation Index

## Introduction

Welcome to the comprehensive documentation index for the Synology SRM (Synology Router Manager) system analysis project. This index serves as the primary navigational hub for all technical documentation covering the RT6600ax router firmware version 5.2-9346.

### How to Use This Index

- **Browse by Category**: Navigate through organized sections below
- **Quick Links**: Access frequently used documentation via quick links
- **Search**: Use your browser's search (Ctrl+F/Cmd+F) or see our search implementation plan below
- **Contributing**: See our [Contributing Guide](CONTRIBUTING.md) to help improve documentation

### Documentation Scope

This documentation provides deep technical analysis of:
- System architecture and components
- Directory structures and their purposes
- Configuration management systems
- Network services and security features
- Integration points and dependencies

---

## Master Table of Contents

### 📋 Documentation Overview
- [Documentation README](README.md) - Project overview and status
- [Documentation Template](TEMPLATE.md) - Standard template for consistency
- [Contributing Guidelines](CONTRIBUTING.md) - How to contribute to documentation

### 🏗️ System Architecture
- [System Architecture Diagrams](system_architecture_diagrams.md) - Visual system overview with 6-layer architecture
- [Configuration Management Guide](configuration_management_guide.md) - Understanding the 3-tier configuration system
- [Network Services Inventory](network_services_inventory.md) - Complete list of all network services
- [Final Review Report](final_review_report.md) - Documentation quality assessment

### 📁 Core System Directories

#### System Binaries and Libraries
- [/bin - Essential User Binaries](structure/bin.md) - Core system commands and BusyBox utilities
- [/sbin - System Administration](structure/sbin.md) - Essential system administration tools
- [/lib - System Libraries](structure/lib.md) - Shared libraries and kernel modules
- [/lib64 - 64-bit Libraries](structure/lib64.md) - Symlink to /lib for compatibility
- [/libexec - Helper Programs](structure/libexec.md) - Internal helper executables

#### User Space and Applications
- [/usr - User Programs](structure/usr.md) - User applications and Synology tools
  - Extensive /usr/syno coverage (25+ subdirectories)
  - 206 binaries in /usr/bin
  - 85 system admin tools in /usr/sbin
- [/var - Variable Data](structure/var.md) - Runtime data, logs, and caches
- [/data - Vendor Data](structure/data.md) - WiFi calibration and certificates

#### Configuration and Defaults
- [/etc - System Configuration](structure/etc.md) - Network, firewall, and service configs
- [/etc.defaults - Default Configurations](structure/etc.defaults.md) - Factory default templates
- [/var.defaults - Default Variable Data](structure/var.defaults.md) - Factory reset templates

#### Virtual Filesystems
- [/sys - Kernel Interface](structure/sys.md) - sysfs virtual filesystem
- [/dev - Device Files](structure/dev.md) - Device nodes and special files
- [/run - Runtime Data](structure/run.md) - Volatile runtime information

#### Storage and Mount Points
- [/volume1 - Main Storage](structure/volume1.md) - User data and applications
- [/mnt - Mount Points](structure/mnt.md) - Temporary mount directory
- [/lost+found - Recovery](structure/lost+found.md) - Filesystem recovery

#### Boot and Special Directories
- [/initrd - Initial RAM Disk](structure/initrd.md) - Boot initialization
- [/ini - WiFi Configuration](structure/ini.md) - Hardware initialization files
- [/root - Root Home](structure/root.md) - Root user directory

### 📦 Software Packages
- [Package Documentation Index](packages/index.md) - Analysis of installed software packages
  - Safe Access - Parental control and web filtering solution
  - Additional system packages (pending documentation)

### 🔧 Key Components Quick Links

#### Critical Configuration Files
- [Network Configuration](structure/etc.md#network-configuration) - `/etc/network/`
- [Firewall Rules](structure/etc.md#firewall-configuration) - `/etc/firewall/`
- [Service Definitions](structure/etc.md#upstart-services) - `/etc/init/`
- [WiFi Settings](structure/ini.md) - Hardware calibration data

#### Synology-Specific Components
- [Synology Router Manager](structure/usr.md#synology-router-manager-core) - `/usr/syno/`
- [Web Management Interface](structure/usr.md#synology-router-manager-core) - `/usr/syno/synoman/`
- [Package System](structure/usr.md#synology-router-manager-core) - `/usr/syno/synopkg/`
- [Mesh Networking](structure/usr.md#synology-router-manager-core) - `/usr/syno/etc/mesh/`

#### System Services
- [Upstart Init System](structure/etc.md#upstart-services) - Service management
- [Network Services](network_services_inventory.md) - All network daemons
- [Security Framework](structure/usr.md#security-considerations) - Security components
- [Logging System](structure/var.md#system-logs) - Centralized logging

### 🛠️ Documentation Tools
- [Validation Tools](tools/README.md) - Automated quality checks
  - [validate_docs.py](tools/validate_docs.py) - Main validation script
  - [fix_whitespace.py](tools/fix_whitespace.py) - Whitespace cleanup
  - [fix_broken_links.py](tools/fix_broken_links.py) - Link repair utility
- [CI/CD Integration](.github/workflows/validate-docs.yml) - GitHub Actions workflow

---

## Search Functionality Plan

### Requirements

Users should be able to search for:
- **Keywords**: Technical terms, component names, file paths
- **Configuration Parameters**: Settings, options, values
- **Commands**: System commands, utilities, scripts
- **Error Messages**: Troubleshooting information
- **Cross-References**: Related documentation

### Research Options

#### 1. Static Site Generators (Recommended)
**MkDocs with Material Theme**
- Built-in search using Lunr.js
- Easy setup and maintenance
- Supports offline search
- Mobile-friendly interface

**Benefits**:
- Zero configuration search
- Automatic index generation
- Syntax highlighting
- Navigation sidebar

#### 2. Client-Side Search Libraries
**Lunr.js**
- Pure JavaScript search
- No server required
- Supports fuzzy matching
- Lightweight (~8KB)

**FlexSearch**
- Faster than Lunr.js
- Better memory efficiency
- Supports partial matching
- Multi-language support

#### 3. Simple Text Search (Current)
For immediate use:
```bash
# Search all documentation
grep -r "search_term" _documentation/

# Search with context
grep -r -B2 -A2 "search_term" _documentation/

# Case-insensitive search
grep -ri "search_term" _documentation/
```

### Proposed Approach

**Phase 1 (Immediate)**: Document grep commands in README for local search

**Phase 2 (Short-term)**: Implement MkDocs with Material theme
1. Install MkDocs: `pip install mkdocs-material`
2. Create `mkdocs.yml` configuration
3. Build static site: `mkdocs build`
4. Deploy to GitHub Pages

**Phase 3 (Long-term)**: Enhanced search features
- Add search filters by category
- Implement search suggestions
- Add search analytics

### Next Steps for Implementation

1. **Select Tool**: MkDocs with Material theme (Phase 2)
2. **Configure Project**:
   ```yaml
   # mkdocs.yml
   site_name: Synology SRM Documentation
   theme:
     name: material
     features:
       - search.suggest
       - search.highlight
   ```
3. **Structure Content**: Organize markdown files for MkDocs
4. **Build Search Index**: Run `mkdocs build` to generate searchable site
5. **Test Search**: Verify all content is indexed and searchable
6. **Deploy**: Use GitHub Actions to auto-deploy on commits

---

## Maintenance Notes

### Adding New Documentation
1. Create documentation following [TEMPLATE.md](TEMPLATE.md)
2. Add entry to appropriate section in this index
3. Update [README.md](README.md) if major component
4. Run validation tools before committing
5. Submit PR following [Contributing Guidelines](CONTRIBUTING.md)

### Updating Links
- Use relative paths from `_documentation/` directory
- Verify links with `validate_docs.py`
- Update both source and target documentation

### Version Control
- Current Documentation Version: 2.0
- Last Major Update: 2025-06-23
- Validation Status: 100% template compliance

---

[↑ Back to Main Project](../README.md) | [→ Documentation Overview](README.md)