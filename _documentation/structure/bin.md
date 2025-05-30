# Struktura katalogu `srm_backup/bin/`

Ten plik zawiera szczegółową analizę zawartości katalogu `srm_backup/bin/`, wraz z opisem przeznaczenia każdego pliku i podkatalogu.

## Zawartość katalogu `srm_backup/bin/ `

Poniżej znajduje się lista plików i podkatalogów znalezionych w `srm_backup/bin/` wraz z ich prawdopodobnym przeznaczeniem w systemie Synology SRM. Znak `@` na końcu nazwy pliku wskazuje na dowiązanie symboliczne (symbolic link), co oznacza, że plik jest w rzeczywistości linkiem do innego pliku, często znajdującego się w `busybox`.

*   **`ash@`**
    *   **Prawdopodobne przeznaczenie:** Dowiązanie symboliczne do interpretera poleceń (shell), prawdopodobnie do `busybox`. `ash` (Almquist shell) to lekki shell, często używany w systemach wbudowanych. Służy do wykonywania skryptów shellowych i interaktywnej pracy w wierszu poleceń.

*   **`busybox*`**
    *   **Prawdopodobne przeznaczenie:** Jest to pojedynczy plik wykonywalny, który łączy w sobie wiele popularnych narzędzi UNIX-owych (takich jak `ls`, `cp`, `mv`, `grep`, `tar` itp.). W systemie Synology SRM, BusyBox jest często używany do zapewnienia podstawowych funkcji systemowych i narzędzi w środowiskach z ograniczonymi zasobami, minimalizując rozmiar systemu operacyjnego. Służy jako uniwersalne narzędzie do wykonywania wielu podstawowych operacji systemowych. Gwiazdka `*` oznacza, że jest to plik wykonywalny.

*   **`cat@`**
    *   **Prawdopodobne przeznaczenie:** Dowiązanie symboliczne do `busybox`. Narzędzie `cat` służy do wyświetlania zawartości plików tekstowych na standardowe wyjście, łączenia plików oraz tworzenia nowych plików.

*   **`catv@`**
    *   **Prawdopodobne przeznaczenie:** Prawdopodobnie dowiązanie symboliczne do `busybox` lub specjalizowana wersja `cat`. Może służyć do wyświetlania zawartości plików z wizualizacją znaków niedrukowalnych.

*   **`chgrp@`**
    *   **Prawdopodobne przeznaczenie:** Dowiązanie symboliczne do `busybox`. Narzędzie `chgrp` służy do zmiany grupy właściciela plików lub katalogów.

*   **`chmod@`**
    *   **Prawdopodobne przeznaczenie:** Dowiązanie symboliczne do `busybox`. Narzędzie `chmod` służy do zmiany uprawnień dostępu do plików lub katalogów.

*   **`chown@`**
    *   **Prawdopodobne przeznaczenie:** Dowiązanie symboliczne do `busybox`. Narzędzie `chown` służy do zmiany właściciela plików lub katalogów.

*   **`cp@`**
    *   **Prawdopodobne przeznaczenie:** Dowiązanie symboliczne do `busybox`. Narzędzie `cp` służy do kopiowania plików i katalogów.

*   **`date@`**
    *   **Prawdopodobne przeznaczenie:** Dowiązanie symboliczne do `busybox`. Narzędzie `date` służy do wyświetlania lub ustawiania daty i czasu systemowego.

*   **`dd@`**
    *   **Prawdopodobne przeznaczenie:** Dowiązanie symboliczne do `busybox`. Narzędzie `dd` służy do konwersji i kopiowania plików na niskim poziomie, często używane do tworzenia obrazów dysków lub kopiowania danych blok po bloku.

*   **`df@`**
    *   **Prawdopodobne przeznaczenie:** Dowiązanie symboliczne do `busybox`. Narzędzie `df` służy do wyświetlania informacji o zajętości przestrzeni dyskowej w systemie plików.

*   **`dmesg@`**
    *   **Prawdopodobne przeznaczenie:** Dowiązanie symboliczne do `busybox`. Narzędzie `dmesg` służy do wyświetlania komunikatów z bufora jądra systemu, co jest przydatne do diagnostyki sprzętu i sterowników.

*   **`dnsdomainname@`**
    *   **Prawdopodobne przeznaczenie:** Dowiązanie symboliczne do `busybox`. Narzędzie `dnsdomainname` służy do wyświetlania nazwy domeny DNS systemu.

