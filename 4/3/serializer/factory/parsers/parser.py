"""
Base Parser class
"""
import io
from abc import ABC, abstractmethod


class Parser(ABC):
    """
    Base parser
    """

    def __init__(self):
        # TODO
        pass

    @abstractmethod
    @staticmethod
    def dump(obj: object, fp: io.IOBase) -> None:
        """
        Prints object to fp
        """

    @abstractmethod
    @staticmethod
    def dumps(obj: object) -> str:
        """
        Returns string with serialized obj
        """

    @abstractmethod
    @staticmethod
    def load(fp: io.IOBase) -> object:
        """
        Returns object serialized from obj
        """

    @abstractmethod
    @staticmethod
    def loads(string: str) -> object:
        """
        Returns object serialized from obj
        """
