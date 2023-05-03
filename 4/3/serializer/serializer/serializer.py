"""
Implementing serializer class
"""
import inspect
from typing import Callable

import re
from .constants import TYPE, TYPE_ANNOTATION, VALUE_ANNOTATION, OBJECT_ANNOTATION


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
        result = tuple((key, value) for key, value in serializer(obj).items())

        return result

    @staticmethod
    def __get_serializer(obj: object) -> Callable[[object], dict[str, object]]:
        """
        Gets serializer for object
        """
        if isinstance(obj, (float, int, complex, bool, str, type(None))):
            return Serializer.__serialize_primitive

    @staticmethod
    def __serialize_primitive(obj: object) -> dict[str, object]:
        """
        Serializes primitive type
        """
        serialized_primitive: dict[str, object] = {}
        serialized_primitive[TYPE_ANNOTATION] = re.search(TYPE, str(type(obj))).group(1)
        serialized_primitive[VALUE_ANNOTATION] = obj

        return serialized_primitive
