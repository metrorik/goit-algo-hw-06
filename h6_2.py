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



# алгоритм DFS
def dfs_path(graph, start, goal, path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == goal:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            new_path = dfs_path(graph, node, goal, path)
            if new_path:
                return new_path
    return None

# BFS
def bfs_path(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                return path + [next]
            else:
                queue.append((next, path + [next]))
    return None

# формат зручний для роботи з алгоритмами
graph_dict = nx.to_dict_of_lists(G)

# Знаходження шляхів
start_node = "A"
goal_node = "G"

dfs_result = dfs_path(graph_dict, start_node, goal_node)
bfs_result = bfs_path(graph_dict, start_node, goal_node)

# Аналіз основних характеристик
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree_dict = dict(G.degree())
average_degree = sum(degree_dict.values()) / num_nodes

print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print(f"Ступінь вершин: {degree_dict}")
print(f"Середній ступінь вершин: {average_degree:.2f}")

print(f"Шлях від {start_node} до {goal_node} за допомогою DFS: {dfs_result}")
print(f"Шлях від {start_node} до {goal_node} за допомогою BFS: {bfs_result}")
