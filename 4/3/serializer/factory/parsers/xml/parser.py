"""
XML Parser file
"""
import io

from serializer.factory.parsers.parser import Parser


class ParserXml(Parser):
    """
    XML parser
    """

    @staticmethod
    def dump(obj: object, fp: io.IOBase) -> None:
        """
        Prints object to fp
        """
        fp.write(ParserXml.dumps(obj))

    @staticmethod
    def dumps(obj: object) -> str:
        """
        Returns string with serialized obj
        """
        # TODO

    @staticmethod
    def load(fp: io.IOBase) -> object:
        """
        Returns object serialized from obj
        """
        return ParserXml.loads(fp.read())

    @staticmethod
    def loads(string: str) -> object:
        """
        Returns object serialized from obj
        """
        # TODO
