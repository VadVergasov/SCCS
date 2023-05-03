"""
Constants for Serializer class
"""
TYPE = r"\'(\w+)\'"

OBJECT_FIELDS = "__fields__"

CLOSURE = "__closure__"
CODE = "__code__"
GLOBALS = "__globals__"
NAMES = "co_names"
FUNCTION_ATTRIBUTES = ["__code__", "__name__", "__defaults__", "__closure__"]
NOT_CLASS_ATTRIBUTES = ["__class__", "__getattribute__", "__new__", "__setattr__"]

CLASS_ANNOTATION = "class"
DICT_ANNOTATION = "dict"
FUNCTION_ANNOTATION = "function"
OBJECT_ANNOTATION = "__object_name__"
TYPE_ANNOTATION = "type"
VALUE_ANNOTATION = "value"
MODULE_ANNOTATION = "__module__name__"
