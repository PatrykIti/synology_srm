# /root Directory

[← Back to Documentation Index](../README.md) | [← Previous: /mnt](mnt.md) | [→ Next: /run](run.md)

---
---

## Overview
The `/root` directory in Synology SRM is the home directory for the `root` user. It is not intended for interactive use but serves as a configuration and state storage location for system-level processes, primarily related to shell environment setup and the secure update mechanism. Its minimal contents reflect the appliance-based design of SRM, prioritizing security and stability over user customization at the root level.

## Directory Structure
```
/root/
├── .gnupg/
│   ├── pubring.kbx
│   └── trustdb.gpg
├── .profile
└── .wget-hsts
```

## Key Components

### Shell Environment
- **Purpose**: Defines the root user's shell environment.
- **Location**: `/root/.profile`
- **Dependencies**: The `ash` shell (default for root).
- **Configuration**: Sets the `PATH` variable, aliases, and a custom prompt.
- **Security**: The `PATH` is configured to prioritize standard system binaries over Synology-specific or locally installed binaries, which is a secure default.

### Update Transport Security
- **Purpose**: Caches HTTP Strict Transport Security (HSTS) policies for system update domains, forcing clients to use secure HTTPS connections. This is not a static configuration file but a stateful cache populated by `wget` after its first successful HTTPS connection to the specified domains.
- **Location**: `/root/.wget-hsts`
- **Dependencies**: System processes using `wget` for updates (e.g., the SRM update checker).
- **Configuration**: Populated automatically by `wget`. Contains entries for Synology update servers with a long `max-age`.
- **Security**: Mitigates downgrade attacks and SSL stripping during the system update process.

### Package Authenticity
- **Purpose**: Stores the GPG keyring used to verify the authenticity and integrity of downloaded SRM firmware and package updates.
- **Location**: `/root/.gnupg/`
- **Dependencies**: The system's package management and update services.
- **Configuration**: Contains Synology's public GPG key.
- **Security**: Ensures that only officially signed packages from Synology can be installed, preventing tampering and malicious software installation.

## Configuration Files

### .profile
This file configures the root user's shell session.

```sh
# .profile

# PATH
PATH=/sbin:/bin:/usr/sbin:/usr/bin:/usr/syno/sbin:/usr/syno/bin:/usr/local/sbin:/usr/local/bin
export PATH

# See if we are running in linuxrc.syno
if [ "$SYNOLINUXRC" = "1" ]; then
    # running in linuxrc.syno
    PS1='linuxrc#'
else
    # not running in linuxrc.syno
    PS1='`hostname`> '
fi

# Alias
alias dir="ls -l"
alias ll="ls -la"
```

**Analysis**:
- **`PATH` Variable**: The `PATH` is set to `/sbin:/bin:/usr/sbin:/usr/bin:/usr/syno/sbin:/usr/syno/bin:/usr/local/sbin:/usr/local/bin`. This ordering ensures that standard, core Linux binaries are found before Synology's custom binaries (`/usr/syno/bin`) and any locally installed binaries (`/usr/local/bin`). This provides a predictable and secure execution environment, reducing the risk of `PATH` manipulation attacks.
- **`SYNOLINUXRC` Check**: The script checks for an environment variable `SYNOLINUXRC`. This indicates the shell is running in a special context, likely during the early boot process (`linuxrc.syno`), and adjusts the prompt accordingly. This highlights an integration with the system's startup sequence.
- **Aliases**: Standard convenience aliases (`dir`, `ll`) are defined for `ls`.

## Scripts and Executables

**Intentionally Blank.**

The `/root` directory does not contain any executable scripts by default. This is a deliberate security choice ("security by absence") to minimize the attack surface. Placing scripts here is strongly discouraged as it deviates from the system's design and they may be removed by firmware updates.

## Integration Points

### Secure Update Workflow
The files within `/root` are critical components of SRM's end-to-end secure update workflow. They work together to ensure both the transport and the payload of system updates are secure.

