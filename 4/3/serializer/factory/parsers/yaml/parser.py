"""
YAML Parser file
"""
import io

from serializer.factory.parsers.parser import Parser


class ParserYaml(Parser):
    """
    YAML parser
    """

    def dump(self, obj: object, fp: io.IOBase) -> None:
        """
        Prints object to fp
        """
        fp.write(self.dumps(obj))

    def dumps(self, obj: object) -> str:
        """
        Returns string with serialized obj
        """
        # TODO
        pass

    def load(self, fp: io.IOBase) -> object:
        """
        Returns object serialized from obj
        """
        return self.loads(fp.read())

    def loads(self, string: str) -> object:
        """
        Returns object serialized from obj
        """
        # TODO
        pass
