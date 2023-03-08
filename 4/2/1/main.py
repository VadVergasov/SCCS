"""
Main code for this task
"""
import os
import sys

from utilities.helpers import (
    get_average_word_length,
    get_average_words_count,
    get_non_declarative_sentences_count,
    get_top_k_n_grams,
)

abbreviations = []

try:
    with open(os.path.join("/data", "text.txt"), "r", encoding="utf8") as fp:
        text = fp.read()
except FileNotFoundError:
    print("No text.txt file, nothing to analyze!")
    sys.exit(1)

print(get_non_declarative_sentences_count(text))
print(get_average_words_count(text))
print(get_average_word_length(text))
print(get_top_k_n_grams(text))
