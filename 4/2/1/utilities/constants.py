"""
File with constants
"""

ABBREVIATIONS: list[str] = [
    "Mr.",
    "Mrs.",
    "Ph.D.",
    "Lt.",
    "Rep.",
    "Dr.",
    "B.A.",
    "a.m.",
]

SENTENCE_REGEX = r"(?:(?:\w+)(?:[^\w\.!?]+|[\.!?\.\.\.]))+"

WORD_REGEX  = r"([\w’']+)"
