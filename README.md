# Synology SRM System Backup Repository

To repozytorium zawiera backup systemu operacyjnego Synology SRM (Synology Router Manager), pochodzący z routera Synology. Celem tego repozytorium jest szczegółowa analiza, dokumentacja oraz zrozumienie wewnętrznej struktury i działania systemu SRM.

## Struktura Katalogów w `srm_backup/`

Katalog `srm_backup/` zawiera kluczowe komponenty systemu Synology SRM, zorganizowane w następujący sposób:

*   **[`bin/`](srm_backup/bin):** Zawiera pliki wykonywalne (binarne) oraz skrypty systemowe. Są to podstawowe narzędzia i programy niezbędne do działania systemu.
*   **[`data/`](srm_backup/data):** Przechowuje dane aplikacji, tymczasowe pliki danych oraz inne zasoby wykorzystywane przez system i zainstalowane pakiety.
*   **[`etc/`](srm_backup/etc):** Katalog ten zawiera główne pliki konfiguracyjne systemu. Zmiany w tych plikach bezpośrednio wpływają na zachowanie systemu.
*   **[`etc.defaults/`](srm_backup/etc.defaults):** Przechowuje domyślne pliki konfiguracyjne. Są to szablony, które system wykorzystuje do przywracania ustawień lub inicjalizacji nowych komponentów.
*   **[`ini/`](srm_backup/ini):** Prawdopodobnie zawiera dodatkowe pliki inicjalizacyjne lub konfiguracyjne dla specyficznych modułów.
*   **[`initrd/`](srm_backup/initrd):** Obraz początkowego ramdysku, używany podczas procesu bootowania systemu. Zawiera minimalny zestaw narzędzi i sterowników potrzebnych do załadowania głównego systemu plików.
*   **[`lib/`](srm_backup/lib):** Biblioteki współdzielone (shared libraries) wymagane przez programy systemowe i aplikacje. Przykłady to `libapr-1.so`, `libboost_regex.so`, `libdbus-1.so`, `libicui18n.so`, `libip6tc.so`, `libkadm5clnt_mit.so`, `liblber-2.4.so`, `libpq.so`, `libsynoglusterfs-dsm.so`, `libsynoportmap.so`, `libsynowifidaemon.so`, `libsyslog-ng-3.5.5.so`, `libtalloc.so`.
*   **[`lost+found/`](srm_backup/lost+found):** Standardowy katalog systemu plików Linux, przechowujący odzyskane fragmenty plików po awariach systemu.
*   **[`mnt/`](srm_backup/mnt):** Puste punkty montowania dla tymczasowych systemów plików lub urządzeń zewnętrznych.
*   **[`root/`](srm_backup/root):** Katalog domowy użytkownika `root`, zawierający pliki konfiguracyjne i skrypty specyficzne dla administratora (`.profile`, `.wget-hsts`).
*   **[`run/`](srm_backup/run):** Zawiera pliki tymczasowe, identyfikatory procesów (PID files), pliki socket oraz inne dane runtime. Przykłady to `crond.pid`, `dhcp-server.pid`, `dnsmasq.pid`, `sshd.pid`, `synoconfd.pid`, pliki reguł dostępu (`access_srm_rules_v4`, `access_srm_rules_v6`), oraz podkatalogi takie jak `avahi-daemon/`, `ddns/`, `httpd/`, `ipset/`, `lock/`, `ngfw/`, `samba/`, `sudo/`, `synoservice/`, `udev/`.
*   **[`sbin/`](srm_backup/sbin):** Zawiera systemowe pliki wykonywalne, przeznaczone głównie do zarządzania systemem przez administratora.
*   **[`usr/`](srm_backup/usr):** Zawiera pliki użytkowe, w tym programy, biblioteki i dokumentację, z których korzystają użytkownicy i aplikacje.
*   **[`var/`](srm_backup/var):** Przechowuje zmienne dane, takie jak pliki logów, spool, pliki tymczasowe oraz inne dane, które zmieniają się w czasie działania systemu.
*   **[`var.defaults/`](srm_backup/var.defaults):** Domyślne zmienne dane, podobne do `var/` ale zawierające początkowe lub resetowalne konfiguracje. Wyróżniającym się elementem jest `dynlib/securityscan/ruleDB/`, który zawiera reguły skanowania bezpieczeństwa, w tym skrypty Pythona do weryfikacji konfiguracji (`DirectoryService`, `FileService`, `Malware`, `Network`, `PublicAccess`, `Security`, `SharedFolder`, `SystemCheck`, `Terminal`, `Update`, `User`).
*   **[`volume1/`](srm_backup/volume1):** Prawdopodobnie punkt montowania dla głównego woluminu pamięci routera, gdzie przechowywane są dane użytkownika i pakiety.

## Cel Dokumentacji

Głównym celem tego repozytorium jest stworzenie kompleksowej dokumentacji systemu Synology SRM, która pozwoli na:
*   Zrozumienie architektury systemu.
*   Identyfikację kluczowych komponentów i ich funkcji.
*   Analizę mechanizmów bezpieczeństwa i konfiguracji sieciowych.
*   Ułatwienie ewentualnych prac badawczych lub rozwojowych związanych z systemem SRM.

Szczegółowa dokumentacja zostanie umieszczona w katalogu [`_documentation/`](_documentation) i będzie podzielona na podkatalogi odpowiadające głównym obszarom systemu.