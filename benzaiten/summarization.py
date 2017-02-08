from bentaizen.graph import GraphBuilder

def summarize(text):
    builder = GraphBuilder()
    #build graph
    text_graph = builder.buildGraph(text)
    #iterate until convergence
    