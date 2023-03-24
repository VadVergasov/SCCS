"""
Testing helpers module
"""
from utilities.helpers import (
    split_to_sentences,
    split_to_words,
    get_average_word_length,
    get_average_words_count,
    get_non_declarative_sentences_count,
    get_top_k_n_grams,
)


def test_split_to_sentences():
    """
    Testing splitting to sentences
    """
    text = "Oh, John! If only our cow weren’t going dry I would."
    assert [
        "Oh, John!",
        "If only our cow weren’t going dry I would.",
    ] == split_to_sentences(text)


def test_split_to_words():
    """
    Testing splitting to words
    """
    sentence = "If only our cow weren’t going dry I would."
    assert [
        "If",
        "only",
        "our",
        "cow",
        "weren’t",
        "going",
        "dry",
        "I",
        "would",
    ] == split_to_words(sentence)


def test_get_average_word_length():
    """
    Testing function to get average word length
    """
    text = "Oh, John! If only our cow weren’t going dry I would."
    assert abs(3.5454545454545454 - get_average_word_length(text)) < 1e-6


def test_get_average_sentence_length():
    """
    Testing function to get average sentence length
    """
    text = "Oh, John! If only our cow weren’t going dry I would."
    assert abs(19.5 - get_average_words_count(text)) < 1e-6


def test_get_non_declarative_sentence_count():
    """
    Testing function of counting non declarative sentences
    """
    text = "How providential that it came before Christmas! She interrupted. I’m crazy to see what’s in it! Aren’t you?"
    assert 3 == get_non_declarative_sentences_count(text)


def test_top_k_n_grams():
    """
    Testing function of getting k top of n-grams
    """
    text = "How providential that it came before Christmas! She interrupted. I’m crazy to see what’s in it! Aren’t you?"
    assert [("it", 2)] == get_top_k_n_grams(text, 1, 1)
    assert [("it Aren’t", 1)] == get_top_k_n_grams(text, 1, 2)
    assert [("it", 2), ("Aren’t", 1)] == get_top_k_n_grams(text, 2, 1)
