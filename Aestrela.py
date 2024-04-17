import sys
from Classes import *

def getHeuristica():
    heuristica = {}
    j = open("Heuristica.txt")
    for i in j.readlines():
        node_heuristica_valor = i.split()
        heuristica[node_heuristica_valor[0]] = int (node_heuristica_valor[1])
    return heuristica

def aEstrela(graph, start_node, heuristica):
    unvisited_nodes = list(graph.get_nodes())
    shortest_path = {}
    previous_nodes = {}
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    shortest_path[start_node] = heuristica[]
    while unvisited_nodes:
        current_min_node = None
        for node in unvisited_nodes:
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                previous_nodes[neighbor] = current_min_node
        unvisited_nodes.remove(current_min_node)
    
    return previous_nodes, shortest_path

def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node
    
    while node != start_node:
        path.append(node)
        node = previous_nodes[node]
 
    path.append(start_node)
    
    print("Melhor Caminho {}.".format(shortest_path[target_node]))
    print(" -> ".join(reversed(path)))

nodes = ["Neant", "Iasi", "Vaslui", "Urziceni", "Hirsova", "Eforie", "Bucareste", "Giurgiu", "Pitesti", "Craiova", "Drobeta", "Mehadia", "Lugov", "Timisoara", "Arad", "Zerind", "Oradea", "Sibiu", "Rimnicu_Vilcea", "Fagaras"]
 
init_graph = {}
for node in nodes:
    init_graph[node] = {}

init_graph["Neant"]["Iasi"] = 87
init_graph["Iasi"]["Vaslui"] = 92
init_graph["Vaslui"]["Urziceni"] = 142
init_graph["Urziceni"]["Hirsova"] = 98
init_graph["Urziceni"]["Bucareste"] = 85
init_graph["Hirsova"]["Eforie"] = 86
init_graph["Bucareste"]["Giurgiu"] = 90
init_graph["Bucareste"]["Pitesti"] = 101
init_graph["Bucareste"]["Fagaras"] = 211
init_graph["Pitesti"]["Craiova"] = 138
init_graph["Pitesti"]["Rimnicu_Vilcea"] = 97
init_graph["Craiova"]["Drobeta"] = 120
init_graph["Craiova"]["Rimnicu_Vilcea"] = 146
init_graph["Drobeta"]["Mehadia"] = 75
init_graph["Mehadia"]["Lugov"] = 70
init_graph["Lugov"]["Timisoara"] = 111
init_graph["Timisoara"]["Arad"] = 118
init_graph["Arad"]["Zerind"] = 75
init_graph["Arad"]["Sibiu"] = 140
init_graph["Zerind"]["Oradea"] = 71
init_graph["Oradea"]["Sibiu"] = 151
init_graph["Sibiu"]["Rimnicu_Vilcea"] = 80
init_graph["Sibiu"]["Fagaras"] = 99

heu_graph = {}
for node in nodes:
    heu_graph[node] = {}
heu_graph["Arad"] = 366
heu_graph["Bucareste"] = 0
heu_graph["Craiova"] = 160
heu_graph["Dobreta"] = 242
heu_graph["Eforie"] = 161
heu_graph["Fagaras"] = 178
heu_graph["Giurgiu"] = 77
heu_graph["Hirsova"] = 151
heu_graph["Iasi"] = 226
heu_graph["Lugoj"] = 244
heu_graph["Mehadia"] = 241
heu_graph["Neamt"] = 234
heu_graph["Oradea"] = 380
heu_graph["Pitesti"] = 98
heu_graph["Rimnicu Vilcea"] = 193
heu_graph["Sibiu"] = 253
heu_graph["Timisoara"] = 329
heu_graph["Urziceni"] = 80
heu_graph["Vaslui"] = 199
heu_graph["Zerind"] = 374

graph = Graph(nodes, init_graph, heu_graph)
previous_nodes, shortest_path = aEstrela(graph=graph, start_node="Neant", heuristica= "Neant")
print_result(previous_nodes, shortest_path, start_node="Neant", target_node="Bucareste")