*   **`echo@`**
    *   **Prawdopodobne przeznaczenie:** Dowiązanie symboliczne do `busybox`. Narzędzie `echo` służy do wyświetlania tekstu lub zmiennych na standardowe wyjście.

*   **`egrep@`**
    *   **Prawdopodobne przeznaczenie:** Dowiązanie symboliczne do `busybox`. Narzędzie `egrep` jest wersją `grep` obsługującą rozszerzone wyrażenia regularne. Służy do wyszukiwania wzorców w plikach.

*   **`false@`**
    *   **Prawdopodobne przeznaczenie:** Dowiązanie symboliczne do `busybox`. Narzędzie `false` zawsze zwraca status wyjścia niezerowy (błąd), używane w skryptach shellowych do warunkowego sterowania przepływem.

*   **`fgrep@`**
    *   **Prawdopodobne przeznaczenie:** Dowiązanie symboliczne do `busybox`. Narzędzie `fgrep` jest wersją `grep` do wyszukiwania stałych ciągów znaków (bez wyrażeń regularnych).

*   **`get_key_value@`**
    *   **Prawdopodobne przeznaczenie:** Prawdopodobnie dowiązanie symboliczne do `busybox` lub niestandardowe narzędzie Synology. Może służyć do odczytywania wartości z plików konfiguracyjnych w formacie klucz-wartość.

*   **`getopt@`**
    *   **Prawdopodobne przeznaczenie:** Dowiązanie symboliczne do `busybox`. Narzędzie `getopt` służy do parsowania opcji wiersza poleceń, ułatwiając pisanie skryptów shellowych z obsługą argumentów.

*   **`grep@`**
    *   **Prawdopodobne przeznaczenie:** Dowiązanie symboliczne do `busybox`. Narzędzie `grep` służy do wyszukiwania wzorców (tekstu) w plikach.

*   **`gunzip@`**
    *   **Prawdopodobne przeznaczenie:** Dowiązanie symboliczne do `busybox`. Narzędzie `gunzip` służy do dekompresji plików skompresowanych za pomocą `gzip`.

*   **`gzip@`**
    *   **Prawdopodobne przeznaczenie:** Dowiązanie symboliczne do `busybox`. Narzędzie `gzip` służy do kompresji plików.

*   **`hostname@`**
    *   **Prawdopodobne przeznaczenie:** Dowiązanie symboliczne do `busybox`. Narzędzie `hostname` służy do wyświetlania lub ustawiania nazwy hosta systemu.

*   **`ip*`**
    *   **Prawdopodobne przeznaczenie:** Standardowe narzędzie w systemach Linux do zarządzania i konfiguracji interfejsów sieciowych, routingiem, politykami routingu, tunelami itp. W Synology SRM będzie używany do zarządzania siecią urządzenia, konfiguracji adresów IP, tras sieciowych i innych parametrów związanych z łącznością. Gwiazdka `*` oznacza, że jest to plik wykonywalny.

*   **`ipcalc@`**
    *   **Prawdopodobne przeznaczenie:** Dowiązanie symboliczne do `busybox` lub narzędzie do obliczeń związanych z adresacją IP (np. maska podsieci, adres sieci, adres rozgłoszeniowy). Może być używane do walidacji lub generowania konfiguracji sieciowych.

*   **`jq*`**
    *   **Prawdopodobne przeznaczenie:** Lekki i elastyczny procesor JSON w wierszu poleceń. W Synology SRM może być używany do parsowania, filtrowania i manipulowania danymi JSON, które są często wykorzystywane w konfiguracjach, logach, danych zwracanych przez API systemowe lub do interakcji z usługami webowymi. Gwiazdka `*` oznacza, że jest to plik wykonywalny.

*   **`kill@`**
    *   **Prawdopodobne przeznaczenie:** Dowiązanie symboliczne do `busybox`. Narzędzie `kill` służy do wysyłania sygnałów do procesów, najczęściej w celu ich zakończenia.

*   **`killps@`**
    *   **Prawdopodobne przeznaczenie:** Prawdopodobnie dowiązanie symboliczne do `busybox` lub niestandardowe narzędzie Synology. Może być skryptem lub aliasem ułatwiającym zabijanie procesów, np. wszystkich procesów o danej nazwie.

*   **`ln@`**
    *   **Prawdopodobne przeznaczenie:** Dowiązanie symboliczne do `busybox`. Narzędzie `ln` służy do tworzenia dowiązań (linków) do plików.

