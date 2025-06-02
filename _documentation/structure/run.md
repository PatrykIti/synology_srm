# `/run` Directory Documentation

## Overview

The `/run` directory in Unix-like operating systems, including Synology SRM, is a standard location for storing runtime data. This data pertains to the system's operation since its last boot and is generally volatile, meaning its contents are cleared upon system restart or shutdown.

Historically, `/var/run` served a similar purpose, but `/run` was introduced to allow `/var` to be potentially mounted later in the boot process or even reside on a separate partition. The `/run` directory is typically a `tmpfs` (temporary file system) mount, meaning it resides in RAM and is very fast but not persistent across reboots.

## Purpose in Synology SRM Backup

In the context of a Synology SRM backup (`srm_backup/run/`), the contents of this directory represent a snapshot of the runtime state of various services and system processes at the moment the backup was created. Due to its volatile nature, the data found here might be:

*   **Incomplete:** Not all runtime data might be captured if processes were actively changing files during the backup.
*   **Time-specific:** The files reflect the state at a particular point in time and might not be relevant if restoring to a system that has been running for a different duration or with different services active.
*   **Potentially empty or sparse:** If the backup was taken shortly after a reboot or if few services were active, the directory might contain very little data.

## Common File Types and Their Roles

The `srm_backup/run/` directory can contain various types of files and subdirectories, including:

*   **PID Files (`.pid`):**
    *   **Purpose:** These files store the Process ID (PID) of a running daemon or service. For example, `crond.pid` would contain the PID of the cron daemon, and `sshd.pid` would contain the PID of the SSH daemon.
    *   **Role:** They are used by system utilities and scripts to manage services (e.g., to send signals like SIGHUP for reloading configuration or SIGTERM for termination) and to ensure that only one instance of a service is running.
    *   **Examples from listing:** `crond.pid`, `dhcp-server.pid`, `dnsmasq.pid`, `sshd.pid`, `syslog-ng.pid`.

*   **Lock Files (`.lock`):**
    *   **Purpose:** Lock files are used as a synchronization mechanism to prevent multiple processes or instances of a script from concurrently accessing or modifying a shared resource.
    *   **Role:** They help avoid race conditions and data corruption. The presence of a lock file typically indicates that a resource is in use.
    *   **Examples from listing:** `device.dhcp.lock`, `syslog-ng.lock`, `data_update/config.lock`, `ipset/.ipset_lock`, `lock/dhcpserver.lock`.

*   **Sockets (Unix Domain Sockets):**
    *   **Purpose:** Sockets in `/run` are often Unix domain sockets, which provide a means of Inter-Process Communication (IPC) between processes running on the same machine.
    *   **Role:** Services use sockets to offer interfaces to other local processes without the overhead of network sockets. For example, a logging daemon might listen on a socket for log messages from other applications.
    *   *(Note: Sockets are special file types and might not be directly visible as simple files in a basic `list_files` output from a backup, but their presence is common in a live `/run` directory).*

*   **Subdirectories for Specific Services:**
    *   **Purpose:** Many services create their own subdirectories within `/run` to organize their runtime files, such as PID files, sockets, or temporary status information.
    *   **Examples from listing:**
        *   `avahi-daemon/`: For the Avahi mDNS/DNS-SD daemon (e.g., `avahi-daemon/pid`).
        *   `data_update/`: Likely related to system data update mechanisms, containing various lock files.
        *   `ipset/`: Contains files related to IP sets used by the firewall (e.g., `FIREWALL_LAN_V4`).
        *   `samba/`: For the Samba service (SMB/CIFS), containing PID files, TDB (Trivial Database) files like `gencache.tdb`, `messages.tdb`.
        *   `synodevice/`: Appears to hold runtime data for Synology's device identification and management services.
        *   `synoservice/`: Contains runtime configuration and status for various Synology services.
        *   `udev/`: Contains data related to `udev`, the device manager for the Linux kernel, reflecting detected hardware and device events.

*   **Other Status/Configuration Files:**
    *   The directory can also contain various other files indicating system state, temporary configurations, or results of operations.
    *   **Examples from listing:** `access_srm_rules_v4`, `nat_rules` (firewall/NAT rules), `checkNewDSM.unavailable`, `device.dhcp` (DHCP client lease information), `externalIP.result` (DDNS external IP), `pmk.txt` / `ptk.txt` (potentially Wi-Fi related keys), `topoinit_phase`, `topology_state` (network topology information).

## Summary of `srm_backup/run/` Contents

The provided listing for `srm_backup/run/` shows a typical collection of runtime files:

*   Numerous PID files for core system services (`crond.pid`, `dhcp-server.pid`, `dnsmasq.pid`, `inetd.pid`, `ntpd.pid`, `syslog-ng.pid`, `sshd.pid`) and Synology-specific services (`findhostd.pid`, `manutild.pid`, `scemd.pid`, `synobackupd.pid`, `synoconfd.pid`, `synonetd.pid`, etc.).
*   Various lock files ensuring exclusive access to resources (`device.dhcp.lock`, `network_policy.lock`, `syslog-ng.lock`, and many within subdirectories like `data_update/`, `lock/`, `ngfw/lock/`, `synodevice/lock/`).
*   Files related to network configuration and status, such as firewall rules (`access_srm_rules_v4`, `nat_rules`), DHCP information (`device.dhcp`), DNS (`dnsmasq.pid`), NTP (`ntpd.pid`, `ntp/ntp.drift`, `syno_ntpd_succeeded`), and network topology (`topoinit_phase`, `topology_state`).
*   Subdirectories for services like Avahi (`avahi-daemon/`), data update mechanisms (`data_update/`), IP sets (`ipset/`), Samba (`samba/`), device management (`synodevice/`), Synology services (`synoservice/`), and `udev`.

The presence of these files indicates an active system state at the time of backup, with many daemons running and network services operational. The `udev/data/` subdirectory, in particular, shows a wealth of information about detected hardware components and loaded kernel modules.

Given the nature of `/run`, these files are primarily useful for forensic analysis of the system's state at backup time rather than for direct restoration, as a live system would regenerate its own `/run` contents upon boot.