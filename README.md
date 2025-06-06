# Synology SRM System Backup Repository

This repository contains a backup of the Synology SRM (Synology Router Manager) operating system, originating from a Synology router. The purpose of this repository is to conduct detailed analysis, documentation, and understanding of the internal structure and operation of the SRM system.

## Directory Structure in `srm_backup/`

The `srm_backup/` directory contains key components of the Synology SRM system, organized as follows:

*   **[`bin/`](srm_backup/bin):** Contains executable files (binaries) and system scripts. These are the basic tools and programs necessary for system operation.
*   **[`data/`](srm_backup/data):** Stores application data, temporary data files, and other resources used by the system and installed packages.
*   **[`etc/`](srm_backup/etc):** This directory contains the main system configuration files. Changes to these files directly affect system behavior.
*   **[`etc.defaults/`](srm_backup/etc.defaults):** Stores default configuration files. These are templates that the system uses to restore settings or initialize new components.
*   **[`ini/`](srm_backup/ini):** Likely contains additional initialization or configuration files for specific modules.
*   **[`initrd/`](srm_backup/initrd):** Initial RAM disk image, used during the system boot process. It contains a minimal set of tools and drivers needed to load the main file system.
*   **[`lib/`](srm_backup/lib):** Shared libraries required by system programs and applications. Examples include `libapr-1.so`, `libboost_regex.so`, `libdbus-1.so`, `libicui18n.so`, `libip6tc.so`, `libkadm5clnt_mit.so`, `liblber-2.4.so`, `libpq.so`, `libsynoglusterfs-dsm.so`, `libsynoportmap.so`, `libsynowifidaemon.so`, `libsyslog-ng-3.5.5.so`, `libtalloc.so`.
*   **[`lost+found/`](srm_backup/lost+found):** A standard Linux file system directory, storing recovered file fragments after system crashes.
*   **[`mnt/`](srm_backup/mnt):** Empty mount points for temporary file systems or external devices.
*   **[`root/`](srm_backup/root):** The home directory for the `root` user, containing configuration files and scripts specific to the administrator (`.profile`, `.wget-hsts`).
*   **[`run/`](srm_backup/run):** Contains temporary files, process IDs (PID files), socket files, and other runtime data. Examples include `crond.pid`, `dhcp-server.pid`, `dnsmasq.pid`, `sshd.pid`, `synoconfd.pid`, access rule files (`access_srm_rules_v4`, `access_srm_rules_v6`), and subdirectories such as `avahi-daemon/`, `ddns/`, `httpd/`, `ipset/`, `lock/`, `ngfw/`, `samba/`, `sudo/`, `synoservice/`, `udev/`.
*   **[`sbin/`](srm_backup/sbin):** Contains system executable files, primarily for system administration.
*   **[`usr/`](srm_backup/usr):** Contains user files, including programs, libraries, and documentation used by users and applications.
*   **[`var/`](srm_backup/var):** Stores variable data such as log files, spool, temporary files, and other data that changes during system operation.
*   **[`var.defaults/`](srm_backup/var.defaults):** Default variable data, similar to `var/` but containing initial or resettable configurations. A notable element is `dynlib/securityscan/ruleDB/`, which contains security scan rules, including Python scripts for configuration verification (`DirectoryService`, `FileService`, `Malware`, `Network`, `PublicAccess`, `Security`, `SharedFolder`, `SystemCheck`, `Terminal`, `Update`, `User`).
*   **[`volume1/`](srm_backup/volume1):** Likely the mount point for the router's main storage volume, where user data and packages are stored.

## Documentation Goal

The primary goal of this repository is to create comprehensive documentation for the Synology SRM system, which will allow for:
*   Understanding the system architecture.
*   Identification of key components and their functions.
*   Analysis of security mechanisms and network configurations.
*   Facilitation of potential research or development work related to the SRM system.

Detailed documentation will be placed in the [`_documentation/`](_documentation) directory and will be divided into subdirectories corresponding to the main areas of the system.