*   **`login@`**
    *   **Prawdopodobne przeznaczenie:** Dowiązanie symboliczne do `busybox`. Narzędzie `login` służy do logowania użytkowników do systemu.

*   **`ls@`**
    *   **Prawdopodobne przeznaczenie:** Dowiązanie symboliczne do `busybox`. Narzędzie `ls` służy do listowania zawartości katalogów.

*   **`mkdir@`**
    *   **Prawdopodobne przeznaczenie:** Dowiązanie symboliczne do `busybox`. Narzędzie `mkdir` służy do tworzenia katalogów.

*   **`mknod@`**
    *   **Prawdopodobne przeznaczenie:** Dowiązanie symboliczne do `busybox`. Narzędzie `mknod` służy do tworzenia specjalnych plików (np. urządzeń blokowych, znakowych, potoków nazwanych).

*   **`more@`**
    *   **Prawdopodobne przeznaczenie:** Dowiązanie symboliczne do `busybox`. Narzędzie `more` służy do paginacji zawartości plików tekstowych, umożliwiając przeglądanie ich strona po stronie.

*   **`mount@`**
    *   **Prawdopodobne przeznaczenie:** Dowiązanie symboliczne do `busybox`. Narzędzie `mount` służy do montowania systemów plików (np. dysków, partycji).

*   **`mv@`**
    *   **Prawdopodobne przeznaczenie:** Dowiązanie symboliczne do `busybox`. Narzędzie `mv` służy do przenoszenia lub zmiany nazwy plików i katalogów.

*   **`netstat@`**
    *   **Prawdopodobne przeznaczenie:** Dowiązanie symboliczne do `busybox`. Narzędzie `netstat` służy do wyświetlania połączeń sieciowych, tablic routingu, statystyk interfejsów itp.

*   **`nice@`**
    *   **Prawdopodobne przeznaczenie:** Dowiązanie symboliczne do `busybox`. Narzędzie `nice` służy do uruchamiania programów ze zmienionym priorytetem, wpływając na ich harmonogramowanie przez jądro.

*   **`ntfs-3g*`**
    *   **Prawdopodobne przeznaczenie:** Jest to sterownik i zestaw narzędzi do odczytu i zapisu na partycjach systemu plików NTFS (New Technology File System), używanego głównie w systemach Windows. W Synology SRM, `ntfs-3g` jest kluczowy do obsługi zewnętrznych dysków twardych sformatowanych w NTFS, umożliwiając odczyt i zapis danych z tych dysków. Gwiazdka `*` oznacza, że jest to plik wykonywalny.

*   **`ntfs-3g.probe*`**
    *   **Prawdopodobne przeznaczenie:** Narzędzie pomocnicze dla `ntfs-3g`, używane do sondowania (probe) partycji i wykrywania, czy są one sformatowane jako NTFS. Prawdopodobnie używane do automatycznego montowania lub sprawdzania integralności dysków NTFS podłączanych do urządzenia Synology SRM. Gwiazdka `*` oznacza, że jest to plik wykonywalny.

*   **`pidof@`**
    *   **Prawdopodobne przeznaczenie:** Dowiązanie symboliczne do `busybox`. Narzędzie `pidof` służy do znajdowania PID (Process ID) uruchomionych programów.

*   **`ping@`**
    *   **Prawdopodobne przeznaczenie:** Dowiązanie symboliczne do `busybox`. Narzędzie `ping` służy do sprawdzania łączności sieciowej z hostem.

*   **`ping6@`**
    *   **Prawdopodobne przeznaczenie:** Dowiązanie symboliczne do `busybox`. Wersja `ping` dla protokołu IPv6.

*   **`proxy*`**
    *   **Prawdopodobne przeznaczenie:** Nazwa wskazuje, że może to być plik wykonywalny związany z serwerem proxy lub narzędziem do zarządzania połączeniami sieciowymi. W kontekście Synology SRM, może być używany do obsługi przekierowywania portów, serwera proxy dla usług sieciowych (np. Web Proxy, Reverse Proxy), lub innych funkcji związanych z pośredniczeniem w ruchu sieciowym w celu zwiększenia bezpieczeństwa lub optymalizacji dostępu do zasobów. Gwiazdka `*` oznacza, że jest to plik wykonywalny.

*   **`ps@`**
    *   **Prawdopodobne przeznaczenie:** Dowiązanie symboliczne do `busybox`. Narzędzie `ps` służy do wyświetlania informacji o aktualnie uruchomionych procesach.

