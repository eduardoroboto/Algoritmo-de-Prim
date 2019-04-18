def sep(graph):
    if "d" in graph.type:
        return "->", "digraph"
    elif "n" in graph.type:
        return "--", "graph"


def convert_graph_dot(graph):
    type_of = sep(graph)
    space = type_of[0]
    type = type_of[1]
    with open('code.dot', 'w') as file:
        file.write("{} graphname ".format(type))
        file.write("{\n")
        file.write("rankdir=LR;\n")
        for edge in graph.edges:
            file.write("{} {} {} [label={}]\n".format(edge.origin.name, space,
                                                      edge.destiny.name, edge.weight))

        file.write("}")


def make_path(graph, path):
    list_path = list()
    type_of = sep(graph)
    space = type_of[0]
    type = type_of[1]
    for index, val in enumerate(path):
        # print(path[index].dado["nome"])
        string = ""
        try:
            string = "{} {} {}".format(val.dado["nome"], space, path[index + 1].dado["nome"])
            list_path.append(string)
        except:
            pass

    # print(list_path)
    with open('code.dot', 'w') as file:

        file.write("{} graphname ".format(type))
        file.write("{\n")
        file.write("rankdir=LR;\n")
        for edge in graph.edges:
            line = "{} {} {}".format(edge.origin.name, space,
                                     edge.destiny.name)

            # print(line in list_path)
            if line in list_path:
                line = "{} [label={}] [color=blue];\n".format(line, edge.weight)
            else:
                line = "{} [label={}];\n".format(line, edge.weight)

            file.write(line)

        file.write("}")
