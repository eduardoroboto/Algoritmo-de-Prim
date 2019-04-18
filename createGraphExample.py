from grafo import Graph


def graphOne():
    grafo = Graph("d")

    grafo.addNode("A")
    grafo.addNode("B")
    grafo.addNode("C")
    grafo.addNode("D")
    grafo.addNode("E")
    grafo.addNode("F")

    grafo.addEdge("A", "B", 1)
    grafo.addEdge("A", "C", 8)
    grafo.addEdge("B", "D", 2)
    grafo.addEdge("C", "B", 3)
    grafo.addEdge("C", "E", 1)
    grafo.addEdge("D", "F", 1)
    grafo.addEdge("D", "C", 1)
    grafo.addEdge("D", "E", 3)
    grafo.addEdge("E", "D", 2)
    grafo.addEdge("E", "F", 9)

    # teste com valores negativos
    # grafo.addEdge("C", "A",-1)
    # grafo.addEdge("B", "C",-1)

    # Ciclo infinito bug na hora de rotanar a lista de Pai
    # grafo.addEdge("C", "E", -1)
    # grafo.addEdge("E", "D", -2)

    return grafo


def graphTwo():
    grafo = Graph("d")
    grafo.addNode("S")
    grafo.addNode("A")
    grafo.addNode("B")
    grafo.addNode("C")
    grafo.addNode("D")
    grafo.addNode("E")

    grafo.addEdge("S", "A", 10)
    grafo.addEdge("S", "E", 8)
    grafo.addEdge("A", "C", 2)
    grafo.addEdge("E", "D", 1)
    grafo.addEdge("D", "A", -4)
    grafo.addEdge("D", "C", -1)
    grafo.addEdge("C", "B", -2)
    grafo.addEdge("B", "A", 1)

    return grafo


def graphThree():
    grafo = Graph("n")
    grafo.addNodes(["A", "B", "C", "D", "E", "F", "G"])

    grafo.addEdge("A", "B", 2)
    grafo.addEdge("A", "D", 3)
    grafo.addEdge("A", "C", 3)
    grafo.addEdge("B", "C", 4)
    grafo.addEdge("B", "E", 3)
    grafo.addEdge("C", "D", 5)
    grafo.addEdge("C", "F", 6)
    grafo.addEdge("C", "E", 1)
    grafo.addEdge("D", "F", 7)
    grafo.addEdge("E", "F", 8)
    grafo.addEdge("F", "G", 9)

    return grafo
