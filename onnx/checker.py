# Copyright (c) ONNX Project Contributors
#
# SPDX-License-Identifier: Apache-2.0
"""
Narzędzia do walidacji modeli ONNX - Przewodnik dla studentów

Ten moduł sprawdza czy modele ONNX są poprawne pod względem:
- Struktury danych (czy wszystkie pola są wypełnione prawidłowo)
- Semantyki (czy operacje mają sens, np. zgodne wymiary tensorów)
- Wersjonowania (czy używane operatory są dostępne w danej wersji)

Główne funkcje walidacyjne:
- check_model() - sprawdza cały model (to zazwyczaj używasz)
- check_graph() - sprawdza tylko graf bez metadanych modelu
- check_node() - sprawdza pojedynczy węzeł (operator)
- check_tensor() - sprawdza poprawność tensorów

Dla studentów: Walidacja to jak sprawdzanie pisowni w Word - wykrywa błędy
zanim spróbujesz uruchomić model na sprzęcie docelowym.
"""

from __future__ import annotations

__all__ = [
    "check_attribute",
    "check_function",
    "check_graph",
    "check_model",
    "check_node",
    "check_sparse_tensor",
    "check_tensor",
    "check_value_info",
    "DEFAULT_CONTEXT",
    "LEXICAL_SCOPE_CONTEXT",
    "ValidationError",
    "C",
    "MAXIMUM_PROTOBUF",
]

import os
import sys
from typing import TYPE_CHECKING

import onnx.defs
import onnx.onnx_cpp2py_export.checker as C  # noqa: N812
from onnx.onnx_pb import IR_VERSION

if TYPE_CHECKING:
    from google.protobuf.message import Message

# Ograniczenie rozmiaru pojedynczego pliku Protobuf to 2GiB
# Dla studentów: To limit techniczny - jeśli Twój model jest większy,
# musisz podzielić wagi na osobne pliki (external data)
MAXIMUM_PROTOBUF = 2147483648


# Kontekst domyślny używany przy walidacji
# Uwaga: Nie modyfikuj tego obiektu - jest współdzielony!
# Dla studentów: Ten obiekt przechowuje informacje o wersji IR (Intermediate Representation)
# i dostępnych operatorach. Każda walidacja używa tych ustawień.
DEFAULT_CONTEXT = C.CheckerContext()
DEFAULT_CONTEXT.ir_version = IR_VERSION
# TODO: Maybe ONNX-ML should also be defaulted?
DEFAULT_CONTEXT.opset_imports = {"": onnx.defs.onnx_opset_version()}

# Kontekst dla sprawdzania zakresu leksykalnego zmiennych
# Dla studentów: Zapewnia, że nazwy zmiennych w grafie są unikalne i używane poprawnie
LEXICAL_SCOPE_CONTEXT = C.LexicalScopeContext()


def _ensure_proto_type(proto: Message, proto_type: type[Message]) -> None:
    """
    Pomocnicza funkcja sprawdzająca typ obiektu Protocol Buffer.
    
    Dla studentów: Protocol Buffer to format serializacji danych używany przez ONNX.
    Ta funkcja po prostu sprawdza czy otrzymaliśmy właściwy typ obiektu
    (np. TensorProto zamiast GraphProto).
    
    Args:
        proto: Obiekt do sprawdzenia
        proto_type: Oczekiwany typ
        
    Raises:
        TypeError: Gdy typ się nie zgadza
    """
    if not isinstance(proto, proto_type):
        raise TypeError(
            f"The proto message needs to be of type '{proto_type.__name__}'"
        )


def check_value_info(
    value_info: onnx.ValueInfoProto, ctx: C.CheckerContext = DEFAULT_CONTEXT
) -> None:
    """
    Sprawdza poprawność informacji o wartości (ValueInfo).
    
    Dla studentów: ValueInfo opisuje tensory w grafie - ich nazwy, typy i kształty.
    Znajdują się w sekcjach inputs/outputs grafu. Ta funkcja weryfikuje czy:
    - Nazwa nie jest pusta
    - Typ jest prawidłowo zdefiniowany (np. FLOAT, INT32)
    - Wymiary kształtu są poprawne (liczby dodatnie lub symbole)
    
    Przykład użycia:
        input_info = helper.make_tensor_value_info('X', TensorProto.FLOAT, [1, 3, 224, 224])
        check_value_info(input_info)  # Sprawdzi poprawność
    """
    _ensure_proto_type(value_info, onnx.ValueInfoProto)
    return C.check_value_info(value_info.SerializeToString(), ctx)


def check_tensor(
    tensor: onnx.TensorProto, ctx: C.CheckerContext = DEFAULT_CONTEXT
) -> None:
    """
    Sprawdza poprawność tensora (wag modelu lub stałych).
    
    Dla studentów: Tensor to wielowymiarowa tablica liczb. W modelach ONNX
    tensory przechowują:
    - Wagi warstw (np. macierze w warstwie Dense)
    - Biasy
    - Stałe wartości używane w obliczeniach
    
    Walidacja sprawdza:
    - Zgodność między typem danych a rzeczywistymi danymi
    - Czy rozmiar danych odpowiada zadeklarowanym wymiarom
    - Czy dane nie są uszkodzone
    """
    _ensure_proto_type(tensor, onnx.TensorProto)
    return C.check_tensor(tensor.SerializeToString(), ctx)


