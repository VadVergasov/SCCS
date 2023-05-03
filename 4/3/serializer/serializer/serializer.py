"""
Implementing serializer class
"""
import inspect
from typing import Callable

import re
from .constants import (
    TYPE,
    TYPE_ANNOTATION,
    VALUE_ANNOTATION,
    OBJECT_ANNOTATION,
    OBJECT_TYPE,
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
                Serializer.serialize(OBJECT_TYPE): Serializer.serialize(type(obj)),
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
        result: dict[str, object] = {}
        result[TYPE_ANNOTATION] = re.search(TYPE, str(type(obj))).group(1)
        result[VALUE_ANNOTATION] = tuple(
            (Serializer.serialize(key), Serializer.serialize(value))
            for key, value in [member for member in inspect.getmembers(obj) if not callable(member[1])]
        )

        return result
