"""
JSON Parser file
"""
import io

from serializer.factory.parsers.parser import Parser

from serializer.serializer.serializer import Serializer


class ParserJson(Parser):
    """
    JSON parser
    """

    @staticmethod
    def __serialize_json(obj: object) -> str:
        """
        Serializes to json format
        """
        if type(obj) == tuple:
            serialized = []
            for current in obj:
                serialized.append(f"{ParserJson.__serialize_json(current)}")
            return f"[{', '.join(serialized)}]"
        else:
            return f'"{str(obj)}"'

    @staticmethod
    def __deserialize_json(obj: str) -> object:
        if obj == "[]":
            return tuple()
        if obj[0] == "[":
            obj = obj[1 : len(obj) - 1]
            deserialized_obj = []
            depth = 0
            is_quote = False
            substr = ""
            for i in obj:
                if i == "[":
                    depth += 1
                elif i == "]":
                    depth -= 1
                elif i == '"':
                    is_quote = not is_quote
                elif i == "," and not is_quote and depth == 0:
                    deserialized_obj.append(ParserJson.__deserialize_json(substr))
                    substr = ""
                    continue
                elif i == " " and not is_quote:
                    continue
                substr += i
            deserialized_obj.append(ParserJson.__deserialize_json(substr))
            return tuple(deserialized_obj)
        return obj[1 : len(obj) - 1]

    @staticmethod
    def dump(obj: object, fp: io.IOBase) -> None:
        """
        Prints object to fp
        """
        fp.write(ParserJson.dumps(obj))

    @staticmethod
    def dumps(obj: object) -> str:
        """
        Returns string with serialized obj
        """
        serialized = Serializer.serialize(obj)
        return ParserJson.__serialize_json(serialized).replace("\n", "\\n")

    @staticmethod
    def load(fp: io.IOBase) -> object:
        """
        Returns object serialized from obj
        """
        return ParserJson.loads(fp.read())

    @staticmethod
    def loads(string: str) -> object:
        """
        Returns object serialized from obj
        """
        obj = ParserJson.__deserialize_json(string)
        return Serializer.deserialize(obj)
