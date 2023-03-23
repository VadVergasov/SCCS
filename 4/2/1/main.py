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


def main() -> None:
    """
    Entry point for this task
    """
    try:
        with open(os.path.join("data", "text.txt"), "r", encoding="utf8") as fp:
            text = fp.read()
    except FileNotFoundError:
        print("No text.txt file, nothing to analyze!")
        sys.exit(1)

    print(get_non_declarative_sentences_count(text))
    print(get_average_words_count(text))
    print(get_average_word_length(text))

    try:
        n, k = map(int, input("Enter n and k (or interrupt input to use n=4 and k=10): ").split())
        print(get_top_k_n_grams(text, k, n))
    except (KeyboardInterrupt, EOFError, ValueError):
        print(get_top_k_n_grams(text))


if __name__ == "__main__":
    main()
