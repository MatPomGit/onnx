# Przewodnik Edukacyjny dla Studentów - Pierwsze Kroki z ONNX

## 🎓 Wprowadzenie dla Początkujących

Witaj w świecie ONNX! Ten dokument został stworzony specjalnie dla studentów, którzy po raz pierwszy zetknęli się z tą technologią. Nie martw się jeśli niektóre terminy brzmią skomplikowanie - wszystko wyjaśnimy krok po kroku.

## 📖 Czym właściwie jest ONNX? - Analogie ze świata rzeczywistego

Wyobraź sobie, że masz dokument tekstowy:
- **Word** może go zapisać w formacie `.docx`
- **LibreOffice** używa formatu `.odt`
- **Google Docs** ma swój własny format w chmurze

Co jeśli chcesz otworzyć dokument z Word w LibreOffice? Potrzebny jest **wspólny format** który rozumieją oba programy - na przykład `.pdf` lub `.txt`.

**ONNX pełni podobną rolę dla modeli sztucznej inteligencji!**

### Konkretny przykład:
- Stworzysz model AI w **PyTorch** (popularny framework do deep learning)
- Chcesz go uruchomić na urządzeniu mobilnym używającym **Core ML**
- Bezpośrednia konwersja? Trudna lub niemożliwa!
- **Rozwiązanie:** PyTorch → ONNX → Core ML ✅

## 🧩 Podstawowe Komponenty - Budulce Modeli

### 1. Model (Najwyższy poziom)
To cały "pakiet" zawierający:
```
Model ONNX
├── Metadane (kto stworzył, wersja, opis)
├── Graf obliczeniowy (jak przetwarzać dane)
└── Wagi (wyuczone parametry)
```

**Analogia:** Model to jak cała książka - ma tytuł (metadane), spis treści (graf) i zawartość (wagi).

### 2. Graf (Graph)
Przepis krok po kroku na przetwarzanie danych:
```
Wejście → [Operacja 1] → [Operacja 2] → [Operacja 3] → Wyjście
```

**Przykład rozpoznawania obrazów:**
```
Obraz (224x224x3)
    ↓
[Konwolucja] - wyciągnięcie cech
    ↓
[Aktywacja ReLU] - nieliniowość
    ↓
[Pooling] - redukcja wymiarów
    ↓
[Fully Connected] - klasyfikacja
    ↓
Prawdopodobieństwa klas (10 liczb)
```

### 3. Węzły (Nodes) - Pojedyncze Operacje
Każdy węzeł to jedna operacja matematyczna:
- **Add** - dodawanie: `C = A + B`
- **MatMul** - mnożenie macierzy: `C = A × B`
- **Conv** - konwolucja (filtrowanie obrazu)
- **ReLU** - funkcja aktywacji: `y = max(0, x)`

**Węzeł zawiera:**
- **Typ operacji** (op_type): np. "Conv", "Add"
- **Wejścia** (inputs): skąd brać dane
- **Wyjścia** (outputs): gdzie zapisać wynik
- **Atrybuty** (attributes): parametry konfiguracyjne

### 4. Tensory - Wielowymiarowe Tablice
Podstawowa struktura danych:

**0D Tensor (Skalar):** Pojedyncza liczba
```
5.0
```

**1D Tensor (Wektor):** Lista liczb
```
[1.0, 2.0, 3.0, 4.0]
```

**2D Tensor (Macierz):** Tabela liczb
```
[[1.0, 2.0, 3.0],
 [4.0, 5.0, 6.0]]
```

**3D Tensor:** Na przykład kolorowy obraz
```
Wymiar 1: wysokość (np. 224 pikseli)
Wymiar 2: szerokość (np. 224 pikseli)
Wymiar 3: kanały RGB (3: czerwony, zielony, niebieski)
```

**4D Tensor:** Batch obrazów
```
Wymiar 1: liczba obrazów w batchu (np. 32)
Wymiar 2-4: jak w 3D tensorze dla pojedynczego obrazu
```

## 🛠️ Twój Pierwszy Model ONNX - Krok po Kroku

Stwórzmy prosty model który dodaje dwie liczby. To jak "Hello World" w świecie ONNX!

### Krok 1: Import bibliotek
```python
import onnx
from onnx import helper, TensorProto
import numpy as np
```

**Co importujemy:**
- `onnx` - główna biblioteka
- `helper` - funkcje pomocnicze do tworzenia komponentów
- `TensorProto` - definicje typów danych
- `numpy` - do pracy z tablicami liczbowymi

