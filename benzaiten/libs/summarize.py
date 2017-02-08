from math import log10

def get_similarity(sentence1, sentence2):
    sentence1 = sentence1.replace(".", "")
    words_s1 = sentence1.split(" ")
    sentence2 = sentence2.replace(".", "")
    words_s2 = sentence2.split(" ")

    common_words = set(set(words_s1) & set(words_s2))
    log_words1 = log10(len(words_s1))
    log_words2 = log10(len(words_s2))
    
    similarity = len(list(common_words)) / (log_words1 + log_words2)
    return similarity


if __name__ == "__main__":
    n = get_similarity("Maria go to the shop.", "Georgi go to the gym.")
    print(n)
