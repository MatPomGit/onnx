<!--
Copyright (c) ONNX Project Contributors

SPDX-License-Identifier: Apache-2.0
-->

# Twoja pierwsza kontrybuacja do ONNX - Kompleksowy przewodnik dla studentów

## 🎓 Dla kogo jest ten przewodnik?

Ten dokument został stworzony z myślą o studentach i osobach, które po raz pierwszy stykają się z:
- Projektami open source
- Systemem kontroli wersji Git i GitHub
- Pracą w międzynarodowym zespole programistów
- Standardami jakości kodu w dużych projektach

Nie zakładamy żadnej wcześniejszej wiedzy - wszystko wyjaśnimy krok po kroku!

## 📚 Co powinieneś wiedzieć przed startem

### Wymagana wiedza minimalna:
1. **Python na poziomie podstawowym** - rozumiesz funkcje, klasy, moduły
2. **Podstawy terminala/konsoli** - potrafisz nawigować między katalogami, uruchamiać komendy
3. **Git w zakresie podstawowym** - commit, push, pull (nauczymy Cię reszty!)

### Przydatna (ale niewymagana) wiedza:
- Znajomość C++ (tylko jeśli chcesz modyfikować rdzeń biblioteki)
- Doświadczenie z machine learning
- Protokoły bufory (Protocol Buffers)

## 🌟 7 Różnych sposobów jak możesz pomóc

### Opcja 1: Uczestnictwo w dyskusjach (Poziom: Początkujący ⭐)

**Co robisz:** Obserwujesz, czytasz i bierzesz udział w rozmowach społeczności.

