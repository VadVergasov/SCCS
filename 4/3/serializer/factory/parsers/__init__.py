"""
Init file of parser module
"""
from .constants import JSON_NAME, TOML_NAME, XML_NAME, YAML_NAME
from .json import ParserJson
from .toml import ParserToml
from .yaml import ParserYaml
from .xml import ParserXml
