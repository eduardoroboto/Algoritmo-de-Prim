from grafo import *


class import_data():
    def __init__(self, file_path, file_name):
        with open("{}/{}".format(file_path, file_name), "r", encoding="ISO-8859-1") as file:
            lista_linhas = file.readlines()

        list_of_lists = list(map(lambda list: list.strip().split(","), lista_linhas))
        edges_index = list_of_lists.index(["edges"])
        nodes_list = list_of_lists[1:edges_index]
        edges_list = list_of_lists[edges_index + 1:]

        self.nodes = list(map(lambda node: node[:3], nodes_list))
        self.edges = list(map(lambda edge: edge[:3], edges_list))

    def create_graph(self):
        list_nodes = self.nodes
        list_edges = self.edges
        grafo = Graph()
        for nod in list_nodes:
            new_node = Node(nod[0], nod[1], nod[2])
            grafo.nodes[nod[0]] = (new_node)

        for edg in list_edges:
            new_edge = Edge(edg[0], edg[2], edg[1])

            grafo.nodes[edg[0]].append_edge(new_edge)
            grafo.nodes[edg[2]].append_edge(new_edge)
            grafo.edges.append(new_edge)

        return grafo

    # declaração de funcões
    def print_files(self, file_list):
        for i, c in enumerate(file_list):
            print("| {} : {} |".format(i, c), end="  ")
