"""
Base Parser class
"""
import io
from abc import ABC, abstractmethod


class Parser(ABC):
    """
    Base parser
    """

    @staticmethod
    @abstractmethod
    def dump(obj: object, fp: io.IOBase) -> None:
        """
        Prints object to fp
        """

    @staticmethod
    @abstractmethod
    def dumps(obj: object) -> str:
        """
        Returns string with serialized obj
        """

    @staticmethod
    @abstractmethod
    def load(fp: io.IOBase) -> object:
        """
        Returns object serialized from obj
        """

    @staticmethod
    @abstractmethod
    def loads(string: str) -> object:
        """
        Returns object serialized from obj
        """
