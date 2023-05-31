"""
Constants for Serializer class
"""
import types
import enum

KEY = "key"
TYPE = "type"
VALUE = "value"

PRIMITIVES = (int, float, bool, str, type(None), complex)
COLLECTIONS = (set, dict, list, tuple, bytes, bytearray)

CODE_ATTRIBUTES = (
    "co_argcount",
    "co_posonlyargcount",
    "co_kwonlyargcount",
    "co_nlocals",
    "co_stacksize",
    "co_flags",
    "co_code",
    "co_consts",
    "co_names",
    "co_varnames",
    "co_filename",
    "co_name",
    "co_qualname",
    "co_firstlineno",
    "co_lnotab",
    "co_exceptiontable",
    "co_freevars",
    "co_cellvars",
)

IGNORED_CLASS_ATTRIBUTES = ("__name__", "__base__", "__basicsize__", "__dictoffset__", "__class__")

IGNORED_TYPES = (
    types.WrapperDescriptorType,
    types.MethodDescriptorType,
    types.BuiltinFunctionType,
    types.GetSetDescriptorType,
    types.MappingProxyType,
)

METHOD_DECORATORS = (classmethod, staticmethod)

ITERATOR_TYPE = "iterator"


class JsonRegularExpression(enum.Enum):
    INT = r"[+-]?\d+"
    FLOAT = rf"({INT}(?:\.\d+)?(?:e{INT})?)"
    BOOL = r"((True)|(False))\b"
    STR = r"\"((\\\")|[^\"])*\""
    NONE = r"\b(None)\b"
    COMPLEX = rf"{FLOAT}{FLOAT}j"

    LIST_RECURSION = r"\[(?R)?(,(?R))*\]"
    DICT_RECURSION = r"\{((?R):(?R))?(?:,(?R):(?R))*\}"

    ANY_VALUE = (
        rf"\s*({LIST_RECURSION}|"
        rf"{DICT_RECURSION}|"
        rf"{STR}|"
        rf"{FLOAT}|"
        rf"{BOOL}|"
        rf"{INT}|"
        rf"{NONE}|"
        rf"{COMPLEX}\s*)"
    )


class XmlRegularExpression(enum.Enum):
    TYPES = "|".join(map(lambda x: x.__name__, list(PRIMITIVES) + [list, dict]))
    ITEM = rf"\s*(\<(?P<{KEY}>{TYPES})\>(?P<{VALUE}>([^<>]*)|(?R)+)\</({TYPES})\>)\s*"


def IS_ITERABLE(obj):
    return hasattr(obj, "__iter__") and hasattr(obj, "__next__") and callable(obj.__iter__)
