import sys
 
class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)
        
    def construct_graph(self, nodes, init_graph):
        graph = {}
        for node in nodes:
            graph[node] = {}
        
        graph.update(init_graph)
        
        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value
                    
        return graph
    
    def get_nodes(self):
        return self.nodes
    
    def get_outgoing_edges(self, node):
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections
    
    def value(self, node1, node2):
        return self.graph[node1][node2]
    
def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())
 
    # We'll use this dict to save the cost of visiting each node and update it as we move along the graph   
    shortest_path = {}
 
    # We'll use this dict to save the shortest known path to a node found so far
    previous_nodes = {}
 
    # We'll use max_value to initialize the "infinity" value of the unvisited nodes   
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    # However, we initialize the starting node's value with 0   
    shortest_path[start_node] = 0
    
    # The algorithm executes until we visit all nodes
    while unvisited_nodes:
        # The code block below finds the node with the lowest score
        current_min_node = None
        for node in unvisited_nodes: # Iterate over the nodes
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
                
        # The code block below retrieves the current node's neighbors and updates their distances
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                # We also update the best path to the current node
                previous_nodes[neighbor] = current_min_node
 
        # After visiting its neighbors, we mark the node as "visited"
        unvisited_nodes.remove(current_min_node)
    
    return previous_nodes, shortest_path

def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node
    
    while node != start_node:
        path.append(node)
        node = previous_nodes[node]
 
    # Add the start node manually
    path.append(start_node)
    
    print("We found the following best path with a value of {}.".format(shortest_path[target_node]))
    print(" -> ".join(reversed(path)))

nodes = ["Neant", "Iasi", "Vaslui", "Urziceni", "Hirsova", "Eforie", "Bucareste", "Giurgiu", "Pitesti", "Craiova", "Drobeta", "Mehadia", "Lugov", "Timisoara", "Arad", "Zerind", "Oradea", "Sibiu", "Rimnicu Vilcea", "Fagaras"]
 
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
init_graph["Pitesti"]["Rimnicu Vilcea"] = 97
init_graph["Craiova"]["Drobeta"] = 120
init_graph["Craiova"]["Rimnicu Vilcea"] = 146
init_graph["Drobeta"]["Mehadia"] = 75
init_graph["Mehadia"]["Lugov"] = 70
init_graph["Lugov"]["Timisoara"] = 111
init_graph["Timisoara"]["Arad"] = 118
init_graph["Arad"]["Zerind"] = 75
init_graph["Arad"]["Sibiu"] = 140
init_graph["Zerind"]["Oradea"] = 71
init_graph["Oradea"]["Sibiu"] = 151
init_graph["Sibiu"]["Rimnicu Vilcea"] = 80
init_graph["Sibiu"]["Fagaras"] = 99

graph = Graph(nodes, init_graph)
previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node="Neant")
print_result(previous_nodes, shortest_path, start_node="Neant", target_node="Rimnicu Vilcea")

