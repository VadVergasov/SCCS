"""
Help function for working with text
"""
import re
from itertools import chain

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


def split_to_sentences(text: str) -> list[str]:
    """
    Function splits text into sentences
    """
    sentences: list[str] = re.findall(
        r"(?:(?:\w+)(?:[^a-zA-Z0-9\.!?]+|[\.!?\.\.\.]))+", text
    )
    result: list[str] = sentences
    for sentence in sentences:
        for abbreviation in ABBREVIATIONS:
            if sentence.endswith(abbreviation):
                index = result.index(sentence)
                result[index] = " ".join(result[index : index + 2])
                result.remove(result[index + 1])
    return result


def split_to_words(sentence: str) -> list[str]:
    """
    Function splits sentence into words
    """
    words: list[str] = re.findall(r"([\w’']+)", sentence)
    words = [word for word in words if not word.isdigit()]
    return words


def get_non_declarative_sentences_count(text: str) -> int:
    """
    Function counts non declarative sentences
    """
    sentences = split_to_sentences(text)
    result: int = len(
        [
            sentence
            for sentence in sentences
            if not (sentence.endswith(".") or sentence.endswith("..."))
        ]
    )
    return result


def get_average_words_count(text: str) -> float:
    """
    Function counts average sententece length
    """
    sentences = split_to_sentences(text)
    symbols_count: int = 0
    for sentence in sentences:
        for word in split_to_words(sentence):
            symbols_count += len(word)
    return symbols_count / len(sentences)


def get_average_word_length(text: str) -> float:
    """
    Function calculates average word length
    """
    char_count: int = 0
    word_count: int = 0
    for sentence in split_to_sentences(text):
        words = split_to_words(sentence)
        word_count += len(words)
        for word in words:
            char_count += len(word)
    return char_count / word_count


def get_top_k_n_grams(text: str, k: int = 10, n: int = 4) -> list[tuple[str, int]]:
    """
    Function returns top-K repeated N-grams in the text
    """
    words: list[str] = list(
        chain.from_iterable(
            [split_to_words(sentence) for sentence in split_to_sentences(text)]
        )
    )
    n_grams: list[str] = [
        " ".join(slice)
        for slice in [words[pos : pos + n] for pos in range(len(words) - n)]
    ]
    count: dict[str, int] = {}
    for n_gram in n_grams:
        if count.get(n_gram, None) is not None:
            count[n_gram] += 1
        else:
            count.update({n_gram: 1})
    result: list[tuple[str, int]] = list(
        dict(reversed(sorted(count.items(), key=lambda item: item[1]))).items()
    )
    return result[:k]
