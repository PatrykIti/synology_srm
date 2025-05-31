# Katalog `srm_backup/lib/`

Katalog `srm_backup/lib/` w systemie Synology SRM pełni kluczową rolę w przechowywaniu bibliotek współdzielonych (shared libraries) oraz modułów jądra, które są niezbędne do prawidłowego funkcjonowania systemu operacyjnego i zainstalowanych aplikacji. Biblioteki te dostarczają reużywalny kod dla różnych programów, co pozwala na zmniejszenie rozmiaru plików wykonywalnych i efektywniejsze zarządzanie pamięcią.

## Ogólne przeznaczenie

Głównym celem katalogu `/lib` (i jego odpowiednika w backupie `srm_backup/lib/`) jest centralne repozytorium dla:

*   **Bibliotek współdzielonych (`.so`):** Są to pliki zawierające skompilowany kod funkcji, z których mogą korzystać różne programy jednocześnie. Przykłady to standardowe biblioteki C ([`libc.so`](srm_backup/lib/libc.so.6:0)), biblioteki do obsługi wątków ([`libpthread.so`](srm_backup/lib/libpthread.so.0:0)), biblioteki kryptograficzne ([`libcrypto.so`](srm_backup/lib/libcrypto.so.1.1:0)), sieciowe ([`libcurl.so`](srm_backup/lib/libcurl.so.4.7.0:0)) i wiele innych specyficznych dla Synology ([`libsynocore.so`](srm_backup/lib/libsynocore.so:0)).
*   **Modułów jądra (w podkatalogu `modules/`):** Są to fragmenty kodu, które mogą być dynamicznie ładowane i usuwane z jądra systemu operacyjnego, rozszerzając jego funkcjonalność. Dotyczy to np. sterowników sprzętowych, obsługi systemów plików czy protokołów sieciowych.
*   **Firmware (często w podkatalogu `firmware/`):** Pliki firmware dla różnych komponentów sprzętowych.
*   **Innych plików systemowych:** Mogą tu również znajdować się inne pliki pomocnicze związane z bibliotekami lub konfiguracją systemu.

## Struktura podkatalogów i zawartość

Na podstawie listingu katalogu `srm_backup/lib/` można wyróżnić następujące kluczowe elementy:

### 1. Biblioteki współdzielone bezpośrednio w `srm_backup/lib/`

Bezpośrednio w tym katalogu znajduje się wiele plików `.so`, które są fundamentalnymi bibliotekami systemowymi oraz bibliotekami specyficznymi dla Synology. Poniżej kilka przykładów z ich prawdopodobnymi rolami:

*   **`ld.so.1`**: Dynamiczny linker/ładowarka, odpowiedzialny za ładowanie bibliotek współdzielonych do pamięci podczas uruchamiania programów.
*   **`libcrypt.so.1`**: Biblioteka do obsługi funkcji kryptograficznych, np. hashowania haseł.
*   **`libcrypto.so.1.1`**: Część pakietu OpenSSL, dostarcza szeroki zakres algorytmów kryptograficznych.
*   **`libcurl.so.4.7.0`**: Biblioteka do transferu danych z użyciem różnych protokołów sieciowych (HTTP, FTP, itp.).
*   **`libdl.so.2`**: Biblioteka do dynamicznego ładowania bibliotek (interfejs do `dlopen()`, `dlsym()`).
*   **`libm.so.6`**: Biblioteka matematyczna.
*   **`libpam.so.0.83.1`**: Pluggable Authentication Modules - biblioteka do obsługi uwierzytelniania.
*   **`libpthread.so.0`** (prawdopodobnie dowiązanie do `libpthread-X.Y.Z.so`): Biblioteka do obsługi wątków POSIX.
*   **`librt.so.1`**: Biblioteka czasu rzeczywistego POSIX.
*   **`libsqlite3.so.0.8.6`**: Biblioteka do obsługi bazy danych SQLite.
*   **`libssl.so.1.1`** (nieobecna na liście, ale spodziewana obok `libcrypto.so.1.1`): Część pakietu OpenSSL, obsługa protokołów SSL/TLS.
*   **`libstdc++.so.6`**: Standardowa biblioteka C++.
*   **Biblioteki `libsyno*`**: Duża grupa bibliotek specyficznych dla Synology, np.:
    *   `libsynocore.so` (nieobecna na liście, ale spodziewana): Podstawowe funkcje systemowe Synology.
    *   `libsynobackup.so.1`: Funkcje związane z backupem.
    *   `libsynocgi.so.5`: Obsługa interfejsów CGI.
    *   `libsynofirewall.so.1.1`: Funkcje związane z firewallem.
    *   `libsynolog.so.1`: Obsługa logowania systemowego.
    *   `libsynomesh.so.5.2`: Funkcje związane z siecią mesh Wi-Fi.
    *   `libsynorouter.so`: Funkcje specyficzne dla routera.
    *   `libsynoutils.so.1`: Różne narzędzia i funkcje pomocnicze Synology.

