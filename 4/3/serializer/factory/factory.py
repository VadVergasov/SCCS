from serializer.factory.parsers import (
    JSON_NAME,
    TOML_NAME,
    XML_NAME,
    YAML_NAME,
    ParserJson,
    ParserToml,
    ParserXml,
    ParserYaml,
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
        if parser == TOML_NAME:
            return ParserToml()
        if parser == YAML_NAME:
            return ParserYaml()
        if parser == XML_NAME:
            return ParserXml()
        raise ValueError("Check parser parser")
