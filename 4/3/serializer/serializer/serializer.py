import inspect
from typing import Any
from types import FunctionType, ModuleType, CellType
from serializer.constants import (
    PRIMITIVES,
    COLLECTIONS,
    CODE_ATTRIBUTES,
    TYPE,
    VALUE,
    ITERATOR_TYPE,
    IGNORED_CLASS_ATTRIBUTES,
    IGNORED_TYPES,
    IS_ITERABLE,
)


class Serializer:
    @staticmethod
    def serialize(obj: Any) -> dict:
        """
        Method that converts object to the dictionary that represents the object.
        """

        if isinstance(obj, PRIMITIVES):
            return {TYPE: type(obj).__name__, VALUE: str(obj) if isinstance(obj, complex) else obj}

        if isinstance(obj, COLLECTIONS):
            if isinstance(obj, dict):
                return {
                    TYPE: type(obj).__name__,
                    VALUE: [[Serializer.serialize(key), Serializer.serialize(value)] for key, value in obj.items()],
                }
            else:
                return {TYPE: type(obj).__name__, VALUE: [Serializer.serialize(item) for item in obj]}

        if inspect.isfunction(obj):
            return {TYPE: type(obj).__name__, VALUE: Serializer._serialize_function(obj)}

        if inspect.iscode(obj):
            return {
                TYPE: type(obj).__name__,
                VALUE: {
                    key: Serializer.serialize(value) for key, value in inspect.getmembers(obj) if key in CODE_ATTRIBUTES
                },
            }

        if isinstance(obj, CellType):
            return {TYPE: type(obj).__name__, VALUE: Serializer.serialize(obj.cell_contents)}

        if inspect.isclass(obj):
            return {TYPE: "class", VALUE: Serializer._serialize_class(obj)}

        if isinstance(obj, property):
            return {
                TYPE: type(obj).__name__,
                VALUE: {
                    "fget": Serializer.serialize(obj.fget),
                    "fset": Serializer.serialize(obj.fset),
                    "fdel": Serializer.serialize(obj.fdel),
                },
            }

        if IS_ITERABLE(obj):
            return {TYPE: ITERATOR_TYPE, VALUE: [Serializer.serialize(item) for item in obj]}

        if inspect.ismethod(obj):
            return {TYPE: type(obj).__name__, VALUE: Serializer._serialize_function(obj.__func__)}

        return {
            TYPE: "object",
            VALUE: {
                "__class__": Serializer.serialize(obj.__class__),
                "__vars__": {key: Serializer.serialize(value) for key, value in vars(obj).items()},
            },
        }

    @staticmethod
    def _serialize_function(obj: FunctionType, cls=None):
        return {
            "__name__": obj.__name__,
            "__globals__": Serializer._serialize_globals(obj, cls),
            "__closure__": Serializer.serialize(obj.__closure__),
            "__defaults__": Serializer.serialize(obj.__defaults__),
            "__kwdefaults__": Serializer.serialize(obj.__kwdefaults__),
            "__code__": {
                key: Serializer.serialize(value) for key, value in inspect.getmembers(obj.__code__) if key in CODE_ATTRIBUTES
            },
        }

    @staticmethod
    def _serialize_globals(obj, cls=None):
        globs = {}

        for key, value in obj.__globals__.items():
            if key not in obj.__code__.co_names:
                continue

            if isinstance(value, ModuleType):
                globs[f"module {key}"] = Serializer.serialize(key)

            elif inspect.isclass(value):
                if cls and value != cls or not cls:
                    globs[key] = Serializer.serialize(value)

            elif key == obj.__code__.co_name:
                globs[key] = Serializer.serialize(obj.__name__)

            else:
                globs[key] = Serializer.serialize(value)

        return globs

    @staticmethod
    def _serialize_class(obj):
        serializeed = {}
        serializeed["__name__"] = Serializer.serialize(obj.__name__)

        for key, value in obj.__dict__.items():
            if key in IGNORED_CLASS_ATTRIBUTES or type(value) in IGNORED_TYPES:
                continue

            if isinstance(obj.__dict__[key], staticmethod):
                serializeed[key] = {}
                serializeed[key]["type"] = "staticmethod"
                serializeed[key]["value"] = {"type": "function", "value": Serializer._serialize_function(value.__func__, obj)}

            elif isinstance(obj.__dict__[key], classmethod):
                serializeed[key] = {}
                serializeed[key]["type"] = "classmethod"
                serializeed[key]["value"] = {"type": "function", "value": Serializer._serialize_function(value.__func__, obj)}

            elif inspect.ismethod(value):
                serializeed[key] = Serializer._serialize_function(value.__func__, obj)

            elif inspect.isfunction(value):
                serializeed[key] = {}
                serializeed[key]["type"] = "function"
                serializeed[key]["value"] = Serializer._serialize_function(value, obj)

            else:
                serializeed[key] = Serializer.serialize(value)

        serializeed["__bases__"] = {}
        serializeed["__bases__"]["type"] = "tuple"
        serializeed["__bases__"]["value"] = [Serializer.serialize(item) for item in obj.__bases__ if item != object]

        return serializeed
