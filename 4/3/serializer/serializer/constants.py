"""
Constants for Serializer class
"""
TYPE = r"\'(\w+)\'"

OBJECT_TYPE = "__type__"
OBJECT_FIELDS = "__fields__"

CLOSURE = "__closure__"
CODE = "__code__"
GLOBALS = "__globals__"
NAMES = "co_names"
FUNCTION_ATTRIBUTES = ["__code__", "__name__", "__defaults__", "__closure__"]

DICT_ANNOTATION = "dict"
FUNCTION_ANNOTATION = "function"
OBJECT_ANNOTATION = "object"
TYPE_ANNOTATION = "type"
VALUE_ANNOTATION = "value"
