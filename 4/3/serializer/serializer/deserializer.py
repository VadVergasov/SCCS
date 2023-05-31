from types import FunctionType, CodeType, CellType, MethodType
import inspect
import builtins
from serializer.constants import (
    PRIMITIVES,
    COLLECTIONS,
    CODE_ATTRIBUTES,
    TYPE,
    VALUE,
    METHOD_DECORATORS,
    ITERATOR_TYPE,
)


class Deserializer:
    @staticmethod
    def deserialize(obj: dict):
        """
        Method that converts dictionary that represents the object to object.
        """

        if obj[TYPE] in tuple(map(lambda p: p.__name__, PRIMITIVES)):
            if obj[TYPE] == str(type(None).__name__):
                return None
            return getattr(builtins, obj[TYPE])(obj[VALUE])

        if obj[TYPE] in tuple(map(lambda c: c.__name__, COLLECTIONS)):
            if obj[TYPE] == dict.__name__:
                return {Deserializer.deserialize(item[0]): Deserializer.deserialize(item[1]) for item in obj[VALUE]}
            return getattr(builtins, obj[TYPE])(Deserializer.deserialize(item) for item in obj[VALUE])

        if obj[TYPE] in [FunctionType.__name__, MethodType.__name__]:
            return Deserializer._unpack_function(obj[VALUE])

        if obj[TYPE] == CodeType.__name__:
            return Deserializer._unpack_code(obj[VALUE])

        if obj[TYPE] == CellType.__name__:
            return CellType(Deserializer.deserialize(obj[VALUE]))

        if obj[TYPE] == "class":
            return Deserializer._unpack_class(obj[VALUE])

        if obj[TYPE] in tuple(map(lambda md: md.__name__, METHOD_DECORATORS)):
            return getattr(builtins, obj[TYPE])(Deserializer.deserialize(obj[VALUE]))

        if obj[TYPE] == property.__name__:
            return property(
                fget=Deserializer.deserialize(obj[VALUE]["fget"]),
                fset=Deserializer.deserialize(obj[VALUE]["fset"]),
                fdel=Deserializer.deserialize(obj[VALUE]["fdel"]),
            )

        if obj[TYPE] == ITERATOR_TYPE:
            return iter(Deserializer.deserialize(item) for item in obj[VALUE])

        return Deserializer._unpack_object(obj[VALUE])

    @staticmethod
    def _unpack_function(obj: dict):
        code = Deserializer._unpack_code(obj["__code__"])

        globs = Deserializer._unpack_globals(obj["__globals__"], obj)
        globs["builtins"] = __import__("builtins")

        closure = Deserializer.deserialize(obj["__closure__"])
        closure = tuple(closure) if closure else tuple()

        unpacked = FunctionType(code=code, globals=globs, closure=closure)
        unpacked.__globals__.update({unpacked.__name__: unpacked})
        unpacked.__defaults__ = Deserializer.deserialize(obj["__defaults__"])
        unpacked.__kwdefaults__ = Deserializer.deserialize(obj["__kwdefaults__"])

        return unpacked

    @staticmethod
    def _unpack_globals(globs, func):
        unpacked = dict()

        for key, value in globs.items():
            if "module" in key:
                unpacked[value[VALUE]] = __import__(value[VALUE])

            elif value != func["__name__"]:
                unpacked[key] = Deserializer.deserialize(value)

        return unpacked

    @staticmethod
    def _unpack_class(obj):
        attrs = {member: Deserializer.deserialize(value) for member, value in obj.items()}

        cls = type(Deserializer.deserialize(obj["__name__"]), Deserializer.deserialize(obj["__bases__"]), attrs)

        for value in attrs.values():
            if inspect.isfunction(value):
                value.__globals__.update({cls.__name__: cls})
            elif isinstance(value, (staticmethod, classmethod)):
                value.__func__.__globals__.update({cls.__name__: cls})

        return cls

    @staticmethod
    def _unpack_object(obj):
        unpacked = object.__new__(Deserializer.deserialize(obj["__class__"]))
        unpacked.__dict__ = {key: Deserializer.deserialize(value) for key, value in obj["__vars__"].items()}

        return unpacked

    @staticmethod
    def _unpack_code(code):
        return CodeType(*(Deserializer.deserialize(code[ATTRIBUTE]) for ATTRIBUTE in CODE_ATTRIBUTES))
