# `/sbin` - System Binaries

The `/sbin` directory in a Unix-like system, including Synology SRM, contains essential system administration binaries. These are typically executables required for booting, restoring, recovering, and/or repairing the system, in addition to other critical system-level tasks. Access to these commands is usually restricted to the root user.

This directory is flat, meaning it does not contain subdirectories in this specific backup.

## Files and Their Probable Purpose

Below is a list of files found in `srm_backup/sbin/` along with their likely functions in the context of a Synology SRM device:

*   **`badblocks`**: Used to search for bad blocks on a disk device. Essential for disk health diagnostics.
*   **`debugfs`**: A file system debugger for ext2, ext3, and ext4 file systems. Allows for low-level interaction with file system structures.
*   **`dhcpcd`**: A DHCP client daemon. Manages network interface configuration via DHCP.
*   **`e2fsck`**: Used to check and repair Linux ext2/ext3/ext4 file systems. Crucial for file system integrity.
*   **`ebtables`**: A tool for administering Ethernet bridge frame filtering rules. Part of network traffic control at the link layer.
*   **`ebtables-restore`**: Restores ebtables rules from a file.
*   **`ebtables-save`**: Saves ebtables rules to a file.
*   **`eject`**: Ejects removable media (like CD-ROMs or USB drives). Its presence might be for broader Linux compatibility or specific hardware features.
*   **`fsck.hfsplus`**: File system consistency check and interactive repair tool for HFS+ file systems. Likely included for compatibility with Apple devices or external drives.
*   **`fstrim`**: Discards unused blocks on a mounted filesystem. Useful for SSDs to maintain performance.
*   **`init`**: The first process started during booting of the system (PID 1). It is responsible for starting up all other processes.
*   **`initctl`**: A utility to communicate and control the init daemon (e.g., Upstart).
*   **`ip`**: A versatile utility for IP address, network interface, and routing configuration. Part of the `iproute2` suite, replacing older tools like `ifconfig` and `route`.
*   **`iwconfig`**: Used to configure wireless network interfaces.
*   **`iwlist`**: Displays detailed wireless information from a wireless interface.
*   **`iwpriv`**: Allows manipulation of wireless extensions private ioctls. Used for advanced wireless card configuration.
*   **`mkdosfs`**: Creates an MS-DOS (FAT) file system.
*   **`mke2fs`**: Creates an ext2, ext3, or ext4 filesystem.
*   **`parted`**: A program for creating and manipulating partition tables.
*   **`quota`**: Displays disk usage and limits for users or groups.
*   **`quotacheck`**: Scans a filesystem for disk usage, and creates or updates quota files.
*   **`quotaon`**: Turns filesystem quotas on and off.
*   **`raidtool`**: A utility for managing software RAID configurations. Synology devices heavily rely on RAID.
*   **`reboot`**: Reboots the system.
*   **`repquota`**: Summarizes quotas for a filesystem.
*   **`resize2fs`**: Resizes ext2, ext3, or ext4 file systems.
*   **`rpcbind`**: Maps RPC (Remote Procedure Call) program numbers to network port numbers. Essential for services like NFS.
*   **`rpcinfo`**: Reports RPC information.
*   **`runlevel`**: Reports the current and previous system runlevel.
*   **`setquota`**: Sets disk quotas for users or groups.
*   **`shutdown`**: Shuts down the system.
*   **`sparted`**: A screen-oriented version of `parted` (though less common, its presence might indicate specific Synology tools or legacy).
*   **`sysctl`**: Configures kernel parameters at runtime.
*   **`tc`**: Traffic Control utility. Used for configuring advanced network traffic shaping, policing, and scheduling.
*   **`telinit`**: An alias or link to `init`, used to change runlevels.
*   **`tune2fs`**: Adjusts tunable filesystem parameters on ext2/ext3/ext4 filesystems.

**Note:** The exact behavior and relevance of these commands can sometimes be specific to Synology's customized Linux environment (SRM). Some might be standard Linux utilities, while others could be linked to or part of Synology's proprietary management software. The absence of suffixes like `*` (executable) or `@` (symlink) in the provided list means these are likely actual binary files, but their permissions and link status would need to be verified on a live system for definitive confirmation.