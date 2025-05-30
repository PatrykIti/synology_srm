# Plan Analizy i Dokumentacji Systemu Synology SRM

Ten dokument przedstawia szczegółowy plan analizy i dokumentacji systemu Synology SRM, którego backup znajduje się w katalogu `srm_backup/`. Celem jest stworzenie kompleksowej bazy wiedzy o strukturze, funkcjonalności i konfiguracji systemu.

## Faza 1: Ogólna Analiza i Struktura

*   **Task 1.1: Przegląd Głównych Katalogów**
    *   **Opis:** Dokładna analiza zawartości każdego z głównych katalogów w `srm_backup/` (np. `bin/`, `data/`, `etc/`, `lib/`, `run/`, `var/`, `var.defaults/`, `usr/`).
    *   **Cel:** Zrozumienie ogólnego przeznaczenia każdego katalogu i identyfikacja kluczowych podkatalogów/plików.
    *   **Wynik:** Utworzenie plików `_documentation/structure/bin.md`, `_documentation/structure/data.md`, `_documentation/structure/etc.md`, `_documentation/structure/lib.md`, `_documentation/structure/run.md`, `_documentation/structure/var.md`, `_documentation/structure/var_defaults.md`, `_documentation/structure/usr.md` z ogólnym opisem.

*   **Task 1.2: Analiza Plików Konfiguracyjnych (etc/)**
    *   **Opis:** Szczegółowy przegląd plików w katalogach `etc/` i `etc.defaults/`. Zwrócenie uwagi na formaty plików (np. `.conf`, `.ini`, skrypty shellowe) i ich wzajemne zależności.
    *   **Cel:** Zrozumienie, jak system jest konfigurowany i jakie są domyślne ustawienia.
    *   **Wynik:** Rozszerzenie `_documentation/structure/etc.md` o sekcje dotyczące kluczowych plików konfiguracyjnych.

## Faza 2: Komponenty Systemowe i Usługi

*   **Task 2.1: Analiza Plików Binarnych i Skryptów (bin/, sbin/)**
    *   **Opis:** Identyfikacja ważnych plików wykonywalnych i skryptów w `bin/` i `sbin/`. Próba określenia ich funkcji na podstawie nazw i ewentualnie nagłówków plików (jeśli to możliwe bez uruchamiania).
    *   **Cel:** Zrozumienie podstawowych narzędzi systemowych i procesów.
    *   **Wynik:** Utworzenie `_documentation/components/binaries.md` i `_documentation/components/scripts.md` z opisem zidentyfikowanych plików.

*   **Task 2.2: Analiza Bibliotek (lib/)**
    *   **Opis:** Przegląd bibliotek w `lib/`. Identyfikacja znanych bibliotek (np. `libapr`, `libdbus`, `libpq`) i próba określenia, do czego są używane w kontekście SRM.
    *   **Cel:** Zrozumienie zależności oprogramowania i wykorzystywanych technologii.
    *   **Wynik:** Utworzenie `_documentation/components/libraries.md`.

*   **Task 2.3: Analiza Procesów Działających (run/)**
    *   **Opis:** Przegląd plików PID i innych plików runtime w `run/`. Identyfikacja usług systemowych (np. `crond`, `dhcp-server`, `dnsmasq`, `sshd`, `synoconfd`).
    *   **Cel:** Zrozumienie, jakie usługi działają w systemie i jak są zarządzane.
    *   **Wynik:** Utworzenie `_documentation/services/running_processes.md`.

## Faza 3: Bezpieczeństwo i Sieć

*   **Task 3.1: Analiza Reguł Sieciowych (run/access_srm_rules_v4/v6, run/isolate_rules_v4/v6, run/ipset/)**
    *   **Opis:** Szczegółowa analiza plików zawierających reguły firewalla i konfiguracje IPSet. Zrozumienie, jak router zarządza dostępem, izolacją i NAT.
    *   **Cel:** Zrozumienie mechanizmów bezpieczeństwa sieciowego i routingu.
    *   **Wynik:** Utworzenie `_documentation/security/network_rules.md`.

*   **Task 3.2: Analiza Skanowania Bezpieczeństwa (var.defaults/dynlib/securityscan/)**
    *   **Opis:** Przegląd skryptów Pythona w `var.defaults/dynlib/securityscan/ruleDB/`. Analiza, jakie aspekty bezpieczeństwa są sprawdzane (np. hasła, konfiguracja FTP, ustawienia DSM, firewall).
    *   **Cel:** Zrozumienie wbudowanych funkcji bezpieczeństwa i audytu.
    *   **Wynik:** Utworzenie `_documentation/security/security_scan.md` z opisem poszczególnych modułów skanowania.

## Faza 4: Dalsza Analiza i Szczegóły

*   **Task 4.1: Analiza Logów i Danych Zmiennych (var/)**
    *   **Opis:** Przegląd typowych lokalizacji logów i innych zmiennych danych w katalogu `var/`.
    *   **Cel:** Zrozumienie, gdzie system przechowuje informacje o swoim działaniu i błędach.
    *   **Wynik:** Utworzenie `_documentation/data/logs_and_runtime.md`.

*   **Task 4.2: Analiza Woluminów (volume1/)**
    *   **Opis:** Jeśli `volume1/` zawiera dane, analiza ich struktury i zawartości (np. zainstalowane pakiety, dane użytkownika).
    *   **Cel:** Zrozumienie, jak dane są przechowywane na głównym woluminie.
    *   **Wynik:** Utworzenie `_documentation/data/volume_structure.md`.

*   **Task 4.3: Wzorce Systemowe i Dobre Praktyki**
    *   **Opis:** Na podstawie zebranych informacji, identyfikacja powtarzających się wzorców w organizacji plików, skryptów i konfiguracji.
    *   **Cel:** Zrozumienie filozofii projektowej Synology SRM.
    *   **Wynik:** Aktualizacja `memory-bank/systemPatterns.md` o zidentyfikowane wzorce.

## Faza 5: Synteza i Utrzymanie

*   **Task 5.1: Konsolidacja Dokumentacji**
    *   **Opis:** Upewnienie się, że wszystkie zebrane informacje są spójne i dobrze zorganizowane w katalogu `_documentation/`.
    *   **Cel:** Stworzenie kompletnej i użytecznej dokumentacji.

*   **Task 5.2: Aktualizacja Banku Pamięci**
    *   **Opis:** Regularne aktualizowanie plików w `memory-bank/` (szczególnie `activeContext.md`, `progress.md`, `decisionLog.md`) w miarę postępów w analizie.
    *   **Cel:** Utrzymanie aktualnego kontekstu projektu.