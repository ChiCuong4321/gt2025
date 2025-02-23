import numpy as np

class Graph:
    def __init__(self, num_vertices):
        self.V = num_vertices
        self.adj_matrix = np.zeros((num_vertices, num_vertices), dtype=int)  

    def add_edge(self, u, v):
        self.adj_matrix[u, v] = 1  

    def dfs(self, node, visited, stack=None):
        visited[node] = True
        for neighbor in range(self.V):
            if self.adj_matrix[node, neighbor] == 1 and not visited[neighbor]:
                self.dfs(neighbor, visited, stack)
        if stack is not None:
            stack.append(node)

    def transpose(self):
        return self.adj_matrix.T  

    def find_scc(self):
        visited = np.zeros(self.V, dtype=bool)
        stack = []
        for i in range(self.V):
            if not visited[i]:
                self.dfs(i, visited, stack)
        transposed_matrix = self.transpose()
        visited.fill(False)
        scc_count = 0
        while stack:
            node = stack.pop()
            if not visited[node]:
                self.dfs_using_matrix(node, visited, transposed_matrix)
                scc_count += 1
        return scc_count

    def dfs_using_matrix(self, node, visited, matrix):
        visited[node] = True
        for neighbor in range(self.V):
            if matrix[node, neighbor] == 1 and not visited[neighbor]:
                self.dfs_using_matrix(neighbor, visited, matrix)

    def find_wcc(self):
        visited = np.zeros(self.V, dtype=bool)
        wcc_count = 0
        undirected_matrix = self.adj_matrix + self.adj_matrix.T 
        for node in range(self.V):
            if not visited[node]:
                self.dfs_using_matrix(node, visited, undirected_matrix)
                wcc_count += 1
        return wcc_count

V = 16 
g = Graph(V)

edges = [
    (2, 7), (2, 13), (2, 14),
    (3, 2), (3, 8),
    (4, 7), (4, 12),
    (5, 8), (5, 9),
    (6, 10), (6, 11),
    (7, 4), (7, 6),
    (8, 5), (8, 9),
    (9, 8), (9, 10),
    (10, 6), (10, 11),
    (11, 5),
    (12, 13),
    (13, 12), (13, 14),
    (14, 3), (14, 15),
    (15, 8)
]

for u, v in edges:
    g.add_edge(u, v)
num_scc = g.find_scc()
num_wcc = g.find_wcc()

print(f"Number of Strongly Connected Components (SCC): {num_scc}")
print(f"Number of Weakly Connected Components (WCC): {num_wcc}")