*   **`pwd@`**
    *   **Prawdopodobne przeznaczenie:** Dowiązanie symboliczne do `busybox`. Narzędzie `pwd` służy do wyświetlania bieżącego katalogu roboczego.

*   **`rm@`**
    *   **Prawdopodobne przeznaczenie:** Dowiązanie symboliczne do `busybox`. Narzędzie `rm` służy do usuwania plików i katalogów.

*   **`rmdir@`**
    *   **Prawdopodobne przeznaczenie:** Dowiązanie symboliczne do `busybox`. Narzędzie `rmdir` służy do usuwania pustych katalogów.

*   **`run-parts@`**
    *   **Prawdopodobne przeznaczenie:** Dowiązanie symboliczne do `busybox`. Narzędzie `run-parts` służy do wykonywania skryptów w katalogu. Często używane do zarządzania skryptami startowymi lub cronem.

*   **`sed@`**
    *   **Prawdopodobne przeznaczenie:** Dowiązanie symboliczne do `busybox`. Narzędzie `sed` (Stream Editor) służy do filtrowania i transformowania tekstu.

*   **`sh@`**
    *   **Prawdopodobne przeznaczenie:** Dowiązanie symboliczne do `busybox`. Jest to kolejny interpreter poleceń (shell), często symboliczny link do `ash` lub `bash`.

*   **`sleep@`**
    *   **Prawdopodobne przeznaczenie:** Dowiązanie symboliczne do `busybox`. Narzędzie `sleep` służy do wstrzymywania wykonania na określony czas.

*   **`stat@`**
    *   **Prawdopodobne przeznaczenie:** Dowiązanie symboliczne do `busybox`. Narzędzie `stat` służy do wyświetlania szczegółowych informacji o pliku lub systemie plików (np. rozmiar, uprawnienia, daty modyfikacji).

*   **`stty@`**
    *   **Prawdopodobne przeznaczenie:** Dowiązanie symboliczne do `busybox`. Narzędzie `stty` służy do ustawiania i wyświetlania opcji terminala.

*   **`su@`**
    *   **Prawdopodobne przeznaczenie:** Dowiązanie symboliczne do `busybox`. Narzędzie `su` (substitute user) służy do zmiany identyfikatora użytkownika podczas sesji.

*   **`sync@`**
    *   **Prawdopodobne przeznaczenie:** Dowiązanie symboliczne do `busybox`. Narzędzie `sync` służy do wymuszania zapisu buforowanych danych na dysk.

*   **`tar@`**
    *   **Prawdopodobne przeznaczenie:** Dowiązanie symboliczne do `busybox`. Narzędzie `tar` służy do archiwizowania i dearchiwizowania plików.

*   **`touch@`**
    *   **Prawdopodobne przeznaczenie:** Dowiązanie symboliczne do `busybox`. Narzędzie `touch` służy do zmiany daty ostatniego dostępu/modyfikacji pliku lub tworzenia pustych plików.

*   **`true@`**
    *   **Prawdopodobne przeznaczenie:** Dowiązanie symboliczne do `busybox`. Narzędzie `true` zawsze zwraca status wyjścia zero (sukces), używane w skryptach shellowych do warunkowego sterowania przepływem.

*   **`umount@`**
    *   **Prawdopodobne przeznaczenie:** Dowiązanie symboliczne do `busybox`. Narzędzie `umount` służy do odmontowywania systemów plików.

*   **`uname@`**
    *   **Prawdopodobne przeznaczenie:** Dowiązanie symboliczne do `busybox`. Narzędzie `uname` służy do wyświetlania informacji o systemie operacyjnym (np. nazwa jądra, wersja).

*   **`usleep@`**
    *   **Prawdopodobne przeznaczenie:** Dowiązanie symboliczne do `busybox`. Narzędzie `usleep` służy do wstrzymywania wykonania na określoną liczbę mikrosekund.

*   **`vi@`**
    *   **Prawdopodobne przeznaczenie:** Dowiązanie symboliczne do `busybox`. Jest to prosty edytor tekstu w trybie terminala, często używany do szybkiej edycji plików konfiguracyjnych lub skryptów.

*   **`zcat@`**
    *   **Prawdopodobne przeznaczenie:** Dowiązanie symboliczne do `busybox`. Narzędzie `zcat` służy do wyświetlania zawartości skompresowanych plików (np. `.gz`) bez konieczności ich wcześniejszej dekompresji.