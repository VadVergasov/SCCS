"""
JSON Parser file
"""
import io
import regex

from serializer.factory.parsers.parser import Parser

from serializer.constants import PRIMITIVES, JsonRegularExpression as Expression
from serializer.serializer import Serializer, Deserializer


class ParserJson(Parser):
    """
    JSON parser
    """

    @staticmethod
    def __serialize_json(obj: object) -> str:
        """
        Serializes to json format
        """
        if isinstance(obj, PRIMITIVES):
            if isinstance(obj, str):
                return '"' + obj.replace("\\", "\\\\").replace('"', '"').replace("'", "'") + '"'
            return str(obj)

        if isinstance(obj, list):
            return "[" + ", ".join([ParserJson.__serialize_json(item) for item in obj]) + "]"

        return (
            "{"
            + ", ".join(
                [
                    f"{ParserJson.__serialize_json(key)}: {ParserJson.__serialize_json(value)}"
                    for key, value in obj.items()
                ]
            )
            + "}"
        )

    @staticmethod
    def __deserialize_json(string: str) -> object:
        string = string.strip()

        if regex.fullmatch(Expression.INT.value, string):
            return int(string)

        if regex.fullmatch(Expression.STR.value, string):
            string = string.replace("\\\\", "\\").replace(r"\"", '"').replace(r"\'", "'")
            return string[1:-1]

        if regex.fullmatch(Expression.FLOAT.value, string):
            return float(string)

        if regex.fullmatch(Expression.BOOL.value, string):
            return string == "True"

        if regex.fullmatch(Expression.NONE.value, string):
            return None

        if string.startswith("[") and string.endswith("]"):
            string = string[1:-1]
            matches = regex.findall(Expression.ANY_VALUE.value, string)
            return [ParserJson.__deserialize_json(match[0]) for match in matches]

        if string.startswith("{") and string.endswith("}"):
            string = string[1:-1]
            matches = regex.findall(Expression.ANY_VALUE.value, string)
            return {
                ParserJson.__deserialize_json(matches[i][0]): ParserJson.__deserialize_json(matches[i + 1][0])
                for i in range(0, len(matches), 2)
            }

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
        return ParserJson.__serialize_json(serialized)

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
        return Deserializer.deserialize(obj)
