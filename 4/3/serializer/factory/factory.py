from serializer.factory.parsers import (
    JSON_NAME,
    XML_NAME,
    ParserJson,
    ParserXml,
)


class Factory(object):
    """
    Factory class to provide parser
    """

    @staticmethod
    def get_parser(parser: str):
        """
        Method to get exact parser
        """
        if parser == JSON_NAME:
            return ParserJson()
        if parser == XML_NAME:
            return ParserXml()
        raise ValueError("Check parser parser")
