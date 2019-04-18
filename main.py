from createGraphExample import graphThree
from graph_dot import *
from prim import *

grafo = graphThree()

p = Prim(grafo)

p.start()

print(grafo.edges)
print(p.graph.edges)

convert_graph_dot(p.graph)
