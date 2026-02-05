<!--
Copyright (c) ONNX Project Contributors

SPDX-License-Identifier: Apache-2.0
-->

<p align="center"><img width="40%" src="https://github.com/onnx/onnx/raw/main/docs/onnx-horizontal-color.png" /></p>

[![PyPI - Version](https://img.shields.io/pypi/v/onnx.svg)](https://pypi.org/project/onnx)
[![CI](https://github.com/onnx/onnx/actions/workflows/main.yml/badge.svg)](https://github.com/onnx/onnx/actions/workflows/main.yml)
[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/3313/badge)](https://bestpractices.coreinfrastructure.org/projects/3313)
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/onnx/onnx/badge)](https://api.securityscorecards.dev/projects/github.com/onnx/onnx)
[![REUSE compliant](https://api.reuse.software/badge/github.com/onnx/onnx)](https://api.reuse.software/info/github.com/onnx/onnx)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![abi3 compatible](https://img.shields.io/badge/abi3-compatible-brightgreen)](https://docs.python.org/3/c-api/stable.html)

# Czym jest ONNX? - Wprowadzenie dla studentów

[Open Neural Network Exchange (ONNX)](https://onnx.ai) to otwarty ekosystem, który umożliwia programistom sztucznej inteligencji wybór odpowiednich narzędzi w miarę rozwoju ich projektów. 

**Dla początkujących:** ONNX to jak "uniwersalny język" dla modeli sztucznej inteligencji. Wyobraź sobie, że masz model AI stworzony w jednym frameworku (np. PyTorch), ale chcesz go użyć w innym środowisku (np. TensorFlow lub urządzeniu mobilnym). ONNX pozwala na to poprzez zapewnienie wspólnego formatu, który rozumieją różne systemy.

**Co oferuje ONNX:**
- **Format otwartoźródłowy** dla modeli AI - zarówno dla głębokiego uczenia (deep learning), jak i tradycyjnego uczenia maszynowego (ML)
- **Definicję rozszerzalnego grafu obliczeń** - reprezentuje strukturę modelu w sposób niezależny od frameworka
- **Zbiór wbudowanych operatorów** - podstawowe operacje matematyczne i logiczne używane w modelach
- **Standardowe typy danych** - określa jak dane są reprezentowane i przetwarzane

**Aktualny fokus:** Koncentrujemy się głównie na możliwościach potrzebnych do wnioskowania (inference), czyli wykorzystywania wytrenowanych modeli do przewidywań.

ONNX jest [szeroko wspierany](http://onnx.ai/supported-tools) i można go znaleźć w wielu frameworkach, narzędziach i sprzęcie. Umożliwienie interoperacyjności między różnymi frameworkami i usprawnienie ścieżki od badań do produkcji pomaga zwiększyć tempo innowacji w społeczności AI. Zapraszamy społeczność do dołączenia do nas i dalszego rozwijania ONNX.


# Jak zacząć używać ONNX - Przewodnik dla początkujących

**Krok 1: Zapoznaj się z dokumentacją**
* [Dokumentacja pakietu ONNX Python](https://onnx.ai/onnx/) - Tutaj znajdziesz szczegółowy opis wszystkich funkcji dostępnych w bibliotece Python

**Krok 2: Naucz się tworzyć modele**
* [Samouczki tworzenia modeli ONNX](https://github.com/onnx/tutorials) - Praktyczne przykłady krok po kroku, idealne do nauki

**Krok 3: Eksperymentuj z gotowymi modelami**
* [Wstępnie wytrenowane modele ONNX](https://github.com/onnx/models) - Gotowe modele, które możesz od razu przetestować bez konieczności długiego trenowania

# Poznaj specyfikację ONNX - Materiały teoretyczne dla studentów

**Co to jest specyfikacja?** To zbiór reguł i definicji opisujących, jak powinien działać ONNX. Dla studentów informatyki to jak dokumentacja techniczna opisująca protokół komunikacji.

**Rekomendowana kolejność nauki:**

1. **Zaczynij od podstaw:** [Przegląd ogólny](https://github.com/onnx/onnx/blob/main/docs/Overview.md) - Najpierw przeczytaj to, aby zrozumieć ogólną ideę
2. **Zrozum reprezentację:** [Specyfikacja reprezentacji pośredniej IR](https://github.com/onnx/onnx/blob/main/docs/IR.md) - Dowiedz się, jak modele są zapisywane wewnętrznie
3. **Wersjonowanie:** [Zasady wersjonowania](https://github.com/onnx/onnx/blob/main/docs/Versioning.md) - Ważne dla kompatybilności między wersjami
4. **Operatory - budulec modeli:** 
   - [Dokumentacja operatorów (kod źródłowy)](https://github.com/onnx/onnx/blob/main/docs/Operators.md)
   - [Dokumentacja operatorów (najnowsza wersja online)](https://onnx.ai/onnx/operators/index.html)
5. **Programowanie w Python:** [Przegląd API Python](https://github.com/onnx/onnx/blob/main/docs/PythonAPIOverview.md) - Jak używać ONNX w swoim kodzie

# Narzędzia programistyczne do pracy z grafami ONNX

**Dla studentów:** Graf w kontekście ONNX to sposób reprezentacji modelu AI jako sieci połączonych operacji. Wyobraź sobie to jak schemat blokowy, gdzie każdy blok to operacja (np. mnożenie macierzy, aktywacja), a strzałki to przepływ danych.

**Trzy kluczowe narzędzia do opanowania:**

### 1. Wnioskowanie kształtów i typów (Shape and Type Inference)
[Dokumentacja wnioskowania kształtów](https://github.com/onnx/onnx/blob/main/docs/ShapeInference.md)

**Co to robi?** Automatycznie określa wymiary tensorów w modelu. Tensor to wielowymiarowa tablica danych - np. obraz może być tensorem 3D (wysokość × szerokość × kanały kolorów).

**Dlaczego to ważne?** Pomaga wykryć błędy przed uruchomieniem modelu - np. jeśli próbujesz pomnożyć macierze o niezgodnych wymiarach.

### 2. Optymalizacja grafu (Graph Optimization)
[Optymalizator ONNX](https://github.com/onnx/optimizer)

**Co to robi?** Upraszcza i przyspiesza model poprzez eliminację zbędnych operacji, łączenie warstw, czy reorganizację obliczeń.

**Przykład:** Jeśli masz dwie kolejne operacje mnożenia przez stałe, optymalizator może je połączyć w jedną.

### 3. Konwersja wersji operatorów (Opset Version Conversion)
[Dokumentacja konwertera wersji](https://github.com/onnx/onnx/blob/main/docs/docsgen/source/api/version_converter.md)

**Co to robi?** Umożliwia aktualizację lub cofnięcie wersji modelu, aby był kompatybilny z różnymi środowiskami.

**Kiedy używać?** Gdy masz stary model i chcesz wykorzystać nowe funkcje, lub odwrotnie - chcesz użyć modelu na starszym systemie.

# Jak możesz pomóc w rozwoju projektu ONNX?

**Dla studentów rozpoczynających pracę z open source:**

ONNX to projekt społecznościowy z otwartym modelem zarządzania opisanym [tutaj](https://github.com/onnx/onnx/blob/main/community/readme.md). Zachęcamy do dołączenia i wnoszenia opinii, pomysłów oraz kodu. 

**Sposoby zaangażowania:**
- Dołącz do [Grup Specjalnego Zainteresowania (SIG)](https://github.com/onnx/onnx/blob/main/community/sigs.md) - tematyczne zespoły pracujące nad konkretnymi aspektami
- Uczestni w [Grupach Roboczych](https://github.com/onnx/onnx/blob/main/community/working-groups.md) - zadaniowe zespoły realizujące określone cele

**Pierwsze kroki w kontrybuowaniu:**

Sprawdź nasz [przewodnik kontrybucji](https://github.com/onnx/onnx/blob/main/CONTRIBUTING.md), aby rozpocząć.

**Chcesz dodać nowy operator?** 

Operator to podstawowa operacja wykonywana na danych (np. konwolucja, normalizacja). Jeśli uważasz, że jakiś operator powinien zostać dodany do specyfikacji ONNX, przeczytaj [ten dokument](https://github.com/onnx/onnx/blob/main/docs/AddNewOp.md) - znajdziesz tam dokładny proces propozycji i implementacji.

# Spotkania społeczności - Gdzie i kiedy się uczyć od innych?

**Regularne spotkania zespołów:**

Harmonogramy regularnych spotkań Komitetu Sterującego, grup roboczych oraz SIG znajdziesz [w kalendarzu ONNX](https://onnx.ai/calendar).

**Dla studentów:** To świetna okazja, aby zobaczyć jak działają prawdziwe projekty open source. Możesz obserwować dyskusje, zadawać pytania i uczyć się od doświadczonych programistów.

**Coroczne spotkania społeczności:**

Społeczność organizuje spotkania co najmniej raz w roku. Materiały z poprzednich wydarzeń:

* 2020.04.09 - [Wirtualne spotkanie Silicon Valley](https://lf-aidata.atlassian.net/wiki/spaces/DL/pages/14091402/LF+AI+Day+-ONNX+Community+Virtual+Meetup+-+Silicon+Valley+-+2020+April+9)
* 2020.10.14 - [Warsztat społeczności październik](https://lf-aidata.atlassian.net/wiki/spaces/DL/pages/14092138/LF+AI+Day+-+ONNX+Community+Workshop+-+2020+October+14)
* 2021.03.24 - [Wirtualne spotkanie marzec](https://lf-aidata.atlassian.net/wiki/spaces/DL/pages/14092424/Instructions+for+Event+Hosts+-+LF+AI+Data+Day+-+ONNX+Virtual+Community+Meetup+-+March+2021)
* 2021.10.21 - [Wirtualne spotkanie październik](https://lf-aidata.atlassian.net/wiki/spaces/DL/pages/14093194/LF+AI+Data+Day+ONNX+Community+Virtual+Meetup+-+October+2021)
* 2022.06.24 - [Dzień społeczności czerwiec](https://lf-aidata.atlassian.net/wiki/spaces/DL/pages/14093969/ONNX+Community+Day+-+2022+June+24)
* 2023.06.28 - [Dzień społeczności czerwiec](https://lf-aidata.atlassian.net/wiki/spaces/DL/pages/14094507/ONNX+Community+Day+2023+-+June+28)

# Gdzie szukać pomocy? - Kanały komunikacji

**Dla studentów potrzebujących wsparcia:**

Zachęcamy do otwierania [Issues na GitHubie](https://github.com/onnx/onnx/issues) gdy napotkasz problem lub masz pytanie. 

**Dyskusje w czasie rzeczywistym:**
Dołącz do [Slack LF AI Foundation](https://lfaifoundation.slack.com/). Jeśli jeszcze nie masz konta, użyj [tego linku do dołączenia](https://join.slack.com/t/lfaifoundation/shared_invite/zt-o65errpw-gMTbwNr7FnNbVXNVFkmyNA).

**Wskazówka:** Slack jest lepszy do szybkich pytań i dyskusji, a GitHub Issues do zgłaszania błędów i propozycji funkcji.

# Bądź na bieżąco z nowinkami ONNX

Śledź najnowsze informacje o ONNX:
- [[Facebook](https://www.facebook.com/onnxai/)]
- [[Twitter/X](https://twitter.com/onnxai)]

# Plan rozwoju projektu (Roadmap)

**Co to jest roadmap?** To dokument planistyczny pokazujący kierunek rozwoju projektu w nadchodzących miesiącach.

Proces planowania odbywa się co roku. Szczegóły znajdziesz [w repozytorium komitetu sterującego](https://github.com/onnx/steering-committee/tree/main/roadmap).

**Dla studentów:** Przejrzenie roadmapy pomoże Ci zrozumieć, jakie funkcje będą dodawane i możesz nauczyć się przy ich implementacji.

# Instalacja - Przewodnik krok po kroku dla studentów

**Metoda 1: Najprostsza instalacja (zalecana dla początkujących)**

Pakiety wydawnicze ONNX są publikowane w repozytorium PyPI (Python Package Index).

```sh
pip install onnx
```

**Co się dzieje po uruchomieniu tej komendy?**
1. `pip` (menedżer pakietów Python) łączy się z serwerem PyPI
2. Pobiera najnowszą stabilną wersję ONNX
3. Instaluje pakiet wraz z wszystkimi wymaganymi zależnościami
4. Po zakończeniu możesz używać `import onnx` w swoim kodzie Python

**Opcjonalnie - instalacja z dodatkowymi narzędziami:**
```sh
pip install onnx[reference]
```
Ten wariant instaluje również zależności dla referencyjnej implementacji - przydatne, jeśli chcesz testować modele bezpośrednio w Python.

**Metoda 2: Wersje tygodniowe (dla zaawansowanych - testowanie nowych funkcji)**

[Pakiety tygodniowe ONNX](https://pypi.org/project/onnx-weekly/) umożliwiają eksperymentowanie z najnowszymi funkcjami, zanim trafią do stabilnego wydania.

**Ostrzeżenie:** Te wersje mogą zawierać błędy - używaj tylko do testów, nie w produkcji!

**Szczegółowe instrukcje:**

Szczegółowe instrukcje instalacji, w tym typowe opcje budowania i częste błędy, znajdziesz [w pliku INSTALL.md](https://github.com/onnx/onnx/blob/main/INSTALL.md).

# Kompatybilność Python ABI3 - Co to oznacza?

**Dla studentów:** ABI (Application Binary Interface) to sposób, w jaki skompilowany kod współpracuje z Pythonem.

Ten pakiet dostarcza koła binarne kompatybilne z [abi3](https://docs.python.org/3/c-api/stable.html), co oznacza, że:
- Jedno skompilowane koło działa z wieloma wersjami Pythona (od wersji 3.12 wzwyż)
- Nie musisz instalować osobnych wersji dla Python 3.12, 3.13, 3.14 itd.
- To oszczędza miejsce i upraszcza dystrybucję


# Testowanie - Jak sprawdzić, czy wszystko działa?

**Framework testowy:** ONNX używa [pytest](https://docs.pytest.org) jako narzędzia do uruchamiania testów.

**Krok 1: Zainstaluj pytest**

```sh
pip install pytest
```

**Co to jest pytest?** To popularne narzędzie do testowania kodu w Python. Automatycznie znajduje i uruchamia testy, raportuje wyniki i pokazuje, co działa, a co nie.

**Krok 2: Uruchom testy**

```sh
pytest
```

**Co się dzieje?**
- `pytest` przeszukuje katalogi w poszukiwaniu plików testowych (zwykle `test_*.py`)
- Uruchamia wszystkie znalezione funkcje testowe
- Wyświetla raport: ile testów przeszło (✓), ile nie powiodło się (✗)
- Pokazuje szczegóły błędów dla nieudanych testów

**Dla studentów:** Uruchamianie testów to dobra praktyka programistyczna. Pomaga upewnić się, że twoje zmiany nie zepsuły istniejącej funkcjonalności.

# Programowanie i rozwijanie projektu

Sprawdź [przewodnik dla kontrybutorów](https://github.com/onnx/onnx/blob/main/CONTRIBUTING.md), aby poznać szczegółowe instrukcje dotyczące:
- Konfiguracji środowiska programistycznego
- Standardów kodowania
- Procesu wysyłania zmian (Pull Requests)
- Testowania własnych modyfikacji

# Powtarzalne buildy (Linux) - Dlaczego to ważne?

**Co to jest "reproducible build"?**

To oznacza, że ten sam kod źródłowy zawsze wyprodukuje identyczne pliki binarne, niezależnie od tego:
- Kto kompiluje projekt
- Gdzie jest kompilowany
- Kiedy odbywa się kompilacja

**Jak to działa?**

Używamy standardu [`SOURCE_DATE_EPOCH`](https://reproducible-builds.org/docs/source-date-epoch/), który:
- Ustawia stałą wartość znacznika czasu kompilacji
- Eliminuje inne informacje zależne od czasu
- Gwarantuje bit-po-bicie identyczne wyniki w różnych środowiskach

**Dlaczego to ma znaczenie dla studentów i użytkowników?**

1. **Przejrzystość:** Każdy może zweryfikować, że rozpowszechniane pliki binarne powstały z opublikowanego kodu źródłowego
2. **Bezpieczeństwo:** Zapobiega wprowadzaniu złośliwego kodu lub ukrytych zmian w procesie budowania
3. **Zaufanie:** Użytkownicy mogą mieć pewność, że pobrane pliki binarne są dokładnie takie, jak zamierzyli opiekunowie projektu

**Opcja dla początkujących:** Jeśli wolisz, możesz użyć gotowych powtarzalnych plików binarnych zamiast samodzielnie budować ze źródła.

# Licencja

[Apache License v2.0](LICENSE) - licencja open source pozwalająca na swobodne używanie, modyfikowanie i dystrybuowanie oprogramowania

# Znak towarowy

Sprawdź rejestrację znaku towarowego na [https://trademarks.justia.com](https://trademarks.justia.com/877/25/onnx-87725026.html).

[Ogólne zasady Linux Foundation dotyczące używania znaków towarowych](https://www.linuxfoundation.org/legal/trademark-usage)

# Kodeks postępowania

[ONNX Open Source - Kodeks postępowania](https://onnx.ai/codeofconduct.html) - zasady etycznego i profesjonalnego zachowania w społeczności
