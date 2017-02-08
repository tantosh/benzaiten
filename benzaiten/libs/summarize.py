from math import log10

def get_sentences(text):
    sentences = text.split(".")
    return sentences

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

if __name__ == "__main__":
    sentences = get_sentences("Where is Maria? She go to the shop.")

    words = get_words("Maria ? go to :the shop.")
    print(words)

    n = get_similarity("Maria go to the shop.", "Georgi go to the gym.")
    print(n)
