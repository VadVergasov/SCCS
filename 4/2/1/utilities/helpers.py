"""
Help function for working with text
"""
from itertools import chain

def split_to_sentences(text: str) -> list[str]:
    """
    Function splits text into sentences
    """
    # TODO


def split_to_words(sentence: str) -> list[str]:
    """
    Function splits sentence into words
    """
    # TODO


def get_non_declarative_sentences_count(text: str) -> int:
    """
    Function counts non declarative sentences
    """
    sentences = split_to_sentences(text)
    result: int = len([
        sentence for sentence in sentences
        if not (sentence.endswith('.') or sentence.endswith('...'))
    ])
    return result


def get_average_words_count(text: str) -> float:
    """
    Function counts average sententece length
    """
    sentences = split_to_sentences(text)
    word_count: int = 0
    for sentence in sentences:
        word_count += len(split_to_words(sentence))
    return word_count / len(sentences)


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
    words = list(
        chain.from_iterable(
            [split_to_words(sentence) for sentence in split_to_sentences(text)]
        )
    )
    n_grams = [
        ' '.join(slice) for slice in [
            words[pos:pos + n] for pos in range(len(words) - n)
        ]
    ]
    count: dict[str, int] = {}
    for n_gram in n_grams:
        if count.get(n_gram, None) is not None:
            count[n_gram] += 1
        else:
            count.update({n_gram: 1})
    result = list(
        dict(
            reversed(sorted(count.items(), key=lambda item: item[1]))
        ).items()
    )
    return result[:k]
