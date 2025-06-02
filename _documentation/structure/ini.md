# Documentation for `srm_backup/ini/` Directory

The `srm_backup/ini/` directory contains INI-style configuration files, primarily related to the system's Wi-Fi hardware and general wireless parameters. These files store settings and parameters that control the behavior of Wi-Fi chipsets and modules.

The presence of files like `QCA6018.ini` and `QCN9000.ini` indicates specific configurations for Qualcomm Atheros Wi-Fi chipsets (QCA6018 and QCN9000 are known models).

## Top-Level Files

*   **`global.ini`**: Likely contains global or default Wi-Fi settings applicable across different chipsets or modules if not overridden by more specific files.
*   **`QCA6018.ini`**: Configuration file specifically for the QCA6018 Wi-Fi chipset. It would contain parameters tailored to this hardware.
*   **`QCN9000.ini`**: Configuration file specifically for the QCN9000 Wi-Fi chipset, containing parameters for this particular model.
*   **`wifi_module_param.ini`**: This file probably stores parameters for various Wi-Fi modules or features that are not tied to a single chipset model, or it could define how different Wi-Fi modules interact or are configured.

## Subdirectory: `internal/`

This subdirectory appears to hold internal or perhaps more detailed/low-level configuration variants of the INI files found in the parent `ini/` directory. The `_i` suffix might denote "internal" or an "implementation-specific" version.

*   **`internal/global_i.ini`**: An internal or implementation-specific version of the global Wi-Fi settings.
*   **`internal/QCA6018_i.ini`**: An internal or implementation-specific configuration for the QCA6018 chipset.
*   **`internal/QCN9000_i.ini`**: An internal or implementation-specific configuration for the QCN9000 chipset.

These internal files might be used by specific drivers or low-level system components, potentially overriding or supplementing the settings in the corresponding top-level INI files.