### Krok 2: Zdefiniuj wejścia i wyjścia
```python
# Pierwszy argument do dodania
wejscie_a = helper.make_tensor_value_info(
    'a',                    # nazwa zmiennej
    TensorProto.FLOAT,      # typ danych (liczby zmiennoprzecinkowe)
    [1]                     # kształt (1 liczba)
)

# Drugi argument do dodania
wejscie_b = helper.make_tensor_value_info(
    'b', 
    TensorProto.FLOAT, 
    [1]
)

# Wynik dodawania
wyjscie_suma = helper.make_tensor_value_info(
    'suma', 
    TensorProto.FLOAT, 
    [1]
)
```

**Wyjaśnienie:**
- `make_tensor_value_info` tworzy "deklarację" tensora
- To jak mówienie "będzie zmienna 'a' typu float o rozmiarze 1"
- Nie zawiera jeszcze wartości - to tylko "szablon"

### Krok 3: Stwórz węzeł operacji
```python
wezel_dodawania = helper.make_node(
    'Add',              # typ operacji
    ['a', 'b'],         # wejścia (nazwy muszą zgadzać się z powyżej!)
    ['suma']            # wyjścia
)
```

**Co się dzieje:**
- Mówimy: "Stwórz operację Add"
- "Weź dane z 'a' i 'b'"
- "Wynik zapisz jako 'suma'"

### Krok 4: Zbuduj graf
```python
graf = helper.make_graph(
    [wezel_dodawania],                      # lista węzłów
    'graf_dodawania',                       # nazwa grafu
    [wejscie_a, wejscie_b],                # wejścia grafu
    [wyjscie_suma]                         # wyjścia grafu
)
```

**Graf to przepis:**
1. Przyjmij dane wejściowe 'a' i 'b'
2. Wykonaj operację Add
3. Zwróć wynik jako 'suma'

### Krok 5: Stwórz model
```python
model = helper.make_model(
    graf,
    producer_name='student-tutorial',      # kto stworzył
    opset_imports=[helper.make_opsetid("", 13)]  # wersja operatorów
)
```

**Model to kompletny pakiet:**
- Zawiera graf
- Plus metadane (kto, kiedy, jaka wersja)

### Krok 6: Sprawdź poprawność
```python
onnx.checker.check_model(model)
print("✅ Model jest poprawny!")
```

**Sprawdzanie (checking):**
- Czy wszystkie nazwy się zgadzają?
- Czy typy danych są kompatybilne?
- Czy używane operacje istnieją?
- Czy nie ma błędów logicznych?

### Krok 7: Zapisz model
```python
onnx.save(model, 'moj_pierwszy_model.onnx')
print("💾 Model zapisany!")
```

**Plik .onnx zawiera:**
- Całą strukturę modelu w formacie Protocol Buffers
- Można go otworzyć w innych narzędziach
- Można go uruchomić w różnych frameworkach

### Krok 8: Wczytaj i użyj
```python
# Wczytaj zapisany model
zaladowany_model = onnx.load('moj_pierwszy_model.onnx')

# Sprawdź czy się poprawnie wczytał
onnx.checker.check_model(zaladowany_model)

# Wyświetl podsumowanie
print(f"Nazwa modelu: {zaladowany_model.graph.name}")
print(f"Liczba węzłów: {len(zaladowany_model.graph.node)}")
```

## 🔍 Inspekcja Modelu - Co jest w środku?

Nauczmy się czytać zawartość modelu:

```python
model = onnx.load('moj_pierwszy_model.onnx')

print("=== WEJŚCIA MODELU ===")
for wejscie in model.graph.input:
    print(f"Nazwa: {wejscie.name}")
    print(f"Typ: {wejscie.type.tensor_type.elem_type}")
    print(f"Kształt: {[dim.dim_value for dim in wejscie.type.tensor_type.shape.dim]}")
    print()

print("=== WĘZŁY (OPERACJE) ===")
for wezel in model.graph.node:
    print(f"Operacja: {wezel.op_type}")
    print(f"Wejścia: {list(wezel.input)}")
    print(f"Wyjścia: {list(wezel.output)}")
    print()

print("=== WYJŚCIA MODELU ===")
for wyjscie in model.graph.output:
    print(f"Nazwa: {wyjscie.name}")
```

**Dlaczego to przydatne:**
- Debugowanie - widzisz co jest nie tak
- Zrozumienie cudzego modelu
- Weryfikacja przed deploymentem