### 2. Kluczowe podkatalogi

*   **`modules/`**: Zawiera moduły jądra.
*   **`firmware/`**: Prawdopodobnie zawiera pliki firmware dla różnych urządzeń.
*   **`samba/`**: Biblioteki i pliki konfiguracyjne związane z serwerem Samba (udostępnianie plików i drukarek w sieci Windows).
*   **`php/`**: Moduły i rozszerzenia dla interpretera PHP.
*   **`python2.7/`**: Standardowe biblioteki i moduły dla Pythona w wersji 2.7.
*   **`openvpn/`**: Pliki związane z OpenVPN.
*   **`httpd/`**: Moduły dla serwera HTTP (prawdopodobnie Apache).
*   **`iptables/`**: Rozszerzenia i biblioteki dla `iptables` (firewall).
*   **`security/`**: Moduły PAM (`.so`) używane do uwierzytelniania.
*   **`udev/`**: Reguły i pliki pomocnicze dla `udev` (zarządzanie urządzeniami w systemie Linux).
*   **`ebtables/`**: Narzędzia i biblioteki do filtrowania ramek Ethernet.
*   **`gconv/`**: Moduły konwersji kodowania znaków dla `glibc`.
*   **`locale/`**: Pliki lokalizacyjne (językowe) dla aplikacji.

W kolejnych sekcjach zostaną opisane bardziej szczegółowo wybrane podkatalogi.
### 3. Podkatalog `modules/` (Moduły Jądra)

Podkatalog `srm_backup/lib/modules/` zawiera moduły jądra systemu Linux (`.ko` - Kernel Object). W odróżnieniu od typowej struktury, gdzie moduły są zorganizowane w podkatalogach odpowiadających wersji jądra (np. `4.4.60/kernel/`), w tym przypadku wszystkie moduły znajdują się bezpośrednio w `srm_backup/lib/modules/`.

Moduły te rozszerzają funkcjonalność jądra o obsługę specyficznego sprzętu, systemów plików, protokołów sieciowych itp. Poniżej przykładowe kategorie modułów znalezione w tym katalogu wraz z reprezentatywnymi plikami i ich prawdopodobnym przeznaczeniem:

*   **Moduły sieciowe (Netfilter, QoS, VPN, etc.):**
    *   `xt_geoip.ko`: Moduł Netfilter do filtrowania ruchu na podstawie geolokalizacji IP.
    *   `xt_limit.ko`: Moduł Netfilter do ograniczania liczby połączeń.
    *   `xt_mac.ko`: Moduł Netfilter do filtrowania na podstawie adresu MAC.
    *   `sch_htb.ko`: Moduł QoS (Quality of Service) do hierarchicznego zarządzania pasmem.
    *   `gre.ko`, `ip6_tunnel.ko`, `l2tp_ppp.ko`, `pppoe.ko`, `pptp.ko`: Moduły do obsługi różnych protokołów tunelowania i VPN.
    *   `nat46.ko`: Moduł do translacji adresów sieciowych między IPv4 a IPv6.
    *   `nf_conntrack_*.ko`, `nf_nat_*.ko`: Moduły Netfilter do śledzenia połączeń i NAT dla różnych protokołów (np. PPTP, SIP).
