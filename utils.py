import re


def strip_punctuation(text):
    """replaces non-word characters by space characters"""
    return re.sub(r'\W', ' ', text)


def text_to_words(text):
    """split text into words while treating non-word characters as whitespaces"""
    text_no_punctuation = strip_punctuation(text)
    words = text_no_punctuation.split()
    return words


def words_to_lowercase(words):
    """converts the list of words to lowercase"""
    return list(map(str.lower, words))


def jaccard_similarity_score(items1, items2):
    """computes the Jaccard similarity score between items1 and items2"""
    intersection = set(items1) & set(items2)
    union = set(items1) | set(items2)
    return len(intersection)/len(union) if union else 0.0

