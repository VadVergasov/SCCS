"""
JSON Parser file
"""
import io

from serializer.factory.parsers.parser import Parser


class ParserJson(Parser):
    """
    JSON parser
    """

    def dump(self, obj: object, fp: io.IOBase) -> None:
        """
        Prints object to fp
        """
        fp.write(self.dumps(obj))

    @staticmethod
    def dumps(obj: object) -> str:
        """
        Returns string with serialized obj
        """
        # TODO
        pass

    @staticmethod
    def load(fp: io.IOBase) -> object:
        """
        Returns object serialized from obj
        """
        return self.loads(fp.read())

    @staticmethod
    def loads(string: str) -> object:
        """
        Returns object serialized from obj
        """
        # TODO
        pass
