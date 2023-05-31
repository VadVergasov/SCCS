"""
XML Parser file
"""
import io
import regex
import builtins

from serializer.factory.parsers.parser import Parser

from serializer.constants import PRIMITIVES, XmlRegularExpression as Expression, KEY, VALUE
from serializer.serializer import Serializer, Deserializer


class ParserXml(Parser):
    """
    XML parser
    """

    @staticmethod
    def __create_xml_item(tag_name, value):
        return f"<{tag_name}>{value}</{tag_name}>"

    @staticmethod
    def __to_special_xml(string):
        return (
            string.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
            .replace("'", "&apos;")
        )

    @staticmethod
    def __from_special_xml(string):
        return (
            string.replace("&amp;", "&")
            .replace("&lt;", "<")
            .replace("&gt;", ">")
            .replace("&quot;", '"')
            .replace("&apos;", "'")
        )

    @staticmethod
    def __serialize_to_xml(obj: object) -> str:
        """
        Serializes object to xml
        """
        if isinstance(obj, PRIMITIVES):
            if isinstance(obj, str):
                return ParserXml.__create_xml_item(type(obj).__name__, ParserXml.__to_special_xml(obj))
            else:
                return ParserXml.__create_xml_item(type(obj).__name__, str(obj))

        if isinstance(obj, list):
            return ParserXml.__create_xml_item(
                type(obj).__name__, "".join([ParserXml.__serialize_to_xml(item) for item in obj])
            )

        return ParserXml.__create_xml_item(
            type(obj).__name__,
            "".join(
                [
                    f"{ParserXml.__serialize_to_xml(key)}{ParserXml.__serialize_to_xml(value)}"
                    for key, value in obj.items()
                ]
            ),
        )

    @staticmethod
    def __deserialize_xml(string: str):
        string = string.strip()

        match = regex.fullmatch(Expression.ITEM.value, string)
        if not match:
            return

        key = match.group(KEY)
        value = match.group(VALUE)

        if key in map(lambda p: p.__name__, PRIMITIVES):
            if key == str.__name__:
                return ParserXml.__from_special_xml(value)
            if key == type(None).__name__:
                return None
            if key == bool.__name__:
                return value == "True"
            return getattr(builtins, key)(value)

        if key == list.__name__:
            matches = regex.findall(Expression.ITEM.value, value)
            return [ParserXml.__deserialize_xml(match[0]) for match in matches]

        if key == dict.__name__:
            matches = regex.findall(Expression.ITEM.value, value)
            return {
                ParserXml.__deserialize_xml(matches[i][0]): ParserXml.__deserialize_xml(matches[i + 1][0])
                for i in range(0, len(matches), 2)
            }

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
        return ParserXml.__serialize_to_xml(Serializer.serialize(obj))

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
        return Deserializer.deserialize(ParserXml.__deserialize_xml(string))
