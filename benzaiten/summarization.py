from benzaiten.graph import GraphBuilder

class TextRankSummarizer:
    
    def __init__(self, k_sentences=10, damping_factor=0.85, max_iterations=10000, convergence_threshold=0.0001):
        self._k_sentences = k_sentences
        self._damping_factor = damping_factor
        self._max_iterations = max_iterations
        self._convergence_threshold = convergence_threshold

    def summarize(self, text):
        #build the text graph
        builder = GraphBuilder()
        text_graph = builder.buildGraph(text)
        
        #iterate until convergence
        self._text_rank(text_graph)
        
        #join most important sentences
        return ' '.join(text_graph.k_highest(self._k_sentences))
    
    def _text_rank(self, text_graph):
        iteration = 0
        while iteration < self._max_iterations and any([error for error in text_graph.errors() if error > self._convergence_threshold]):
            for vertex in text_graph.verteces:
                vertex.score = self._calculate_score(vertex)
            iteration += 1

    def _calculate_score(self, vertex):
        connected_weight = self._calculate_connected_weight(vertex.connected)
        return (1 - self._damping_factor) + self._damping_factor * (connected_weight)

    def _calculate_connected_weight(self, connected):
        connected_weight = 0
        for node, weight in connected.items():
            weight_sum = weight / sum(list(node.connected.values()))
            connected_weight += weight_sum * node.score
        return connected_weight