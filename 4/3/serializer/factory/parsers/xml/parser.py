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
    def __serialize_to_xml(obj: object) -> str:
        """
        Serializes object to xml
        """
        if isinstance(obj, tuple):
            serialized = []
            for current in obj:
                if isinstance(current, tuple):
                    serialized.append(f"<str>{ParserXml.__serialize_to_xml(current)}</str> ")
                else:
                    serialized.append(f"{ParserXml.__serialize_to_xml(current)}")
            ans = "".join(serialized)
            return f"<{type(obj).__name__}>{ans}</{type(obj).__name__}> "
        else:
            return obj

    @staticmethod
    def __deserialize_xml(obj: str):
        if obj == "<tuple></tuple>":
            return tuple()
        elif obj[:7] == "<tuple>":
            obj = obj[7:-9]
            if obj[-1] == " ":
                obj = obj[:-1]
            parsed = []
            depth = 0
            substr = ""
            for current in obj:
                if current in ("<", ">"):
                    depth += 1
                elif current == "/":
                    depth -= 4
                elif depth == 0:
                    parsed.append(ParserXml.__deserialize_xml(substr))
                    substr = ""
                    continue
                substr += current
            parsed.append(ParserXml.__deserialize_xml(substr))
            return tuple(parsed)
        elif obj[:5] == "<str>":
            parsed = []
            ind = obj.find("</str>")
            if obj[ind + 6 :] != "":
                parsed.append(ParserXml.__deserialize_xml(obj[5:ind]))
                parsed.append(ParserXml.__deserialize_xml(obj[ind + 6 :]))
            else:
                return obj[5:ind]
            return tuple(parsed)
        else:
            return obj

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
        return ParserXml.__serialize_to_xml(obj)

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
        return ParserXml.__deserialize_xml(string)
