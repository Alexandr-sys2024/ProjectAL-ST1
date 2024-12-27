import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        # Добавление ребра в граф
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def print_graph(self):
        # Вывод смежностей для каждой вершины
        for node in self.graph:
            print(node, "->", " -> ".join(map(str, self.graph[node])))

    def draw_graph(self):
        # Визуализация графа с использованием NetworkX
        G = nx.DiGraph()  # Направленный граф
        for node in self.graph:
            for neighbor in self.graph[node]:
                G.add_edge(node, neighbor)

        # Отображение графа
        nx.draw(G, with_labels=True, node_size=2000, node_color="skyblue", font_size=12)
        plt.show()


# Пример использования:
g = Graph()

# Добавление рёбер
g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(3, 4)

# Печать графа
g.print_graph()

# Визуализация графа
g.draw_graph()