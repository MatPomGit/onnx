<!--
Copyright (c) ONNX Project Contributors

SPDX-License-Identifier: Apache-2.0
-->

# Instalacja ONNX - Kompleksowy przewodnik dla studentów

Ten dokument przedstawia różne metody instalacji ONNX. Wybierz metodę odpowiednią do twojego poziomu zaawansowania i potrzeb.

## 🎯 Która metoda jest dla Ciebie?

| Metoda | Poziom | Czas | Kiedy używać |
|--------|--------|------|--------------|
| **Oficjalne pakiety Python** | ⭐ Początkujący | 2 min | Chcesz tylko używać ONNX |
| **Pakiety vcpkg** | ⭐⭐ Średniozaawansowany | 10 min | Pracujesz z projektami C++ |
| **Pakiety Conda** | ⭐ Początkujący | 3 min | Używasz środowiska Conda |
| **Budowanie ze źródeł** | ⭐⭐⭐ Zaawansowany | 30+ min | Chcesz modyfikować kod ONNX |

## 📦 Metoda 1: Oficjalne pakiety Python (Zalecana dla studentów)

### Podstawowa instalacja

```sh
pip install onnx
```

**Co się dzieje krok po kroku:**
1. Narzędzie `pip` (Python Package Installer) łączy się z repozytorium PyPI
2. Pobiera najnowszą stabilną wersję ONNX (~60 MB)
3. Instaluje pakiet i wszystkie wymagane zależności
4. Po instalacji możesz użyć `import onnx` w swoich skryptach Python

### Instalacja z dodatkami (referencyjną implementacją)

```sh
pip install onnx[reference]
```

**Co dodatkowo otrzymujesz:**
- Referencyjną implementację wykonawcy ONNX
- Możliwość bezpośredniego uruchamiania modeli w Python
- Dodatkowe narzędzia do debugowania modeli

**Kiedy to potrzebne:** Gdy chcesz testować modele bez zewnętrznego runtime'u jak ONNX Runtime.

### Wersje eksperymentalne (dla odważnych!)

