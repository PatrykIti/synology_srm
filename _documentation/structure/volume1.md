# /volume1/

The `/volume1/` directory on a Synology SRM (Synology Router Manager) device typically represents the primary storage volume. This is where user data, application data, package configurations, and potentially data from connected USB drives (if treated as part of `volume1`) are stored.

In the context of an `srm_backup`, this directory holds the backed-up state of this primary storage volume.

## Key Contents of `/volume1/`

Based on the provided file listing, the key top-level contents of `srm_backup/volume1/` are:

*   [`srm-backup-fixed.tar.gz`](#srm-backup-fixedtargz)
*   [`@appstore/`](#appstore)
*   [`@db/`](#db)
*   [`@tmp/`](#tmp)
*   [`lost+found/`](#lostfound)

---

### `srm-backup-fixed.tar.gz`

*   **Path:** `srm_backup/volume1/srm-backup-fixed.tar.gz`
*   **Type:** File
*   **Probable Purpose:** This appears to be a main archive file, possibly containing a consolidated backup of the entire SRM system or a significant portion of its configuration and data. Its presence at the root of `/volume1/` in a backup context suggests it might be the primary artifact of the backup process itself, or a manually created archive. Further investigation by extracting its contents would be needed to determine its exact role.

---

### `@appstore/`

*   **Path:** `srm_backup/volume1/@appstore/`
*   **Type:** Directory
*   **Probable Purpose:** This directory is standard on Synology devices for storing data and configuration files for applications (packages) installed from the Package Center.

#### `@appstore/SafeAccess/`

*   **Path:** `srm_backup/volume1/@appstore/SafeAccess/`
*   **Type:** Directory
*   **Probable Purpose:** Contains all data related to the "Safe Access" package, which provides parental controls, web filtering, and security features.
    *   **`block_page/`**: Contains assets (HTML, CSS, images, CGI scripts) for various block pages displayed to users when access is restricted due to:
        *   `blocktime/`: Time-based blocking.
        *   `security/`: Security threats (e.g., malware, phishing).
        *   `timequota/`: Time quota limits reached.
        *   `webfilter/`: Web filter categories.
    *   **`lib/`**: Contains shared libraries (`.so` files) specific to the Safe Access package, such as `libsynoparentalcontrol.so.1.3.1`, `libsynosafeaccess-notify.so.5.2`, and `libsynosafebrowsing.so.5.2`. These likely handle core functionalities like access control, notifications, and safe browsing lookups. It also includes libraries from PcapPlusPlus (`libpcppcommon++.so`, `libpcpppacket++.so`, `libpcpppcap++.so`), suggesting network packet analysis capabilities.
    *   **`report_ui/`**: Contains files for generating and displaying Safe Access reports (HTML, CSS, JavaScript, images).
    *   **`scripts/`**: Contains various shell scripts (`.sh`) used for managing Safe Access services, updating databases (e.g., `ipblock_update_db_hook.sh`, `safebrowsing_update_db_hook.sh`), handling IP/DNS changes, and managing firewall rules (`dnsfilter-iptables.sh`).
    *   **`webapi/`**: Contains libraries and configuration for Safe Access Web APIs, allowing programmatic interaction with its features. Includes legacy API definitions.

---

### `@db/`

*   **Path:** `srm_backup/volume1/@db/`
*   **Type:** Directory
*   **Probable Purpose:** This directory appears to be a central location for various databases used by the SRM system and its packages.

#### `@db/var/db/`

*   **Path:** `srm_backup/volume1/@db/var/db/`
*   **Type:** Directory
*   **Probable Purpose:** A subdirectory within `@db/` that houses the actual database files.
    *   **`geoip-database/`**: Contains GeoIP databases (e.g., `GeoIP.dat`, `GeoLite2-City.mmdb`, `GeoLite2-Country.mmdb`) used for mapping IP addresses to geographical locations. The `xt_geoip/` subdirectory contains numerous `.iv4` and `.iv6` files, likely pre-compiled IP address ranges for specific countries used by the `xt_geoip` netfilter module for efficient country-based IP blocking.
    *   **`libsynooui/oui.db`**: An OUI (Organizationally Unique Identifier) database, used to identify the manufacturer of network devices based on their MAC addresses.
    *   **`safebrowsing-database/prefix.db`**: Database for the Safe Browsing feature, likely containing prefixes of known malicious URLs.
    *   **`sudo/lectured/pciechanski_admin`**: Records when the user `pciechanski_admin` was last shown the `sudo` lecture (a warning about using `sudo` responsibly).
    *   **`syno-device-identity-database/dhcpFingerPrints`**: Database for device identification based on DHCP fingerprints.
    *   **`syno-doh-server-lists/server_lists.db`**: Database of DNS-over-HTTPS (DoH) server lists.
    *   **`syno-domain-lists/category_database.db`**: Database of domain categories, likely used by web filtering features.
    *   **`syno-ip-blocklist/`**: Contains IP blocklists, including `blocklist` (custom user-defined blocklist), `blocklist_enable_map` (mapping enabled blocklists), and `firehol_level*.netset` (pre-defined blocklists from FireHOL).
    *   **`synotps-database/custom_signature.json`**: Custom signatures for the Threat Prevention System (TPS).
    *   **`@db/var/lib/data_update/`**: Contains version information for updatable data components like `syno-doh-server-lists` and `synotps-database`.

---

### `@tmp/`

*   **Path:** `srm_backup/volume1/@tmp/`
*   **Type:** Directory
*   **Probable Purpose:** Stores temporary files for the system or applications running on `/volume1/`.

#### `@tmp/pkglist.tmp/`

*   **Path:** `srm_backup/volume1/@tmp/pkglist.tmp/`
*   **Type:** Directory
*   **Probable Purpose:** Contains temporary files related to package management, specifically icons for available packages like `DNSServer`, `DownloadStation`, `MediaServer`, and `RadiusServer`. These are likely cached during Package Center operations.

---

### `lost+found/`

*   **Path:** `srm_backup/volume1/lost+found/`
*   **Type:** Directory
*   **Probable Purpose:** This is a standard directory used by `ext2/3/4` file systems. When the file system checker (`fsck`) finds orphaned or corrupted files (data blocks not associated with any file name), it places them in this directory. In a backup context, its presence is normal, but it's typically empty unless a file system recovery event occurred prior to the backup.