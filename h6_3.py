import networkx as nx

# порожній граф
G = nx.Graph()

# вершини
stations = ["A", "B", "C", "D", "E", "F", "G"]
G.add_nodes_from(stations)

# ребра з вагами
edges = [
    ("A", "B", 4), ("A", "C", 2), 
    ("B", "D", 5), ("C", "D", 8), ("C", "E", 10),
    ("D", "E", 2), ("E", "F", 3), ("E", "G", 6), ("F", "G", 1)
]
G.add_weighted_edges_from(edges)


# Реалізація алгоритму Дейкстри
def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())
    
    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])
        
        if distances[current_vertex] == float('infinity'):
            break
        
        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
        
        unvisited.remove(current_vertex)
    
    return distances


# перетворення формату
graph_dict = {node: {} for node in G.nodes}
for edge in G.edges(data=True):
    u, v, data = edge
    weight = data['weight']
    graph_dict[u][v] = weight
    graph_dict[v][u] = weight


# найкоротші шляхи від усіх вершин
all_shortest_paths = {}
for node in graph_dict:
    distances = dijkstra(graph_dict, node)
    all_shortest_paths[node] = distances


print("\nНайкоротші шляхи між усіма вершинами:")
for start_node in all_shortest_paths:
    for end_node in all_shortest_paths[start_node]:
        path_distance = all_shortest_paths[start_node][end_node]
        print(f"Найкоротший шлях від {start_node} до {end_node} має довжину: {path_distance}")
