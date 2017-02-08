from benzaiten.graph import GraphBuilder

class TextRankSummarizer:
    
    def __init__(self, k_sentences=10):
        self._k_sentences = k_sentences

    def summarize(self, text):
        builder = GraphBuilder()
        #build graph
        text_graph = builder.buildGraph(text)
        #iterate until convergence

        #join most important sentences
        return ' '.join(text_graph.k_highest(self._k_sentences))
    