## 📊 Wizualizacja Modeli

ONNX modele można wizualizować! Polecane narzędzia:

### 1. Netron (Najprostsze)
```python
# Zainstaluj: pip install netron
import netron

# Otwórz model w przeglądarce
netron.start('moj_pierwszy_model.onnx')
```

**Co zobaczysz:**
- Graficzny diagram przepływu danych
- Kształty tensorów na każdym etapie
- Parametry każdej operacji
- Interaktywna eksploracja

### 2. Własna wizualizacja tekstowa
```python
def wyswietl_model(sciezka_modelu):
    """
    Prosta funkcja do wyświetlania struktury modelu.
    Idealna dla studentów do nauki!
    """
    model = onnx.load(sciezka_modelu)
    
    print("╔" + "="*50 + "╗")
    print(f"║ MODEL: {model.graph.name:^46} ║")
    print("╠" + "="*50 + "╣")
    
    print("║ WEJŚCIA:                                       ║")
    for idx, inp in enumerate(model.graph.input, 1):
        print(f"║   {idx}. {inp.name:40} ║")
    
    print("║ OPERACJE:                                      ║")
    for idx, node in enumerate(model.graph.node, 1):
        print(f"║   {idx}. {node.op_type:40} ║")
    
    print("║ WYJŚCIA:                                       ║")
    for idx, out in enumerate(model.graph.output, 1):
        print(f"║   {idx}. {out.name:40} ║")
    
    print("╚" + "="*50 + "╝")

# Użycie
wyswietl_model('moj_pierwszy_model.onnx')
```

## 🚀 Bardziej Zaawansowane Przykłady

### Przykład 1: Prosty Model Regresji Liniowej
```python
# y = 2x + 3

# Wejście
x = helper.make_tensor_value_info('x', TensorProto.FLOAT, [1])

# Wagi (stałe wartości)
waga = helper.make_tensor(
    name='waga',
    data_type=TensorProto.FLOAT,
    dims=[1],
    vals=[2.0]  # współczynnik kierunkowy
)

bias = helper.make_tensor(
    name='bias',
    data_type=TensorProto.FLOAT,
    dims=[1],
    vals=[3.0]  # wyraz wolny
)

# Operacje
# Krok 1: x * 2
mul_node = helper.make_node('Mul', ['x', 'waga'], ['x_times_waga'])

# Krok 2: (x * 2) + 3
add_node = helper.make_node('Add', ['x_times_waga', 'bias'], ['y'])

# Wyjście
y = helper.make_tensor_value_info('y', TensorProto.FLOAT, [1])

# Graf z inicjalizacją wag
graf = helper.make_graph(
    nodes=[mul_node, add_node],
    name='regresja_liniowa',
    inputs=[x],
    outputs=[y],
    initializer=[waga, bias]  # stałe wartości
)

model = helper.make_model(graf)
onnx.checker.check_model(model)
onnx.save(model, 'regresja_liniowa.onnx')
```

**Nowe koncepty:**
- **Initializer**: Tensory ze stałymi wartościami (wagi, biasy)
- **Sekwencja operacji**: Wynik jednej operacji to wejście kolejnej
- **Nazewnictwo pośrednie**: 'x_times_waga' to tymczasowa zmienna

### Przykład 2: Funkcja Aktywacji ReLU
```python
# ReLU(x) = max(0, x)
# Jeśli x > 0: zwróć x
# Jeśli x <= 0: zwróć 0

x = helper.make_tensor_value_info('x', TensorProto.FLOAT, [5])  # 5 liczb
y = helper.make_tensor_value_info('y', TensorProto.FLOAT, [5])

relu_node = helper.make_node(
    'Relu',  # Wbudowana operacja ONNX
    ['x'],
    ['y']
)

graf = helper.make_graph([relu_node], 'aktywacja_relu', [x], [y])
model = helper.make_model(graf)
onnx.save(model, 'relu.onnx')
```

**Dlaczego ReLU jest ważne:**
- Wprowadza nieliniowość do sieci neuronowych
- Bez nieliniowości nie można modelować złożonych zależności
- Jest bardzo szybkie obliczeniowo

## ⚠️ Typowe Pułapki dla Początkujących

### Pułapka 1: Niezgodne kształty
```python
# ❌ ŹLE
a = helper.make_tensor_value_info('a', TensorProto.FLOAT, [3, 2])
b = helper.make_tensor_value_info('b', TensorProto.FLOAT, [2, 5])
# Nie możesz ich dodać! Różne wymiary.

# ✅ DOBRZE
a = helper.make_tensor_value_info('a', TensorProto.FLOAT, [3, 2])
b = helper.make_tensor_value_info('b', TensorProto.FLOAT, [3, 2])
# Teraz można dodać element po elemencie
```

