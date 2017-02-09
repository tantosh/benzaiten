# benzaiten

[![Build Status](https://travis-ci.org/tantosh/benzaiten.svg?branch=master)](https://travis-ci.org/tantosh/benzaiten)

A library for automatic text summarization.

## Installation

1. Clone project
2. Run 'python -m setup.py install'

You should now be able to use the 'bsum' command.

_Note_: If you're running on Windows, check if the installation directory of script is added to your path.

## TextRank

### Algorithm

1. Extract all sentences from the text
2. Build a weighted graph with random scores
	* every sentence is a vertex (node)
	* draw edges between two nodes if there's a *similarity*


Similarity is a function of content overlap and can be defined as:

![equation](http://www.sciweavers.org/tex2img.php?eq=Similarity%28S_%7Bi%7D%2C%20S_%7Bj%7D%29%20%3D%20%5Cfrac%7B%7C%20%7B%20w_%7Bk%7D%7C%20w_%7Bk%7D%20%5Cin%20S_%7Bi%7D%20%20%5Cwedge%20%20w_%7Bk%7D%20%5Cin%20S_%7Bj%7D%20%7D%7C%20%7D%7Blog%28%7CS_%7Bi%7D%7C%29%20%2B%20log%28%7CS_%7Bj%7D%7C%29%7D%20&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)

3. Iterate over the graph until convergence is achieved

```
Convergence is achieved when the error (the dufference of scores computed at iterations k and k-1) falls below a certain threshold (such as 0.0001).
```

The score of each vertex is calculated with the formula:
![equation](http://www.sciweavers.org/tex2img.php?eq=Score%28V_%7Bi%7D%29%20%3D%20%281%20-%20d%29%20%2B%20d%20%2A%20%5Csum_%7B%20V_%7Bj%7D%20%20%5Cin%20In%28V_%7Bj%7D%29%20%7D%20%5Cfrac%7Bw_%7Bij%7D%7D%7B%20%5Csum_%7BV_%7Bk%7D%20%20%5Cin%20Out%28V_%7Bj%7D%29%7D%20w_%7Bjk%7D%7D%20%2A%20Score%28V_%7Bj%7D%29&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)

where:
- d - damping factor between 0 and 1
- In(Vi) - the set of all vertices that point to vertor i (predecessors)
- Out(Vi) - the set of all vertices that vertor i points to (successors)

### Resources

* [TextRank: Bringing Order into Texts](https://web.eecs.umich.edu/~mihalcea/papers/mihalcea.emnlp04.pdf)
* [Variations of the Similarity Function](https://arxiv.org/pdf/1602.03606.pdf)