**Gdzie:**
- Grupy SIG (Special Interest Groups) - [zobacz listę](community/sigs.md)
- Grupy robocze - [zobacz aktywne grupy](community/working-groups.md)
- [Dyskusje techniczne na GitHub](https://github.com/onnx/onnx/discussions)
- Kanały Slack w LF AI and Data

**Jak zacząć:**
1. Wybierz temat, który Cię interesuje (np. optymalizacja, bezpieczeństwo, nowe operatory)
2. Dołącz do odpowiedniej grupy
3. Słuchaj i ucz się przez pierwsze spotkania
4. Zadawaj pytania - nie ma głupich pytań!
5. Pomagaj odpowiadać innym początkującym

**Czas potrzebny:** 1-2 godziny tygodniowo

### Opcja 2: Tworzenie przypadków użycia i narzędzi (Poziom: Średniozaawansowany ⭐⭐)

**Co robisz:** Pokazujesz praktyczne zastosowania ONNX.

**Przykładowe aktywności:**
- Napisz skrypt konwertujący model z frameworka X do ONNX
- Stwórz tutorial pokazujący konkretne zastosowanie
- Przedstaw ONNX na uniwersyteckich spotkaniach lub hackathonach
- Opublikuj case study z własnego projektu

**Jak zacząć:**
1. Zidentyfikuj problem, który możesz rozwiązać z ONNX
2. Stwórz proof-of-concept
3. Udokumentuj swoje rozwiązanie
4. Podziel się z społecznością przez blog lub prezentację

**Czas potrzebny:** Projekt weekendowy lub dłuższy

### Opcja 3: Implementacja funkcji z planu rozwoju (Poziom: Zaawansowany ⭐⭐⭐)

**Co robisz:** Aktywnie kodujesz nowe możliwości.

**Jak zacząć:**
1. Przeczytaj [dokument roadmap](https://github.com/onnx/steering-committee/tree/main/roadmap)
2. Znajdź funkcję oznaczoną jako "help wanted" lub "good first issue"
3. Zgłoś się w Issue, że chcesz nad tym popracować
4. Współpracuj z maintainerami nad implementacją
5. Dąż do statusu committer - osoby z prawami do zatwierdzania zmian

**Czas potrzebny:** Kilka tygodni na większą funkcję

### Opcja 4: Wzbogacanie Model Zoo (Poziom: Średniozaawansowany ⭐⭐)

**Co robisz:** Dodajesz nowe modele do publicznej kolekcji.

**Wymagania:**
- Model musi być w formacie ONNX
- Powinien demonstrować konkretną funkcjonalność
- Musi zawierać dokumentację i przykłady użycia
- Licencja musi pozwalać na publiczne udostępnienie

**Proces:**
1. Wytrenuj lub przekonwertuj model
2. Przetestuj go dokładnie
3. Przygotuj dokumentację
4. Zgłoś PR do repozytorium models

**Czas potrzebny:** Zależnie od złożoności modelu

### Opcja 5: Publikacje naukowe i edukacyjne (Poziom: Każdy ⭐)

**Co robisz:** Piszesz o ONNX i jego zastosowaniach.

**Formaty:**
- Artykuły na arXiv (jeśli prowadzisz badania)
- Posty na blogu technicznym
- Tutoriale wideo na YouTube
- Książki lub e-booki
- Prezentacje na konferencjach studenckich

**Dlaczego to ważne:** Zwiększa adopcję ONNX i pomaga innym się uczyć.

**Czas potrzebny:** Zależnie od formatu - od kilku godzin do miesięcy

### Opcja 6: Testy i zgłaszanie błędów (Poziom: Początkujący ⭐)

**Co robisz:** Używasz ONNX i zgłaszasz problemy, które napotkasz.

**Jak skutecznie zgłaszać błędy:**
1. Sprawdź, czy problem nie został już zgłoszony
2. Przygotuj minimalny przykład, który powoduje błąd
3. Opisz:
   - Jakie kroki wykonałeś
   - Co się stało (otrzymany błąd)
   - Czego się spodziewałeś
   - Twoje środowisko (wersja ONNX, Python, system operacyjny)
4. Użyj odpowiednich etykiet (labels)

**Czas potrzebny:** 30 minut na zgłoszenie

### Opcja 7: Udział w Komitecie Sterującym (Poziom: Po wykazaniu się ⭐⭐⭐)

**Co robisz:** Pomagasz kształtować przyszłość projektu.

**Kto może:** 
- Liderzy SIG i grup roboczych
- Osoby z udokumentowanym wkładem w projekt
- Wszyscy mogą obserwować spotkania (są otwarte!)

**Proces:** Coroczne wybory, możliwość samodzielnej nominacji.

## 💻 Kontrybuowanie kodu - Szczegółowy przewodnik

### Etap 1: Propozycja nowego operatora

**Co to jest operator?** To podstawowa operacja wykonywana na danych - np. konwolucja, dodawanie, normalizacja.

**Zanim zaproponujesz nowy operator:**
1. Przeczytaj **dokładnie** [tutorial dodawania operatora](docs/AddNewOp.md)
2. Sprawdź, czy operator już nie istnieje
3. Przygotuj uzasadnienie - dlaczego jest potrzebny?
4. Przedstaw przypadki użycia
5. Rozważ, czy nie można użyć kombinacji istniejących operatorów

**Proces zatwierdzania:**
- Dyskusja w odpowiedniej grupie SIG
- Przegląd przez maintainerów
- Implementacja prototypu
- Testy i dokumentacja
- Finalne zatwierdzenie

### Etap 2: Przygotowanie środowiska programistycznego

**Krok A: Instalacja narzędzi**

Zainstaluj następujące narzędzia (jeśli jeszcze ich nie masz):
```bash
# Menedżer pakietów Python
python -m pip install --upgrade pip

# Narzędzie do testowania
pip install pytest

# Narzędzie do sprawdzania stylu kodu
pip install lintrunner lintrunner-adapters
lintrunner init
```

**Krok B: Budowanie ONNX ze źródeł**

Szczegółowe instrukcje znajdziesz w [INSTALL.md](https://github.com/onnx/onnx/blob/main/INSTALL.md#build-onnx-from-source).

Krótka wersja dla Linux/Mac:
```bash
# 1. Sklonuj repozytorium (jeśli jeszcze nie masz)
git clone https://github.com/onnx/onnx.git
cd onnx

# 2. Pobierz submoduły
git submodule update --init --recursive

# 3. Zainstaluj w trybie deweloperskim
pip install -e . -v
```

**Co oznacza flaga `-e`?** 
To "editable mode" - twoje zmiany w kodzie Python będą widoczne natychmiast, bez reinstalacji!

**Co oznacza flaga `-v`?**
"Verbose" - pokazuje szczegółowe informacje o procesie instalacji, przydatne do debugowania.

### Etap 3: Zrozumienie struktury projektu

```
onnx/
├── onnx/                    # Główny katalog z kodem
│   ├── onnx.proto          # Definicje struktur danych (Protocol Buffers)
│   ├── checker.py          # Walidacja poprawności modeli
│   ├── shape_inference.py  # Wnioskowanie wymiarów tensorów
│   ├── version_converter.py # Konwersja między wersjami
│   ├── parser.py           # Parsowanie tekstowej reprezentacji
│   ├── hub.py              # Pobieranie modeli z Model Zoo
│   ├── compose.py          # Łączenie wielu modeli
│   ├── helper.py           # Funkcje pomocnicze
│   ├── defs/               # Definicje operatorów ONNX
│   └── test/               # Testy jednostkowe i integracyjne
├── docs/                    # Dokumentacja
├── examples/               # Przykładowe notebooki Jupyter
└── tools/                  # Narzędzia wspomagające
```

**Dla studentów - które pliki edytować:**
- **Python:** Zmiany są widoczne natychmiast (tryb `-e`)
- **C++:** Musisz przebudować projekt przez `pip install -e . -v`
- **Protobuf (*.proto):** Wymaga pełnej przebudowy

### Etap 4: Workflow zmiany kodu

**Standardowy przepływ pracy:**

```bash
# 1. Upewnij się, że jesteś na aktualnej wersji
git checkout main
git pull origin main

# 2. Stwórz nową gałąź dla swojej zmiany
git checkout -b moja-nowa-funkcja

# 3. Wprowadź zmiany w plikach

# 4. Sprawdź, co zostało zmienione
git status
git diff

# 5. Przetestuj swoje zmiany
pytest

# 6. Sprawdź styl kodu
lintrunner -a

# 7. Dodaj zmiany do commita
git add .

# 8. Stwórz commit z opisowym komunikatem
git commit -s -m "Dodaj operator XYZ dla obsługi funkcji ABC"

# 9. Wypchnij zmiany do swojego forka
git push origin moja-nowa-funkcja

# 10. Otwórz Pull Request na GitHubie
```

**Ważne: flaga `-s` w commit**
Dodaje "Signed-off-by" - potwierdzenie, że masz prawo do kontrybuowania tego kodu (wymagane przez DCO).

### Etap 5: Proces Pull Request (PR)

**Co się dzieje po wysłaniu PR:**

1. **Automatyczne testy (CI)** - Uruchamiają się na Twoim kodzie
   - Testy jednostkowe
   - Testy integracyjne  
   - Sprawdzenie stylu kodu
   - Budowanie na różnych platformach

2. **Code Review** - Ludzie przeglądają Twój kod
   - Członkowie odpowiedniej grupy [SIG](community/sigs.md) lub [grupy roboczej](community/working-groups.md)
   - Mogą poprosić o zmiany - to normalne!
   - Odpowiadaj na komentarze konstruktywnie

3. **Iteracje** - Poprawiasz kod na podstawie feedbacku
   - Wprowadź zmiany w tej samej gałęzi
   - Commit i push - PR zaktualizuje się automatycznie

4. **Zatwierdzenie i merge** - Gdy wszystko jest OK
   - Maintainer zatwierdza zmiany
   - Kod trafia do głównej gałęzi
   - Gratulacje! Jesteś kontrybutorem ONNX! 🎉

## 🎨 Standardy jakości kodu

### Style przewodnie

Używamy standardów:
- **Python:** [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- **C++:** [Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html)

**Nie musisz ich znać na pamięć!** Narzędzie `lintrunner` automatycznie sprawdzi i poprawi większość problemów.

### Automatyczne formatowanie kodu

```bash
# Sprawdź i pokaż wszystkie problemy
lintrunner

# Automatycznie napraw co się da
lintrunner -a

# Lub szybsza wersja - tylko napraw
lintrunner f

# Zobacz dostępne opcje
lintrunner --help
```

**Co robi lintrunner?**
- Sprawdza formatowanie (wcięcia, spacje, długość linii)
- Wykrywa potencjalne błędy
- Weryfikuje nazewnictwo zmiennych i funkcji
- Sprawdza dokumentację (docstrings)
- I wiele więcej!

Konfiguracja znajduje się w pliku `.lintrunner.toml` w głównym katalogu projektu.

## 🧪 Testowanie - Upewnij się, że nie zepsujesz projektu

### Testy Python (pytest)

**Podstawowe użycie:**

```bash
# Uruchom wszystkie testy
pytest

# Uruchom testy z konkretnego pliku
pytest onnx/test/test_checker.py

# Uruchom konkretny test
pytest onnx/test/test_checker.py::TestChecker::test_check_graph

# Pokaż szczegółowe wyjście (przydatne przy debugowaniu)
pytest -v

# Zatrzymaj się przy pierwszym błędzie
pytest -x
```

**Po zmianach w kodzie zawsze:**
1. Uruchom testy związane z Twoją zmianą
2. Jeśli wszystko działa, uruchom pełny zestaw testów
3. Napraw wszystkie błędy przed wysłaniem PR

### Testy C++ (googletest)

**Kiedy są potrzebne:** Gdy modyfikujesz kod C++ (rdzeń biblioteki).

**Kompilacja z testami:**
```bash
# Linux/Mac: Ustaw flagę środowiskową
export ONNX_BUILD_TESTS=1
pip install -e . -v

# Lub alternatywnie podczas instalacji
ONNX_BUILD_TESTS=1 pip install -e . -v
```

**Uruchamianie testów C++:**

Linux/Mac:
```bash
# Ustaw ścieżkę do bibliotek
export LD_LIBRARY_PATH="./.setuptools-cmake-build/:$LD_LIBRARY_PATH"

# Uruchom testy
./.setuptools-cmake-build/onnx_gtests
```

Windows:
```powershell
# Debug build
.setuptools-cmake-build\Debug\onnx_gtests.exe

# Release build  
.setuptools-cmake-build\Release\onnx_gtests.exe
```

**Co testują testy C++:**
- Wnioskowanie kształtów
- Propagacja danych
- Parser modeli
- Optymalizacje niskiego poziomu

### Aktualizacja pokrycia testów

Po dodaniu nowych testów:
```bash
python onnx/backend/test/stat_coverage.py
```

To generuje raport pokazujący, które części kodu są pokryte testami.

## 📝 Developer Certificate of Origin (DCO)

**Co to jest DCO?** To formalne potwierdzenie, że:
- Masz prawo kontrybuować swój kod
- Rozumiesz licencję projektu
- Zgadzasz się na udostępnienie kodu na tych warunkach

**Jak to działa:**

Każdy commit musi zawierać linię:
```
Signed-off-by: Twoje Imię <twoj@email.com>
```

**Automatyczne dodawanie:**
```bash
git commit -s -m "Twój komunikat commita"
```

Flaga `-s` automatycznie doda tę linię!

**Ważne:** DCO jest wymagane dla **każdego** commita, nie tylko na poziomie całego PR.

### Co jeśli zapomniałeś dodać DCO?

**Dla nowych commitów:**
```bash
# Popraw ostatni commit
git commit --amend -s --no-edit

# Wypchnij z wymuszeniem
git push -f
```

**Dla starych commitów w PR:**

Najprostszy sposób - squash wszystkiego w jeden commit:
```bash
# Przełącz się na main
git checkout main

# Stwórz tymczasową gałąź
git checkout -b temp-branch

# Scal squashując z twojej starej gałęzi
git merge --squash stara-galaz

# Usuń starą gałąź
git branch -d stara-galaz

# Stwórz nową o tej samej nazwie
git checkout -b stara-galaz

# Zrób jeden commit z DCO
git commit -s -m "Twoja opisowa wiadomość"

# Wymuś push
git push origin stara-galaz -f
```

## 🔄 Proces CI (Continuous Integration)

**Co to jest CI?** System automatycznie testujący każdą zmianę przed jej zaakceptowaniem.

**Co sprawdza CI w ONNX:**
1. Poprawność kompilacji na różnych platformach (Linux, Windows, macOS)
2. Przejście wszystkich testów
3. Styl kodu
4. Brak regresji wydajności
5. Kompatybilność wsteczna

**Gdzie sprawdzić status:**
- Na stronie twojego Pull Requesta
- [Lista workflow runs](https://github.com/onnx/onnx/actions)

**Jeśli CI się nie powiódł:**
1. Kliknij na czerwony X przy Twoim PR
2. Zobacz szczegóły błędu
3. Napraw problem lokalnie
4. Commit i push - CI uruchomi się ponownie

Szczegóły pipeline'ów CI: [docs/CIPipelines.md](docs/CIPipelines.md)

## 📖 Dodatkowe zasoby dla deweloperów

**Implementacja backend'u:**
[Jak zaimplementować backend ONNX](docs/ImplementingAnOnnxBackend.md) - jeśli chcesz stworzyć konwerter ONNX do innego formatu

**Infrastruktura testów backend:**
[Infrastruktura testów i jak dodawać testy](docs/OnnxBackendTest.md) - szczegóły systemu testowania

**Generowanie dokumentacji operatorów:**

Dokumentacja operatorów ([Operators.md](Operators.md), [Operators-ml.md](Operators-ml.md)) oraz changelogi są generowane automatycznie.

Aby odświeżyć dokumentację:
```bash
# Ustaw flagę dla ML operatorów
export ONNX_ML=1

# Zainstaluj
pip install -e . -v

# Generuj dokumentację
python onnx/defs/gen_doc.py
```

**Co się stanie:** 
- Skrypt przejrzy definicje operatorów w C++
- Wyciągnie opisy, parametry, przykłady
- Wygeneruje sformatowane pliki Markdown
- Zaktualizuje changelog

Jeśli ustawisz `ONNX_ML=0`, zaktualizują się tylko `Operators.md` i `Changelog.md` (bez ML operatorów).

## ⚖️ Licencja

[Apache License v2.0](/LICENSE) - oznacza to, że:
- Możesz używać kodu komercyjnie
- Możesz modyfikować kod
- Musisz dołączyć informację o licencji
- Musisz udokumentować znaczące zmiany

## 🤝 Kodeks postępowania

[ONNX Open Source Code of Conduct](http://onnx.ai/codeofconduct.html)

**Podstawowe zasady:**
- Bądź przyjazny i pomocny
- Szanuj różnorodność opinii
- Konstruktywna krytyka, nie osobiste ataki
- Koncentruj się na tym, co najlepsze dla społeczności

**Jeśli widzisz naruszenie:** Zgłoś maintainerom lub komitetowi sterującemu.

---

## 🎯 Podsumowanie dla początkujących

**Twoje pierwsze kroki:**

1. ⭐ Zgwiezdkuj projekt na GitHubie
2. 📖 Przeczytaj dokumentację i README
3. 🔧 Zainstaluj ONNX i przetestuj podstawowe funkcje
4. 🐛 Poszukaj Issues oznaczonych "good first issue"
5. 💬 Przedstaw się na Slack
6. 📝 Spróbuj naprawić mały błąd lub ulepszyć dokumentację
7. 🚀 Wyślij swój pierwszy Pull Request!

**Pamiętaj:** Wszyscy kiedyś byli początkującymi. Nie bój się pytać, popełniać błędów i uczyć się. Społeczność ONNX jest otwarta i pomocna!

Powodzenia w Twojej przygodzie z open source! 🎉
