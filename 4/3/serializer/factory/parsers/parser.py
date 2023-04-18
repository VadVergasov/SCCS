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
    def dump(self, obj: object, fp: io.IOBase) -> None:
        """
        Prints object to fp
        """
        pass

    @abstractmethod
    def dumps(self, obj: object) -> str:
        """
        Returns string with serialized obj
        """
        pass

    @abstractmethod
    def load(self, fp: io.IOBase) -> object:
        """
        Returns object serialized from obj
        """
        pass

    @abstractmethod
    def loads(self, string: str) -> object:
        """
        Returns object serialized from obj
        """
        pass
