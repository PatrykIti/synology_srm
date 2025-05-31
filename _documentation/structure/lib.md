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