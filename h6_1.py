import networkx as nx
import matplotlib.pyplot as plt

# порожній граф
G = nx.Graph()

# вершини (станції транспортної мережі міста)
stations = ["A", "B", "C", "D", "E", "F", "G"]
G.add_nodes_from(stations)

# ребра (маршрути)
edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("C", "E"), ("D", "E"), ("E", "F"), ("E", "G"), ("F", "G")]
G.add_edges_from(edges)

# Візуалізація графа
plt.figure(figsize=(10, 7))
pos = nx.spring_layout(G)  # Розташування вузлів
nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=1500, edge_color="gray", font_size=15)
plt.title("Транспортна мережа міста")
plt.show()

# Аналіз основних характеристик
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree_dict = dict(G.degree())
average_degree = sum(degree_dict.values()) / num_nodes

print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print(f"Ступінь вершин: {degree_dict}")
print(f"Середній ступінь вершин: {average_degree:.2f}")
