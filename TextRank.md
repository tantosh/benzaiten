## Basic algorithm

1. Extract all the sentences from the text
2. Build a weighted graph
	- in the graph every sentence is a node
	- you put links from each sentence to all others or to the k-most similar sentences WEIGHTED by similarity
	- you have to define a similarity score between two sentences
3. Run PageRank on weighted graph
	- get "n" most important sentences for summary (sorted by number of links to each node)

> TextRank is basically PageRank for sentences. 
> Sentences are extracted from the text and then a graph is built linking sentences that are similar. 
> If we imagine a Random walk over this graph of sentences then the most 
> important ones will be the ones that are most visited. That is PageRank. 
> So if you apply PageRank to the graph and then list the "n" most important 
> sentences in the order in which they appeared in the text then you have a summary.
> The key principle is that the sentence that is most similar to all others 
> is probably the one that captures the ideas of the text better. 
> [quora resource](https://www.quora.com/Natural-Language-Processing-What-are-algorithms-for-auto-summarize-text)

###### [Variations of the Similarity Function](https://arxiv.org/pdf/1602.03606.pdf)
