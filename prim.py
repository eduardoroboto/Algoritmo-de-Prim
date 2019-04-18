import sys

from grafo import Graph


class Prim:
    def __init__(self, graph):
        self.graph = graph
        self.init_values(graph, "key", sys.maxsize)
        self.init_values(graph, "parent", None)
        self.lista = dict()

    def start(self):
        prim_graph = Graph("n")
        nodes_visited = list()
        nodes_to_visit = self.graph.nodes
        prim_graph.addNodes(nodes_to_visit)
        print(nodes_to_visit)
        nodes_to_visit["A"].data["key"] = 0
        while nodes_to_visit:
            min = self.return_min_value(nodes_to_visit)
            nodes_to_visit.pop(min.name)
            print(nodes_to_visit)
            if min.data["parent"] is not None:
                # self.lista[min.name] = min.data["parent"]

                prim_graph.addEdge(min.name, min.data["parent"].name, min.data["key"])

            nodes_adj = self.return_all_vertices(min)

            for node in nodes_adj:
                if node[1].weight < node[0].data["key"]:
                    node[0].data["parent"] = min
                    node[0].data["key"] = node[1].weight

            # break

        self.graph = prim_graph

    def return_min_value(self, nodes):
        node = list(nodes.values())
        return min(node, key=lambda x: x.data["key"])

    def init_values(self, graph, type, value):
        for key in graph.nodes:
            graph.nodes[key].add_data_key(type, value)

    def return_all_vertices(self, node):
        nodes_list = list()
        for edge in node.edges:
            nodes_list.append([edge.destiny, edge])

        return nodes_list