*   **Moduły związane z Wi-Fi i sprzętem Qualcomm Atheros (QCA):**
    *   `cfg80211.ko`: Podstawowa konfiguracja Wi-Fi dla Linuksa.
    *   `umac.ko`, `qdf.ko`, `qca_ol.ko`, `qca_spectral.ko`, `ath_pktlog.ko`: Prawdopodobnie sterowniki i moduły pomocnicze dla chipsetów Wi-Fi Qualcomm Atheros.
    *   `qca-nss-drv.ko` i inne `qca-nss-*.ko`: Moduły związane z Network Subsystem (NSS) firmy Qualcomm, służące do akceleracji sprzętowej operacji sieciowych.
    *   `shortcut-fe.ko`, `shortcut-fe-ipv6.ko`: Moduły "Shortcut Forwarding Engine", prawdopodobnie do przyspieszania przekazywania pakietów.
    *   `wifi_2_0.ko`, `wifi_3_0.ko`: Prawdopodobnie główne moduły sterowników Wi-Fi.
*   **Moduły systemów plików:**
    *   `vfat.ko`, `fat.ko`: Obsługa systemów plików FAT/VFAT.
    *   `hfsplus.ko`: Obsługa systemu plików HFS+ (używanego przez Apple).
    *   `ecryptfs.ko`: Obsługa szyfrowanego systemu plików eCryptfs.
*   **Moduły USB:**
    *   `usbnet.ko`: Sterownik dla urządzeń USB działających jako karty sieciowe.
    *   `usbserial.ko`: Ogólny sterownik dla urządzeń szeregowych USB.
    *   `cdc-acm.ko`, `cdc_ether.ko`, `cdc_ncm.ko`: Moduły dla urządzeń USB klasy CDC (Communication Device Class).
    *   `usblp.ko`: Sterownik dla drukarek USB.
*   **Moduły kryptograficzne:**
    *   `cryptodev.ko`: Interfejs do sprzętowych i programowych sterowników kryptograficznych.
    *   `ocf.ko` (OpenBSD Cryptographic Framework): Framework dla operacji kryptograficznych.
    *   `qca-nss-cfi-cryptoapi.ko`: Moduł integrujący akcelerację kryptograficzną NSS z CryptoAPI Linuksa.
*   **Moduły specyficzne dla Synology:**
    *   `synobios.ko`: Prawdopodobnie moduł związany z interakcją z BIOS/firmware systemu.
    *   `synoxtmac.ko`: Może być związany z obsługą specyficznych funkcji sieciowych lub sprzętowych Synology.
    *   `syno_port_event.ko`: Moduł do obsługi zdarzeń portów.
*   **Inne:**
    *   `bonding.ko`: Agregacja interfejsów sieciowych.
    *   `loop.ko`: Obsługa urządzeń pętli zwrotnej (loop devices).
    *   `tun.ko`: Obsługa wirtualnych interfejsów sieciowych TUN/TAP.

Liczba i rodzaj modułów wskazują na zaawansowane funkcje sieciowe routera, w tym obsługę różnych protokołów VPN, QoS, akcelerację sprzętową operacji sieciowych oraz wsparcie dla specyficznych chipsetów Wi-Fi.
### 4. Podkatalog `firmware/`

Podkatalog `srm_backup/lib/firmware/` przechowuje pliki firmware, które są niezbędne do działania różnych komponentów sprzętowych routera. Na podstawie listingu można zidentyfikować:

*   **Pliki `.bin` bezpośrednio w `firmware/`:**
    *   `ifpp.bin`, `ipue.bin`, `ofpp.bin`, `opue.bin`: Mogą to być pliki firmware dla specyficznych mikrokontrolerów lub procesorów sygnałowych.
    *   `qca-nss0.bin`: Plik firmware dla jednostki Qualcomm Atheros Network Subsystem (NSS), odpowiedzialnej za akcelerację sprzętową operacji sieciowych.

*   **Podkatalogi specyficzne dla chipsetów Qualcomm:**
    *   **`IPQ6018/`**: Ten podkatalog prawdopodobnie zawiera firmware specyficzny dla chipsetu Qualcomm IPQ6018, który jest popularnym SoC (System-on-Chip) używanym w routerach Wi-Fi 6. Można się spodziewać, że wewnątrz znajdują się pliki `.bin` dla różnych komponentów tego SoC (np. rdzeni CPU, kontrolera Wi-Fi, jednostki NSS).
    *   **`qcn9000/`**: Ten podkatalog prawdopodobnie zawiera firmware dla chipsetu Qualcomm QCN9000, który jest używany w zaawansowanych rozwiązaniach Wi-Fi 6 i Wi-Fi 6E. Podobnie jak w przypadku `IPQ6018/`, można oczekiwać plików `.bin` dla tego konkretnego chipsetu.

