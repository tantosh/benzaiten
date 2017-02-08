import re
from math import log10

def summarize(text):
    sents = sentences(text)


def sentences(text):
    return re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s', text)

def get_similarity(sentence1, sentence2):
    ''' Get how similar are two sentences. '''
    words_s1 = get_words(sentence1)
    words_s2 = get_words(sentence2)

    common_words = set(set(words_s1) & set(words_s2))
    log_words1 = log10(len(words_s1))
    log_words2 = log10(len(words_s2))
    
    similarity = len(list(common_words)) / (log_words1 + log_words2)
    return similarity

def get_words(sentence):
    ''' Clear special symbols in the sentence and return words in list.'''

    sentence = sentence.replace(".", "").replace("!", "").replace("?", "")
    sentence = sentence.replace(",", "").replace(";", "").replace(":", "")
    sentence = sentence.replace("\'", "").replace("\"", "").replace("-", "").replace("_", "").replace("+", "")
    sentence = sentence.replace("(", "").replace(")", "").replace("[", "").replace("]", "").replace("{", "").replace("}", "")
    sentence = sentence.replace("  ", " ")

    words = sentence.split(" ")
    return words