import networkx as nx
import matplotlib.pyplot as plt

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

# Візуалізація графа
plt.figure(figsize=(10, 7))
pos = nx.spring_layout(G)  # Розташування вузлів
nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=1500, edge_color="gray", font_size=15)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Транспортна мережа міста з вагами")
plt.show()

# алгоритм Дейкстри для знаходження найкоротшого шляху
def dijkstra_all_pairs_shortest_paths(graph):
    return dict(nx.all_pairs_dijkstra_path(graph))

# найкоротші шляхи між усіма вершинами
shortest_paths = dijkstra_all_pairs_shortest_paths(G)

# аналіз основних характеристик
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree_dict = dict(G.degree())
average_degree = sum(degree_dict.values()) / num_nodes

print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print(f"Ступінь вершин: {degree_dict}")
print(f"Середній ступінь вершин: {average_degree:.2f}")

# вивід найкоротших шляхів між усіма вершинами
for start_node in shortest_paths:
    for end_node in shortest_paths[start_node]:
        path = shortest_paths[start_node][end_node]
        print(f"Найкоротший шлях від {start_node} до {end_node}: {path}")