def check_attribute(
    attr: onnx.AttributeProto,
    ctx: C.CheckerContext = DEFAULT_CONTEXT,
    lexical_scope_ctx: C.LexicalScopeContext = LEXICAL_SCOPE_CONTEXT,
) -> None:
    """
    Sprawdza poprawność atrybutu operatora.
    
    Dla studentów: Atrybuty to parametry konfiguracyjne operatorów.
    Przykłady:
    - W operatorze Conv: kernel_shape=[3,3], stride=[1,1], padding='SAME'
    - W operatorze Dropout: ratio=0.5
    - W operatorze Reshape: shape=[-1, 10]
    
    Ta funkcja sprawdza czy:
    - Atrybut ma poprawny typ (int, float, string, tensor, itd.)
    - Wartości są sensowne (np. stride nie może być ujemny)
    - Wymagane atrybuty są obecne
    """
    _ensure_proto_type(attr, onnx.AttributeProto)
    return C.check_attribute(attr.SerializeToString(), ctx, lexical_scope_ctx)


def check_node(
    node: onnx.NodeProto,
    ctx: C.CheckerContext = DEFAULT_CONTEXT,
    lexical_scope_ctx: C.LexicalScopeContext = LEXICAL_SCOPE_CONTEXT,
) -> None:
    """
    Sprawdza poprawność pojedynczego węzła (operatora) w grafie.
    
    Dla studentów: Węzeł (Node) to pojedyncza operacja w modelu, np.:
    - Conv2D (konwolucja)
    - MatMul (mnożenie macierzy)
    - Add (dodawanie)
    - ReLU (funkcja aktywacji)
    
    Każdy węzeł ma:
    - Typ operatora (op_type): np. "Conv", "Add", "Relu"
    - Wejścia (inputs): nazwy tensorów wejściowych
    - Wyjścia (outputs): nazwy tensorów wyjściowych
    - Atrybuty (attributes): parametry konfiguracyjne
    
    Walidacja sprawdza:
    - Czy operator istnieje w danej wersji ONNX
    - Czy liczba wejść/wyjść jest poprawna
    - Czy wszystkie wymagane atrybuty są obecne
    - Czy typy danych są kompatybilne
    """
    _ensure_proto_type(node, onnx.NodeProto)
    return C.check_node(node.SerializeToString(), ctx, lexical_scope_ctx)


def check_function(
    function: onnx.FunctionProto,
    ctx: C.CheckerContext | None = None,
    lexical_scope_ctx: C.LexicalScopeContext = LEXICAL_SCOPE_CONTEXT,
) -> None:
    _ensure_proto_type(function, onnx.FunctionProto)
    if ctx is None:
        ctx = C.CheckerContext()
        ctx.ir_version = onnx.helper.find_min_ir_version_for(
            function.opset_import, ignore_unknown=True
        )
        ctx.opset_imports = {
            domain_version.domain: domain_version.version
            for domain_version in function.opset_import
        }
    C.check_function(function.SerializeToString(), ctx, lexical_scope_ctx)


def check_graph(
    graph: onnx.GraphProto,
    ctx: C.CheckerContext = DEFAULT_CONTEXT,
    lexical_scope_ctx: C.LexicalScopeContext = LEXICAL_SCOPE_CONTEXT,
) -> None:
    _ensure_proto_type(graph, onnx.GraphProto)
    return C.check_graph(graph.SerializeToString(), ctx, lexical_scope_ctx)


def check_sparse_tensor(
    sparse: onnx.SparseTensorProto, ctx: C.CheckerContext = DEFAULT_CONTEXT
) -> None:
    _ensure_proto_type(sparse, onnx.SparseTensorProto)
    C.check_sparse_tensor(sparse.SerializeToString(), ctx)


def check_model(
    model: onnx.ModelProto | str | bytes | os.PathLike,
    full_check: bool = False,
    skip_opset_compatibility_check: bool = False,
    check_custom_domain: bool = False,
) -> None:
    """Check the consistency of a model.

    An exception will be raised if the model's ir_version is not set
    properly or is higher than checker's ir_version, or if the model
    has duplicate keys in metadata_props.

    If IR version >= 3, the model must specify opset_import.
    If IR version < 3, the model cannot have any opset_import specified.

    Args:
        model: Model to check. If model is a path, the function checks model
            path first. If the model bytes size is larger than 2GB, function
            should be called using model path.
        full_check: If True, the function also runs shape inference check.
        skip_opset_compatibility_check: If True, the function skips the check for
            opset compatibility.
        check_custom_domain: If True, the function will check all domains. Otherwise
            only check built-in domains.
    """
    # If model is a path instead of ModelProto
    if isinstance(model, (str, os.PathLike)):
        C.check_model_path(
            os.fspath(model),
            full_check,
            skip_opset_compatibility_check,
            check_custom_domain,
        )
    else:
        protobuf_string = (
            model if isinstance(model, bytes) else model.SerializeToString()
        )
        # If the protobuf is larger than 2GiB,
        # remind users should use the model path to check
        if sys.getsizeof(protobuf_string) > MAXIMUM_PROTOBUF:
            raise ValueError(
                "This protobuf of onnx model is too large (>2GiB). Call check_model with model path instead."
            )
        C.check_model(
            protobuf_string,
            full_check,
            skip_opset_compatibility_check,
            check_custom_domain,
        )


ValidationError = C.ValidationError