### Pułapka 2: Nieistniejące nazwy
```python
# ❌ ŹLE
node = helper.make_node('Add', ['x', 'y'], ['sum'])
# Ale w grafie nie zdefiniowałeś 'x' i 'y' jako wejść!

# ✅ DOBRZE
x = helper.make_tensor_value_info('x', TensorProto.FLOAT, [1])
y = helper.make_tensor_value_info('y', TensorProto.FLOAT, [1])
node = helper.make_node('Add', ['x', 'y'], ['sum'])
graph = helper.make_graph([node], 'g', [x, y], [...])
# Teraz nazwy się zgadzają
```

### Pułapka 3: Zapomnienie o check_model
```python
# Zawsze sprawdzaj przed zapisem!
model = helper.make_model(graf)
onnx.checker.check_model(model)  # To może uratować Ci godziny debugowania
onnx.save(model, 'model.onnx')
```

## 📚 Dalsze Kroki Nauki

### Poziom 1: Podstawy (jesteś tutaj!)
- ✅ Zrozumienie czym jest ONNX
- ✅ Tworzenie prostych modeli
- ✅ Zapisywanie i wczytywanie

### Poziom 2: Średniozaawansowany
- Konwersja modeli z PyTorch/TensorFlow do ONNX
- Optymalizacja grafów (usuwanie zbędnych operacji)
- Wnioskowanie kształtów (shape inference)
- Praca z rzeczywistymi modelami (ResNet, BERT)

### Poziom 3: Zaawansowany
- Tworzenie własnych operatorów
- Kwantyzacja modeli (redukcja rozmiaru)
- Deployment na urządzeniach embedded
- Optymalizacja wydajności

## 🎯 Ćwiczenia Praktyczne

### Ćwiczenie 1: Kalkulator
Stwórz model ONNX który:
- Przyjmuje 3 liczby: a, b, c
- Oblicza: (a + b) * c
- Zwraca wynik

**Wskazówki:**
- Potrzebujesz 2 węzłów: Add i Mul
- Pamiętaj o pośredniej zmiennej na wynik a+b

### Ćwiczenie 2: Normalizacja
Stwórz model który normalizuje wartość:
- normalized = (x - mean) / std
- Przyjmij mean=5.0, std=2.0

**Wskazówki:**
- Sub (odejmowanie), Div (dzielenie)
- mean i std jako initializers

### Ćwiczenie 3: Dwuwarstwowa Sieć
Stwórz prostą sieć neuronową:
- Wejście: wektor 10 liczb
- Warstwa 1: fully connected (10 → 5) + ReLU
- Warstwa 2: fully connected (5 → 2)
- Wyjście: 2 liczby

**To już wymaga wiedzy o mnożeniu macierzy!**

## 🤝 Potrzebujesz Pomocy?

**Gdzie szukać:**
1. [Dokumentacja oficjalna ONNX](https://onnx.ai/onnx/)
2. [Tutoriale na GitHub](https://github.com/onnx/tutorials)
3. [Stack Overflow z tagiem 'onnx'](https://stackoverflow.com/questions/tagged/onnx)
4. [Slack społeczności LF AI](https://lfaifoundation.slack.com/)

**Jak zadawać dobre pytania:**
- Opisz co chcesz osiągnąć
- Pokaż swój kod
- Opisz błąd który dostajesz
- Podaj wersję ONNX i Python

## 🎊 Podsumowanie

Gratulacje! Teraz wiesz:
- ✅ Czym jest ONNX i dlaczego jest przydatny
- ✅ Jakie są podstawowe komponenty (model, graf, węzły, tensory)
- ✅ Jak stworzyć prosty model od podstaw
- ✅ Jak zapisać i wczytać model
- ✅ Jak sprawdzić poprawność modelu
- ✅ Jakie są typowe błędy początkujących

**Następny krok:** Spróbuj przerobić ćwiczenia praktyczne!

**Pamiętaj:** Każdy ekspert był kiedyś początkującym. Nie zniechęcaj się błędami - są naturalną częścią nauki! 💪

---

*Ten przewodnik został stworzony dla polskich studentów uczących się ONNX. Jeśli masz sugestie ulepszeń, zgłoś issue na GitHubie!*
