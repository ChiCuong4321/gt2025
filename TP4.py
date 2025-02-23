import numpy as np

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = np.full((vertices, vertices), np.inf)  

    def add_edge(self, u, v, weight):
        self.graph[u-1, v-1] = weight  
        self.graph[v-1, u-1] = weight  

    def prim_mst(self, start):
        visited = np.zeros(self.V, dtype=bool)
        min_edge = np.full(self.V, np.inf)
        parent = np.full(self.V, -1)
        min_edge[start] = 0

        mst_edges = []
        total_weight = 0

        for _ in range(self.V):
            u = np.argmin(min_edge)  
            if min_edge[u] == np.inf:
                break  # If no valid edge, stop

            visited[u] = True
            total_weight += min_edge[u]

            if parent[u] != -1:
                mst_edges.append((parent[u] + 1, u + 1, int(min_edge[u])))

            min_edge[u] = np.inf  

            for v in range(self.V):
                if self.graph[u, v] < min_edge[v] and not visited[v]:
                    min_edge[v] = self.graph[u, v]
                    parent[v] = u

        return mst_edges, total_weight

    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])  
        return parent[i]

    def union(self, parent, rank, x, y):
        root_x, root_y = self.find(parent, x), self.find(parent, y)
        if root_x != root_y:
            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_y] = root_x
                rank[root_x] += 1

    def kruskal_mst(self):
        edges = [(self.graph[u, v], u, v) for u in range(self.V) for v in range(u) if self.graph[u, v] != np.inf]
        edges.sort()

        parent = np.arange(self.V)
        rank = np.zeros(self.V, dtype=int)

        mst_edges = []
        total_weight = 0

        for weight, u, v in edges:
            root_u, root_v = self.find(parent, u), self.find(parent, v)
            if root_u != root_v:
                self.union(parent, rank, root_u, root_v)
                mst_edges.append((u + 1, v + 1, int(weight)))
                total_weight += weight

        return mst_edges, total_weight

g = Graph(9)
edges = [
    (1, 2, 4), (1, 5, 1), (1, 7, 2), (2, 3, 7), (2, 6, 5),
    (3, 4, 1), (3, 6, 8), (4, 6, 6), (4, 7, 4), (4, 8, 3),
    (6, 9, 2), (5, 6, 9), (5, 7, 10), (7, 9, 8), (8, 9, 1)
]

for u, v, w in edges:
    g.add_edge(u, v, w)

start_node = int(input("Enter the starting node (1-9) for Prim's Algorithm: ")) - 1

prim_mst_edges, prim_total_weight = g.prim_mst(start_node)
print("Prim's Algorithm MST:")
for edge in prim_mst_edges:
    print(f"Edge: {edge[0]} - {edge[1]}, Weight: {edge[2]}")
print(f"Total Weight: {prim_total_weight}")

kruskal_mst_edges, kruskal_total_weight = g.kruskal_mst()
print("\nKruskal's Algorithm MST:")
for edge in kruskal_mst_edges:
    print(f"Edge: {edge[0]} - {edge[1]}, Weight: {edge[2]}")
print(f"Total Weight: {kruskal_total_weight}")