Zawartość tego katalogu jest kluczowa dla inicjalizacji i poprawnego działania sprzętu sieciowego routera, w szczególności modułów Wi-Fi i funkcji akceleracji sieciowej.
### 5. Inne istotne podkatalogi

Oprócz `modules/` i `firmware/`, katalog `srm_backup/lib/` zawiera wiele innych podkatalogów, które przechowują biblioteki i pliki konfiguracyjne dla różnych usług i aplikacji systemowych. Poniżej krótki opis niektórych z nich:

*   **`samba/`**: Zawiera biblioteki współdzielone (`.so`) oraz prawdopodobnie pliki konfiguracyjne dla serwera Samba, który implementuje protokół SMB/CIFS, umożliwiając udostępnianie plików i drukarek w sieciach Windows.
*   **`php/`**: Prawdopodobnie zawiera moduły i rozszerzenia dla interpretera PHP, używanego przez interfejs webowy routera lub inne aplikacje webowe.
*   **`python2.7/`**: Zawiera standardowe biblioteki i moduły dla interpretera Python w wersji 2.7, który może być używany przez różne skrypty systemowe lub aplikacje.
*   **`httpd/`**: Moduły dla serwera HTTP (prawdopodobnie Apache lub jego pochodna, np. `lighttpd`), który obsługuje interfejs zarządzania routerem.
*   **`iptables/`**: Rozszerzenia i biblioteki dla `iptables`, narzędzia do konfiguracji firewalla w systemie Linux.
*   **`security/`**: Zawiera moduły PAM (Pluggable Authentication Modules, pliki `.so`), które są używane przez system do uwierzytelniania użytkowników i usług.
*   **`udev/`**: Reguły (`.rules`) i programy pomocnicze dla systemu `udev`, który dynamicznie zarządza plikami urządzeń w katalogu `/dev` w odpowiedzi na zdarzenia jądra (np. podłączenie urządzenia USB).
*   **`cups/`**: Pliki związane z Common UNIX Printing System, jeśli router obsługuje funkcje serwera wydruku.
*   **`ebtables/`**: Narzędzia i biblioteki do filtrowania na poziomie mostu sieciowego (Ethernet bridge filtering).
*   **`gconv/`**: Moduły konwersji kodowania znaków używane przez bibliotekę `glibc`.
*   **`locale/`**: Pliki danych lokalizacyjnych (tłumaczenia, formaty daty/czasu itp.) dla różnych języków.
*   **`openvpn/`**: Pliki związane z klientem lub serwerem OpenVPN.
*   **`postgresql/`**: Biblioteki klienckie lub inne komponenty związane z bazą danych PostgreSQL, jeśli jest używana przez system.
*   **`pppd/`**: Pliki związane z demonem PPP (Point-to-Point Protocol), używanym m.in. do połączeń PPPoE.
*   **`rsync/`**: Pliki związane z narzędziem `rsync` do synchronizacji plików.
*   **`sasl2/`**: Biblioteki SASL (Simple Authentication and Security Layer) używane do uwierzytelniania w różnych protokołach sieciowych.
*   **`syslog-ng/`**: Pliki konfiguracyjne i moduły dla zaawansowanego demona logowania `syslog-ng`.
*   **`ulogd/`**: Demon do logowania pakietów z Netfilter.
*   **`vfs/`**: Moduły VFS (Virtual File System) dla Samby, rozszerzające jej możliwości.
*   **`wifi/`**: Dodatkowe pliki konfiguracyjne lub skrypty związane z Wi-Fi, które nie są bezpośrednio modułami jądra ani firmware.

Ta lista nie jest wyczerpująca, ale pokazuje różnorodność komponentów systemowych, których biblioteki i pliki pomocnicze znajdują się w `srm_backup/lib/`. Dokładna analiza każdego z tych podkatalogów wykraczałaby poza zakres tego dokumentu, ale ich obecność świadczy o bogatej funkcjonalności systemu SRM.