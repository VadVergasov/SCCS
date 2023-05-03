"""
Implementing serializer class
"""
import inspect
from typing import Callable

import re
from .constants import TYPE, TYPE_ANNOTATION, VALUE_ANNOTATION, OBJECT_ANNOTATION, OBJECT_TYPE, OBJECT_FIELDS


class Serializer:
    """
    Serializer class
    """

    @staticmethod
    def serialize(obj: object):
        """
        Serialization function
        """
        serializer: Callable[[object], dict[str, object]] = Serializer.__get_serializer(obj)
        result = tuple(serializer(obj).items())

        return result

    @staticmethod
    def __get_serializer(obj: object) -> Callable[[object], dict[str, object]]:
        """
        Gets serializer for object
        """
        if isinstance(obj, (float, int, complex, bool, str, type(None))):
            return Serializer.__serialize_primitive
        if isinstance(obj, (list, tuple, bytes)):
            return Serializer.__serialize_collection

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