1.  **Initiation**: A system process, likely using a tool like `wget`, initiates a connection to a Synology update server (e.g., `update.synology.com`).
2.  **Transport Security (HSTS)**: The server responds with an HSTS header. `wget` caches this policy in `/root/.wget-hsts`. On all subsequent connections, `wget` will enforce a secure HTTPS connection, preventing an attacker from downgrading the connection to plaintext HTTP (SSL stripping).
3.  **Payload Integrity (GPG Signature)**: The downloaded update package or manifest is cryptographically signed by Synology.
4.  **Authenticity Verification (GPG Keyring)**: The update mechanism uses the GPG keyring located at `/root/.gnupg/pubring.kbx` to verify the signature on the downloaded file. This keyring contains Synology's trusted public key. A valid signature confirms the package is authentic (it truly came from Synology) and has not been tampered with in transit.

This multi-layered process provides robust protection against man-in-the-middle (MITM) attacks and the installation of malicious firmware.

## Security Considerations

### Appliance Model & Security by Absence
The minimal nature of the `/root` directory is a key feature of SRM's security posture. It treats the device as a sealed appliance, not a general-purpose Linux server.
-   **Pro**: By not including user scripts, cron jobs, SSH `authorized_keys`, or other common configuration files, the potential for misconfiguration or persistent threats in the root account's home directory is drastically reduced.
-   **Con/Implication**: This model is not designed for advanced administrator customization. Adding files (like an `authorized_keys` file for passwordless SSH) deviates from the intended security model and is not guaranteed to persist across firmware updates.

### GPG Trust Anchor
The entire package verification process relies on the integrity of the GPG public key stored in `/root/.gnupg/pubring.kbx`. This file acts as the ultimate root of trust for all system software.

It is possible to inspect the key to verify its fingerprint:
```bash
# Note: This command must be run on the device itself.
$ gpg --no-default-keyring --keyring /root/.gnupg/pubring.kbx --list-keys
```
**Operational Note:** It is recommended to periodically re-run this command, especially after a major firmware update, to verify that the trusted key has not changed unexpectedly. Any change to the key fingerprint should be cross-referenced with official Synology security advisories.

## Network Services

**Intentionally Blank.**

The `/root` directory itself does not configure or expose any network services. Its contents are used to support client-side operations (like `wget`) initiated by other system processes.

## Performance Considerations

### Resource Usage
- **Disk Space**: Minimal (~1MB)
- **Memory**: No runtime memory usage
- **CPU**: No CPU usage
- **I/O**: Minimal - only during updates

### Performance Impact
- **System Updates**: GPG verification overhead
- **HTTPS Connections**: HSTS cache improves speed
- **Shell Startup**: .profile parsing negligible
- **Security Operations**: GPG operations when needed

### Optimization Notes
- GPG keyring kept minimal
- HSTS cache reduces SSL handshakes
- Profile kept simple for fast login
- No user customization overhead

## Maintenance Notes

-   **Do Not Modify**: The contents of the `/root` directory should be considered system-managed and should not be modified.
-   **No Persistence Guarantee**: Any manual additions or modifications to this directory (e.g., adding scripts, SSH keys, or custom profile settings) are not guaranteed to survive a firmware update and may be overwritten. Such changes can also lead to unforeseen security vulnerabilities by deviating from the tested, default state of the appliance.

## Cross-References
- System binaries: [/sbin/](sbin.md) and [/bin/](bin.md)
- Synology binaries: [/usr/syno/](usr.md)
- Update system: [/usr/syno/bin/](usr.md#synology-specific-tools)
- GPG tools: [/usr/bin/gpg](usr.md#user-binaries)
- Configuration defaults: [/etc.defaults/](etc.defaults.md)
- System logs: [/var/log/](var.md#system-logs)

---

[← Back to Documentation Index](../README.md) | [← Previous: /mnt](mnt.md) | [→ Next: /run](run.md)