import re
import random
from itertools import permutations
from heapq import nlargest
from math import log10

class GraphBuilder:
    
    def __init__(self, precision = 4):
        self._precision = precision

    def buildGraph(self, text):
        '''
        Builds a graph from the given text.
        The verteces of the graph are the sentences in the text.
        The edges connect two verteces if they are similar to each other.
        '''
        sentences = self._extract_sentences(text)
        return TextGraph(self._create_verteces(sentences))
    
    def _create_verteces(self, sentences):
        '''
        Creates the verteces of the graph from the given list of sentences.
        Similarity is computed for every pair of sentences. If the sentences are similar, the verteces are connected with weight equal to the similarity between them.
        '''
        verteces = [GraphNode(sentence, order) for order, sentence in enumerate(sentences)]
        for vertex, other in permutations(verteces, 2):
            similarity = self._similarity(vertex.sentence, other.sentence)
            if similarity:
                vertex.connect(other, similarity)
        return verteces
    
    def _similarity(self, sentence1, sentence2):
        '''
        Computes how similar are two sentences. The number of common words and the length of the sentences is taken into consideration.
        '''
        if sentence1 == '' or sentence2 == '':
            return 0
        words_s1 = self._extract_words(sentence1)
        words_s2 = self._extract_words(sentence2)

        common_words = [w for w in words_s1 if w in words_s2]
        log_words1 = log10(len(words_s1))
        log_words2 = log10(len(words_s2))
    
        return round(len(common_words) / (log_words1 + log_words2), self._precision)
    
    def _extract_sentences(self, text):
        ''' Extract sentences in a text '''
        return re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s', text)
    
    def _extract_words(self, sentence):
        ''' Extract words in a sentence '''
        return re.sub("[^\w]", " ",  sentence).split()

class TextGraph:
    
    def __init__(self, verteces):
        self._verteces = verteces
    
    def __iter__(self):
        return iter(self._verteces)
    
    @property
    def verteces(self):
        return self._verteces
    
    def k_highest(self, k):
        '''Get k most important sentences, ordered by occurrence in text.'''
        n_largest = nlargest(k, self._verteces, lambda v: v.score)
        n_largest.sort(key = lambda sentence: sentence.order)
        return list(map(lambda v: v.sentence, n_largest))
    
    def errors(self):
        return [vertex.error for vertex in self._verteces]
              
class GraphNode:
    
    def __init__(self, value, order, score = random.random(), precision = 4):
        self._value = value
        self._order = order
        self._score = score
        self._error = score
        self._connected = dict()
        self._precision = precision
    
    def __hash__(self):
        return hash(self._value)

    def __eq__(self, other):
        return self._value == other._value

    def __ne__(self, other):
        return not(self == other)
    
    @property
    def sentence(self):
        return self._value
    
    @property
    def order(self):
        return self._order
    
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, new_score):
        self._error = round(abs(self._score - new_score), self._precision)
        self._score = new_score
    
    @property
    def error(self):
        return self._error
    
    @property
    def connected(self):
        return self._connected
    
    def connect(self, node, strength):
        node._add_connection(self, strength)
        self._add_connection(node, strength)
    
    def _add_connection(self, node, strength):
        self._connected[node] = strength