[Pakiety tygodniowe ONNX](https://pypi.org/project/onnx-weekly/) to wersje developerskie z najnowszymi funkcjami:

```sh
pip install onnx-weekly
```

**⚠️ Ostrzeżenie:** 
- Mogą zawierać niestabilny kod
- Nie używaj w projektach produkcyjnych
- Idealne do testowania nowych funkcji i zgłaszania błędów

## 🔧 Metoda 2: Pakiety vcpkg (dla projektów C++)

**Co to jest vcpkg?** To menedżer pakietów dla bibliotek C/C++ stworzony przez Microsoft.

**Dlaczego vcpkg:** Jeśli piszesz aplikację w C++ i chcesz używać ONNX, vcpkg automatycznie zarządza zależnościami.

### Instalacja krok po kroku:

```sh
# Krok 1: Pobierz vcpkg
git clone https://github.com/microsoft/vcpkg.git
cd vcpkg

# Krok 2: Zbootstrap narzędzie (zależnie od systemu)
# Na Windows PowerShell:
./bootstrap-vcpkg.bat

# Na Linux/Mac bash:
./bootstrap-vcpkg.sh

# Krok 3: Zainstaluj ONNX
./vcpkg install onnx
```

**Co się dzieje:**
- vcpkg automatycznie pobierze i zbuduje ONNX
- Skonfiguruje wszystkie zależności (Protobuf, etc.)
- Zintegruje się z Twoim systemem budowania (CMake)

**Czas instalacji:** 10-20 minut (zależnie od prędkości komputera)

## 🐍 Metoda 3: Pakiety Conda

**Co to jest Conda?** Menedżer pakietów i środowisk, popularny w społeczności data science.

**Kiedy używać:** Jeśli już pracujesz z Anaconda/Miniconda.

### Instalacja przez Conda:

```sh
conda install -c conda-forge onnx
```

**Wyjaśnienie parametrów:**
- `-c conda-forge` - pobiera z kanału conda-forge (community-maintained repository)
- `onnx` - nazwa pakietu do zainstalowania

**Zalety Conda:**
- Izolowane środowiska (nie psuje innych projektów)
- Łatwe zarządzanie wersjami Pythona
- Automatyczna rozdzielczość zależności

## 🏗️ Metoda 4: Budowanie ze źródeł - Dla zaawansowanych

**Dlaczego budować samodzielnie:**
- Chcesz modyfikować kod ONNX
- Potrzebujesz najnowszych zmian z brancha main
- Optymalizujesz dla specyficznego sprzętu
- Uczysz się jak działa ONNX wewnętrznie

### Przygotowanie - Ważne informacje

**Zanim zaczniesz:**

```sh
# Odinstaluj istniejącą wersję ONNX
pip uninstall onnx
```

**Czemu to ważne:** Stara zainstalowana wersja może kolidować z wersją budowaną ze źródeł.

**Wymagania systemowe:**

1. **Kompilator C++17 lub nowszy**
   - Linux: GCC 7+ lub Clang 5+
   - Mac: Xcode 10+ (clang)
   - Windows: Visual Studio 2019 lub nowsze

2. **Protobuf** (Protocol Buffers)
   - **Co to jest:** System serializacji danych stworzony przez Google
   - **Po co:** ONNX używa Protobuf do zapisywania struktury modeli
   - **Opcje:** ONNX może pobrać i zbudować automatycznie, lub możesz zainstalować ręcznie

### Konfiguracja Protobuf - Ważne decyzje

**Opcja A: Automatyczna (zalecana dla początkujących)**

Nie rób nic - ONNX automatycznie pobierze i zbuduje Protobuf podczas instalacji.

**Opcja B: Ręczna instalacja Protobuf**

Jeśli chcesz użyć konkretnej wersji lub już masz zainstalowanego Protobuf:

#### Shared libraries (biblioteki dynamiczne)

**Co to znaczy:** Pliki .dll (Windows), .so (Linux), .dylib (Mac) - kod ładowany w runtime.

```sh
# Linux/Mac
export CMAKE_ARGS="-DONNX_USE_PROTOBUF_SHARED_LIBS=ON"

# Windows
set CMAKE_ARGS="-DONNX_USE_PROTOBUF_SHARED_LIBS=ON"
```

#### Static libraries (biblioteki statyczne)

**Co to znaczy:** Pliki .lib (Windows), .a (Linux/Mac) - kod wkompilowany bezpośrednio.

```sh
# Linux/Mac
export CMAKE_ARGS="-DONNX_USE_PROTOBUF_SHARED_LIBS=OFF"

# Windows
set CMAKE_ARGS="-DONNX_USE_PROTOBUF_SHARED_LIBS=OFF"
```

**Jak sprawdzić jaki typ masz:**
- Shared: szukaj plików `libprotobuf.so` / `protobuf.dll` / `libprotobuf.dylib`
- Static: szukaj plików `libprotobuf.a` / `protobuf.lib`

**Domyślnie:** OFF (statyczne) - jeśli nie ustawisz, ONNX użyje bibliotek statycznych.

### Budowanie na Windows - Instrukcje szczegółowe

**Środowisko:** Windows 10/11 z Visual Studio 2019 lub nowszym

#### Metoda uproszczona:

```cmd
# Krok 1: Pobierz kod źródłowy
git clone https://github.com/onnx/onnx.git
cd onnx

# Krok 2: Pobierz submoduły (dodatkowe zależności)
git submodule update --init --recursive

# Krok 3: Konfiguracja budowania (opcjonalna optymalizacja)
set CMAKE_ARGS=-DONNX_USE_LITE_PROTO=ON -DONNX_USE_PROTOBUF_SHARED_LIBS=ON

# Krok 4: Zbuduj i zainstaluj
pip install -e . -v
```

**Wyjaśnienie flag:**
- `-DONNX_USE_LITE_PROTO=ON` - używa lekkiej wersji Protobuf (mniejsze pliki binarne, szybsza kompilacja)
- `-e` - tryb edytowalny (editable mode) - zmiany w kodzie od razu widoczne
- `-v` - verbose (szczegółowe logi kompilacji)

**Czas kompilacji:** 15-30 minut przy pierwszej kompilacji

### Środowisko oparte na pixi (Nowoczesne podejście)

**Co to jest pixi?** Nowoczesny menedżer środowisk bazujący na conda-forge.

**Dla kogo:** Dla osób, które chcą mieć pełne, odizolowane środowisko programistyczne.

#### Instalacja pixi:

Odwiedź [https://prefix.dev/](https://prefix.dev/) i podążaj za instrukcjami instalacji dla twojego systemu.

#### Użycie pixi z ONNX:

```sh
# Zbuduj i zainstaluj ONNX
pixi run install
```

**Co się dzieje:**
- pixi automatycznie tworzy izolowane środowisko
- Instaluje wszystkie wymagane zależności
- Buduje i instaluje ONNX

#### Uruchamianie testów:

```sh
# Testy C++ (googletest)
pixi run gtest

# Testy Python (pytest)
pixi run pytest
```

#### Dodatkowe zadania pixi:

```sh
# Generowanie dokumentacji operatorów
pixi run gen-docs

# Inicjalizacja lintrunner
pixi run lintrunner-init

# Uruchomienie lintrunner
pixi run lintrunner-run
```

**Zalety pixi:**
- Wszystko skonfigurowane automatycznie
- Odizolowane od systemowego Pythona
- Powtarzalne środowisko (wszyscy programiści mają to samo)

### Budowanie na Linux - Instrukcje krok po kroku

#### Wymagania wstępne:

**Ubuntu 20.04 i nowsze:**

```sh
# Instalacja podstawowych narzędzi
sudo apt-get update
sudo apt-get install python3-pip python3-dev libprotobuf-dev protobuf-compiler
```

**Inne dystrybucje:**
- Fedora: `sudo dnf install python3-devel protobuf-devel protobuf-compiler`
- Arch: `sudo pacman -S python protobuf`

**⚠️ Uwaga:** Systemowa wersja Protobuf może być starsza niż wymagane minimum (4.25.1).

#### Opcja A: Budowanie Protobuf ze źródeł (Zalecane)

**Dlaczego:** Kontrolujesz wersję i masz pewność kompatybilności.

<details>
  <summary>Kliknij, aby zobaczyć szczegółowe kroki budowania Protobuf</summary>

```sh
# Krok 1: Pobierz Protobuf
git clone https://github.com/protocolbuffers/protobuf.git
cd protobuf

# Krok 2: Przełącz się na stabilną wersję
git checkout v5.29.2

# Krok 3: Pobierz submoduły Protobuf
git submodule update --init --recursive

# Krok 4: Stwórz katalog budowania
mkdir build_source && cd build_source

# Krok 5: Konfiguruj CMake
cmake \
  -Dprotobuf_BUILD_SHARED_LIBS=OFF \
  -DCMAKE_INSTALL_PREFIX=/usr \
  -Dprotobuf_BUILD_TESTS=OFF \
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_POSITION_INDEPENDENT_CODE=ON \
  ..

# Krok 6: Zbuduj i zainstaluj
cmake --build . --target install
```

**Wyjaśnienie kluczowej flagi `-DCMAKE_POSITION_INDEPENDENT_CODE=ON`:**

**Problem:** Statyczne biblioteki domyślnie budują się bez flagi `-fPIC`.

**Co to oznacza:**
- PIC = Position Independent Code
- Kod, który może być załadowany pod dowolnym adresem pamięci
- **Wymagane** dla bibliotek współdzielonych (shared libraries)

**Dlaczego to ważne dla ONNX:**
- ONNX jest rozszerzeniem Python (shared library)
- Musi linkować się z bibliotekami Protobuf
- Jeśli Protobuf nie ma PIC, linkowanie się nie powiedzie

**Efekt:** Bez tej flagi dostaniesz błędy linkowania typu "recompile with -fPIC".

</details>

#### Opcja B: Budowanie ONNX (po zainstalowaniu Protobuf)

```sh
# Krok 1: Pobierz ONNX
git clone https://github.com/onnx/onnx.git
cd onnx

# Krok 2: Pobierz submoduły
git submodule update --init --recursive

# Krok 3: (Opcjonalnie) Użyj lite proto
export CMAKE_ARGS=-DONNX_USE_LITE_PROTO=ON

# Krok 4: Zbuduj i zainstaluj
pip install -e . -v
```

**Co to jest "lite proto":**
- Uproszczona wersja Protocol Buffers
- Mniejsze pliki binarne (~50% redukcji rozmiaru)
- Brak niektórych zaawansowanych funkcji (reflection, text format)
- Szybsza kompilacja i wykonanie

**Kiedy używać lite proto:**
- Aplikacje mobilne lub embedded
- Zależy Ci na rozmiarze binarki
- Nie potrzebujesz zaawansowanych funkcji Protobuf

### Budowanie na macOS - Specyfika Apple

#### Instalacja narzędzi przez Homebrew:

```sh
# Aktualizacja Homebrew
brew update

# Instalacja CMake (system budowania)
brew install cmake

# Protobuf zostanie zbudowany ze źródeł - tak jak na Linux
```

#### Budowanie Protobuf:

```sh
# Pobierz i przygotuj
git clone https://github.com/protocolbuffers/protobuf.git
cd protobuf
git checkout v5.29.2
git submodule update --init --recursive

# Stwórz katalog budowania
mkdir build_source && cd build_source

# Konfiguruj (uwaga na flagi dla macOS)
cmake \
  -Dprotobuf_BUILD_SHARED_LIBS=OFF \
  -Dprotobuf_BUILD_TESTS=OFF \
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_POSITION_INDEPENDENT_CODE=ON \
  ..

# Zbuduj i zainstaluj
cmake --build . --target install
```

**Aktualizacja PATH:**

Po budowaniu dodaj ścieżkę do binariów Protobuf:

```sh
# Dodaj do ~/.bash_profile lub ~/.zshrc
export PATH="/usr/local/bin:$PATH"
```

#### Budowanie ONNX na macOS:

```sh
# Pobierz kod (z submodułami od razu)
git clone --recursive https://github.com/onnx/onnx.git
cd onnx

# Opcjonalnie: lite proto
export CMAKE_ARGS=-DONNX_USE_LITE_PROTO=ON

# Zbuduj
pip install -e . -v
```

**Specyficzne problemy macOS:**
- **M1/M2 (Apple Silicon):** Wszystko powinno działać natywnie
- **Intel Mac:** Może wymagać Rosetta 2 dla niektórych zależności
- **Xcode:** Upewnij się, że masz zainstalowane narzędzia wiersza poleceń: `xcode-select --install`

## ✅ Weryfikacja instalacji

Po instalacji jakąkolwiek metodą, sprawdź czy ONNX działa:

```sh
python -c "import onnx; print(f'ONNX wersja: {onnx.__version__}')"
```

**Oczekiwane wyście:**
```
ONNX wersja: 1.x.x
```

**Jeśli zobaczysz błąd:**
- `ModuleNotFoundError`: ONNX nie został zainstalowany - sprawdź logi instalacji
- `ImportError` związany z Protobuf: Konflikt wersji Protobuf
- Błędy kompilacji: Zobacz sekcję "Typowe błędy" poniżej

### Test bardziej zaawansowany:

```python
import onnx
from onnx import helper, TensorProto

# Stwórz prosty model (dwa wejścia, jedno wyjście - suma)
input1 = helper.make_tensor_value_info('input1', TensorProto.FLOAT, [1, 3])
input2 = helper.make_tensor_value_info('input2', TensorProto.FLOAT, [1, 3])
output = helper.make_tensor_value_info('output', TensorProto.FLOAT, [1, 3])

# Węzeł Add
add_node = helper.make_node('Add', ['input1', 'input2'], ['output'])

# Graf
graph = helper.make_graph([add_node], 'test_graph', [input1, input2], [output])

# Model
model = helper.make_model(graph)

# Sprawdź poprawność
onnx.checker.check_model(model)

print("✅ ONNX działa poprawnie! Model test został stworzony i zwalidowany.")
```

## ⚙️ Opcje budowania - Zaawansowane

### Zmienne środowiskowe:

#### `USE_MSVC_STATIC_RUNTIME`

**Tylko Windows!**

```cmd
set USE_MSVC_STATIC_RUNTIME=1  # Linkuj statycznie z runtime
set USE_MSVC_STATIC_RUNTIME=0  # Linkuj dynamicznie (domyślne)
```

**Co to zmienia:**
- `=1`: Runtime C++ wkompilowany w binarki ONNX (większy rozmiar, brak zależności)
- `=0`: Runtime C++ jako DLL (mniejszy rozmiar, wymaga Visual C++ Redistributable)

**Domyślnie:** 0 (dynamiczne linkowanie)

#### `DEBUG`

```sh
# Linux/Mac
export DEBUG=1  # Build debug
export DEBUG=0  # Build release (domyślne)

# Windows
set DEBUG=1
```

**Co się zmienia w trybie debug:**
- Włączone symbole debugowania
- Wyłączone optymalizacje
- Więcej asercji (sprawdzeń) w kodzie
- Wolniejsze wykonanie, ale łatwiejsze debugowanie

**Uwaga:** W trybie debug musisz też mieć debug wersje zależności. W `CMakeLists.txt` zmień:
```cmake
NAMES protobuf-lite  # na
NAMES protobuf-lited  # (z 'd' na końcu)
```

### Zmienne CMake:

#### `ONNX_USE_PROTOBUF_SHARED_LIBS`

```sh
# Używaj shared libraries Protobuf
export CMAKE_ARGS="-DONNX_USE_PROTOBUF_SHARED_LIBS=ON"

# Używaj static libraries Protobuf (domyślne)
export CMAKE_ARGS="-DONNX_USE_PROTOBUF_SHARED_LIBS=OFF"
```

**Kiedy ON:**
- Definiuje `PROTOBUF_USE_DLLS`
- ONNX linkuje się z protobuf.dll / libprotobuf.so
- Mniejsze binarie ONNX
- Wymaga obecności DLL podczas uruchomienia

**Kiedy OFF (domyślne):**
- ONNX zawiera cały kod Protobuf
- Większe binarie
- Brak zewnętrznych zależności runtime

#### `ONNX_USE_LITE_PROTO`

```sh
export CMAKE_ARGS="-DONNX_USE_LITE_PROTO=ON"  # Lite version
# lub
export CMAKE_ARGS="-DONNX_USE_LITE_PROTO=OFF"  # Full version (domyślne)
```

**Porównanie:**

| Aspekt | Full Protobuf | Lite Protobuf |
|--------|---------------|---------------|
| Rozmiar binarki | Większy (~2-3x) | Mniejszy |
| Prędkość | Trochę wolniejszy | Szybszy |
| Reflection | Tak | Nie |
| Text format | Tak | Nie |
| Użycie pamięci | Więcej | Mniej |

**Zalecenie:** Lite dla produkcji, Full dla developmentu i debugowania.

#### `ONNX_WERROR`

```sh
export CMAKE_ARGS="-DONNX_WERROR=ON"   # Ostrzeżenia = błędy
export CMAKE_ARGS="-DONNX_WERROR=OFF"  # Ostrzeżenia = tylko ostrzeżenia
```

**Co robi:** Traktuje ostrzeżenia kompilera jako błędy (kompilacja się nie powiedzie).

**Domyślnie:**
- OFF w lokalnych buildach (możesz ignorować ostrzeżenia)
- ON w CI i release pipelines (wymuszamy jakość)

**Dla studentów:** Pozostaw OFF, chyba że chcesz mieć super czysty kod.

## 🐛 Typowe błędy i rozwiązania

### Błąd 1: `ModuleNotFoundError: No module named 'onnx.onnx_cpp2py_export'`

**Objawy:** Import ONNX nie działa z katalogu źródłowego.

**Przyczyna:** Próbujesz importować ONNX z katalogu, gdzie jest kod źródłowy.

**Rozwiązanie:**
```sh
# Wyjdź z katalogu onnx/
cd ..

# Teraz sprawdź import
python -c "import onnx"
```

**Dlaczego to się dzieje:** Python najpierw szuka modułów w bieżącym katalogu. Znajduje katalog `onnx/`, ale tam nie ma skompilowanych rozszerzeń C++.

### Błąd 2: Konflikt shared vs. static Protobuf libraries

**Objawy:** 
```
Could not find protobuf library
undefined reference to `google::protobuf::...`
```

**Przyczyna:** ONNX szuka jednego typu biblioteki, a Ty masz drugi.

**Rozwiązanie:**

Opcja A - Usuń konfliktujące biblioteki:
```sh
# Znajdź wszystkie instalacje Protobuf
find /usr -name "libprotobuf*"

# Usuń te, których nie chcesz używać
sudo rm /usr/lib/libprotobuf.so*  # usuń shared
# lub
sudo rm /usr/lib/libprotobuf.a    # usuń static
```

Opcja B - Zbuduj Protobuf od nowa:
```sh
# Zbuduj zgodnie z instrukcjami w sekcji Linux
# Upewnij się, że używasz -Dprotobuf_BUILD_SHARED_LIBS=OFF dla static
```

### Błąd 3: `Could not find pythonXX.lib` (Windows)

**Objawy:** Błąd podczas budowania na Windows.

**Przyczyna:** Różne wersje Python dla różnych komend.

**Rozwiązanie:**

```cmd
# Sprawdź wersje
python --version
pip --version

# Jeśli są różne, użyj:
python -m pip install -e . -v
```

**Dodatkowe kroki:**
1. Usuń katalog `.setuptools-cmake-build/`
2. Przebuduj od nowa
3. Upewnij się, że PATH wskazuje na jedną instalację Python

### Błąd 4: Błędy kompilacji C++ "recompile with -fPIC"

**Objawy:**
```
relocation R_X86_64_32 against `.rodata' can not be used when making a shared object; recompile with -fPIC
```

**Przyczyna:** Statyczna biblioteka bez Position Independent Code.

**Rozwiązanie:**

Przebuduj Protobuf z flagą:
```sh
cmake -DCMAKE_POSITION_INDEPENDENT_CODE=ON ...
```

Zobacz szczegóły w sekcji "Budowanie Protobuf ze źródeł" powyżej.

### Błąd 5: Timeout podczas instalacji pip

**Objawy:** `pip install` zawiesza się lub timeout.

**Przyczyna:** Wolne połączenie lub kompilacja ze źródeł trwa bardzo długo.

**Rozwiązanie:**

```sh
# Zwiększ timeout
pip install --timeout=1000 onnx

# Lub użyj verbose aby widzieć postęp
pip install -v onnx

# Lub zainstaluj prekompilowane koło
pip install --only-binary :all: onnx
```

## 📊 Benchmarking i profilowanie

Po zainstalowaniu możesz sprawdzić wydajność:

```python
import onnx
import time

# Załaduj model
model_path = "twoj_model.onnx"
model = onnx.load(model_path)

# Zmierz czas wnioskowania kształtów
start = time.time()
onnx.shape_inference.infer_shapes(model)
end = time.time()

print(f"Wnioskowanie kształtów zajęło: {end - start:.4f} sekund")
```

## 🎓 Dodatkowe zasoby dla studentów

**Polecane tutoriale:**
1. [ONNX Tutorials](https://github.com/onnx/tutorials) - oficjalne przykłady
2. [ONNX Model Zoo](https://github.com/onnx/models) - gotowe modele do nauki

**Społeczność:**
- [GitHub Discussions](https://github.com/onnx/onnx/discussions) - zadawaj pytania
- [Slack LF AI](https://lfaifoundation.slack.com/) - czat społeczności

**Dokumentacja techniczna:**
- [IR Specification](https://github.com/onnx/onnx/blob/main/docs/IR.md) - jak modele są reprezentowane
- [Operators](https://github.com/onnx/onnx/blob/main/docs/Operators.md) - lista wszystkich operatorów

## 🎯 Podsumowanie - Szybki start

**Dla absolutnych początkujących:**
```sh
pip install onnx
python -c "import onnx; print('Działa!')"
```

**Dla programistów chcących kontrybuować:**
```sh
git clone https://github.com/onnx/onnx.git
cd onnx
git submodule update --init --recursive
pip install -e . -v
pytest  # sprawdź czy testy przechodzą
```

**Dla użytkowników Conda:**
```sh
conda create -n onnx_env python=3.10
conda activate onnx_env
conda install -c conda-forge onnx
```

---

**Masz problemy z instalacją?** 
1. Sprawdź sekcję "Typowe błędy" powyżej
2. Przeszukaj [GitHub Issues](https://github.com/onnx/onnx/issues)
3. Zapytaj na [Slack](https://lfaifoundation.slack.com/)

**Powodzenia z ONNX! 🚀**
