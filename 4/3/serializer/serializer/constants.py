"""
Constants for Serializer class
"""
OBJECT_FIELDS = "__fields__"

CLOSURE = "__closure__"
CODE = "__code__"
GLOBALS = "__globals__"
BUILTINS = "__builtins__"
DOC = "__doc__"
NAMES = "co_names"
FUNCTION_ATTRIBUTES = ["__code__", "__name__", "__defaults__", "__closure__"]
NOT_CLASS_ATTRIBUTES = ["__class__", "__getattribute__", "__new__", "__setattr__"]
CODE_OBJECT_ARGS = [
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
    "co_firstlineno",
    "co_lnotab",
    "co_freevars",
    "co_cellvars",
]

CLASS_ANNOTATION = "class"
DICT_ANNOTATION = "dict"
FUNCTION_ANNOTATION = "function"
OBJECT_ANNOTATION = "__object_name__"
TYPE_ANNOTATION = "type"
VALUE_ANNOTATION = "value"
MODULE_ANNOTATION = "__module__name__"
NAME_NAME = "__name__"
