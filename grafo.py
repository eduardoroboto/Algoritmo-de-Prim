class Node:
    def __init__(self, name, type=None, weight=None):
        self.name = name
        self.edges = list()
        self.data = dict()

        if (type is not None):
            self.type = type

        if (weight is not None):
            self.weight = weight

    def add_data_key(self, key, value):
        self.data[key] = value

    def append_edge(self, edge):
        self.edges.append(edge)

    def grau(self):
        return len(self.edges)

    def __str__(self):
        return "{}".format(self.name)

    def __repr__(self):
        return str(self)


class Edge:
    def __init__(self, origin, destiny, weight=None):
        self.origin = origin
        self.destiny = destiny
        if weight is not None:
            self.weight = weight

    def __str__(self):
        return "{}->{} p{}".format(self.origin, self.destiny, self.weight)

    def __repr__(self):
        return str(self)


class Graph:
    def __init__(self, type=None):
        self.nodes = dict()
        self.edges = list()
        if (type is not None):
            self.type = type

    def addNode(self, name, type=None, weight=None):
        new_node = Node(name, type, weight)
        self.nodes[name] = new_node

    def addNodes(self, list_of_nodes):
        for name in list_of_nodes:
            self.addNode(name)

    def addEdge(self, origin, destiny, weight):

        new_edge = Edge(self.nodes[origin], self.nodes[destiny], weight)
        other_edge = Edge(self.nodes[destiny], self.nodes[origin], weight)

        self.edges.append(new_edge)
        self.nodes[origin].append_edge(new_edge)
        self.nodes[destiny].append_edge(other_edge)

    def ordem(self):
        return len(self.nodes)

    def tamanho(self):
        return len(self.edges)

    def densidade(self):
        return len(self.edges) / (len(self.nodes) * (len(self.nodes) - 1) / 2)

    def list_grau(self):
        return list(map(lambda x: x.grau(), list(self.nodes.values())))
