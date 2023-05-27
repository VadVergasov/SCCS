"""
Implementing serializer class
"""
import inspect
from typing import Callable
from pydoc import locate

import re
from .constants import (
    TYPE,
    TYPE_ANNOTATION,
    VALUE_ANNOTATION,
    OBJECT_ANNOTATION,
    OBJECT_FIELDS,
    DICT_ANNOTATION,
    FUNCTION_ANNOTATION,
    FUNCTION_ATTRIBUTES,
    CLOSURE,
    CODE,
    GLOBALS,
    NAMES,
    CLASS_ANNOTATION,
    NOT_CLASS_ATTRIBUTES,
    MODULE_ANNOTATION,
)


class Serializer:
    """
    Serializer class
    """

    @staticmethod
    def serialize(obj: object):
        """
        Serialization function
        """
        serializer: Callable[[object], dict[str, object] | None] = Serializer.__get_serializer(obj)
        result = tuple(serializer(obj).items())

        return result

    @staticmethod
    def __get_serializer(obj: object) -> Callable[[object], dict[str, object] | None]:
        """
        Gets serializer for object
        """
        if isinstance(obj, (float, int, complex, bool, str, type(None))):
            return Serializer.__serialize_primitive
        if isinstance(obj, (list, tuple, bytes)):
            return Serializer.__serialize_collection
        if isinstance(obj, dict):
            return Serializer.__serialize_dictionary
        if inspect.isfunction(obj):
            return Serializer.__serialize_function
        if inspect.isclass(obj):
            return Serializer.__serialize_class
        if inspect.iscode(obj):
            return Serializer.__serialize_code
        if inspect.ismodule(obj):
            return Serializer.__serialize_module
        if (
            inspect.ismemberdescriptor(obj)
            or inspect.isbuiltin(obj)
            or inspect.isgetsetdescriptor(obj)
            or inspect.ismethoddescriptor(obj)
            or isinstance(obj, type(type.__dict__))
        ):
            return Serializer.__serialize_instance

        return Serializer.__serialize_object

    @staticmethod
    def __serialize_primitive(obj: object) -> dict[str, object]:
        """
        Serializes primitive type
        """
        serialized_primitive: dict[str, object] = {}
        serialized_primitive[TYPE_ANNOTATION] = re.search(TYPE, str(type(obj))).group(1)
        serialized_primitive[VALUE_ANNOTATION] = obj

        return serialized_primitive

    @staticmethod
    def __serialize_object(obj: object) -> dict[str, object]:
        """
        Serializes objects
        """
        result: dict[str, object] = {}
        result[TYPE_ANNOTATION] = OBJECT_ANNOTATION
        result[VALUE_ANNOTATION] = tuple(
            {
                Serializer.serialize(OBJECT_ANNOTATION): Serializer.serialize(type(obj)),
                Serializer.serialize(OBJECT_FIELDS): Serializer.serialize(obj.__dict__),
            }.items()
        )

        return result

    @staticmethod
    def __serialize_collection(obj: object) -> dict[str, object]:
        """
        Serializes collections
        """
        result: dict[str, object] = {}
        result[TYPE_ANNOTATION] = re.search(TYPE, str(type(obj))).group(1)
        result[VALUE_ANNOTATION] = tuple(Serializer.serialize(current) for current in obj)

        return result

    @staticmethod
    def __serialize_dictionary(obj: object) -> dict[str, object]:
        """
        Serializes dictionary
        """
        result: dict[str, object] = {}
        result[TYPE_ANNOTATION] = DICT_ANNOTATION
        result[VALUE_ANNOTATION] = tuple(
            (Serializer.serialize(key), Serializer.serialize(value)) for key, value in obj.items()
        )

        return result

    @staticmethod
    def __serialize_function(obj: object) -> dict[str, object]:
        """
        Serializes function
        """
        result: dict[str, object] = {}
        result[TYPE_ANNOTATION] = FUNCTION_ANNOTATION
        value: dict = {}
        for member in [current for current in inspect.getmembers(obj) if current[0] in FUNCTION_ATTRIBUTES]:
            key = Serializer.serialize(member[0])
            val = member[1]
            if member[0] == CLOSURE:
                key = Serializer.serialize(member[0])
                val = None
            elif member[0] == CODE:
                key = Serializer.serialize(GLOBALS)
                val = {}
                for name in member[1].__getattribute__(NAMES):
                    if name == obj.__name__:
                        val[name] = obj.__name__
                    elif (
                        name in obj.__getattribute__(GLOBALS)
                        and not inspect.ismodule(name)
                        and name not in __builtins__
                    ):
                        val[name] = obj.__getattribute__(GLOBALS)[name]
            value[key] = Serializer.serialize(val)
        result[VALUE_ANNOTATION] = tuple(value.items())

        return result

    @staticmethod
    def __serialize_class(obj: object) -> dict[str, object]:
        """
        Serializes class
        """
        result: dict[str, object] = {}
        result[TYPE_ANNOTATION] = CLASS_ANNOTATION
        result[VALUE_ANNOTATION] = tuple(
            (Serializer.serialize(key), Serializer.serialize(value))
            for key, value in [member for member in inspect.getmembers(obj) if member[0] not in NOT_CLASS_ATTRIBUTES]
        )

        return result

    @staticmethod
    def __serialize_code(obj: object) -> dict[str, object] | None:
        """
        Serializes code
        """
        if re.search(TYPE, str(type(obj))) is None:
            return None

        return Serializer.__serialize_instance(obj)

    @staticmethod
    def __serialize_module(obj: object) -> dict[str, object]:
        """
        Serializes module
        """
        result: dict[str, object] = {}
        result[TYPE_ANNOTATION] = MODULE_ANNOTATION
        result[VALUE_ANNOTATION] = re.search(TYPE, str(obj)).group(1)

        return result

    @staticmethod
    def __serialize_instance(obj: object) -> dict[str, object]:
        """
        Serializes instance
        """
        result: dict[str, object] = {}
        result[TYPE_ANNOTATION] = re.search(TYPE, str(type(obj))).group(1)
        result[VALUE_ANNOTATION] = tuple(
            (Serializer.serialize(key), Serializer.serialize(value))
            for key, value in [member for member in inspect.getmembers(obj) if not callable(member[1])]
        )

        return result

    @staticmethod
    def deserialize(obj: dict[str, object]) -> object:
        """
        Deserializes object
        """
        deserializer: Callable[[object, object], object] = Serializer.__create_deserializer(obj[TYPE_ANNOTATION])
        if deserializer is None:
            return None

        return deserializer(obj[TYPE_ANNOTATION], obj[VALUE_ANNOTATION])

    @staticmethod
    def __create_deserializer(object_type) -> Callable[[object, object], object]:
        """
        Returns function for type to deserealize
        """
        if object_type in [
            str(bool.__name__),
            str(str.__name__),
            str(int.__name__),
            str(float.__name__),
            str(complex.__name__),
            str(type(None).__name__),
        ]:
            return Serializer.__deserialize_primitive
        if object_type in [str(list.__name__), str(tuple.__name__), str(bytes.__name__)]:
            return Serializer.__deserialize_collections
        if object_type == MODULE_ANNOTATION:
            return Serializer.__deserialize_module
        if object_type == DICT_ANNOTATION:
            return Serializer.__deserialize_dictionary
        if object_type == OBJECT_ANNOTATION:
            return Serializer.__deserialize_object

    @staticmethod
    def __deserialize_primitive(object_type: object, obj: object | None = None) -> object:
        """
        Deserializes primite
        """
        if object_type == str(type(None).__name__):
            return None
        if object_type == str(type(True).__name__) and isinstance(obj, str):
            return obj == str(True)

        return locate(object_type)(obj)

    @staticmethod
    def __deserialize_collections(object_type: object, obj: object) -> object:
        """
        Deserialized collections
        """
        if object_type == str(tuple.__name__):
            return tuple(Serializer.deserialize(current) for current in obj)
        if object_type == str(bytes.__name__):
            return bytes([Serializer.deserialize(current) for current in obj])

        return [Serializer.deserialize(current) for current in obj]

    @staticmethod
    def __deserialize_module(_, obj: object) -> object:
        """
        Deserializes module
        """
        return __import__(obj)

    @staticmethod
    def __deserialize_dictionary(object_type: object, obj: object) -> object:
        """
        Deserialize dictionary
        """
        return {Serializer.deserialize(current[0]): Serializer.deserialize(current[1]) for current in obj}

    @staticmethod
    def __deserialize_object(object_type: object, obj: object) -> object:
        """
        Deserialize object
        """
        dct = Serializer.__deserialize_dictionary(DICT_ANNOTATION, obj)
        result = dct[OBJECT_ANNOTATION]()
        for key, value in dct[OBJECT_FIELDS].items():
            setattr(result, key, value)

        return result
