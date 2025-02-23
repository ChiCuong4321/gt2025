import numpy as np

graph = np.array([
    [0, 9, 4, 0, 0, 5, 0, 0, 0],
    [9, 0, 7, 0, 0, 4, 0, 8, 0],
    [4, 7, 0, 3, 0, 1, 0, 0, 0],
    [0, 0, 3, 0, 5, 6, 2, 0, 0],
    [0, 0, 0, 5, 0, 0, 0, 0, 8],
    [5, 4, 1, 6, 0, 0, 7, 8, 0],
    [0, 0, 0, 2, 0, 7, 0, 0, 4],
    [0, 8, 0, 0, 0, 8, 0, 0, 3],
    [0, 0, 0, 0, 8, 0, 4, 3, 0]
])

def prim_numpy(graph):
    n = graph.shape[0]
    selected_nodes = np.zeros(n, dtype=bool)  
    selected_nodes[0] = True  
    mst_edges = []
    
    for _ in range(n - 1):
        min_weight = np.inf
        min_edge = (-1, -1)

        for u in range(n):
            if selected_nodes[u]:
                for v in range(n):
                    if not selected_nodes[v] and 0 < graph[u, v] < min_weight:
                        min_weight = graph[u, v]
                        min_edge = (u, v)

        mst_edges.append(min_edge)
        selected_nodes[min_edge[1]] = True

    return mst_edges

prim_result = prim_numpy(graph)
print("Prim's MST Edges:", [(u+1, v+1) for u, v in prim_result]) 

def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x != root_y:
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

def kruskal_numpy(graph):
    edges = []
    n = graph.shape[0]
    
    for i in range(n):
        for j in range(i+1, n):
            if graph[i, j] > 0:
                edges.append((graph[i, j], i, j))

    edges.sort()  
    parent = np.arange(n)
    rank = np.zeros(n, dtype=int)
    mst_edges = []

    for weight, u, v in edges:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            mst_edges.append((u, v))

    return mst_edges

kruskal_result = kruskal_numpy(graph)
print("Kruskal's MST Edges:", [(u+1, v+1) for u, v in kruskal_result])  

def dijkstra_numpy(graph, source, target):
    n = graph.shape[0]
    visited = np.zeros(n, dtype=bool)
    distances = np.full(n, np.inf)
    distances[source] = 0
    predecessors = np.full(n, -1)

    while not visited[target]:
        min_dist = np.inf
        current = -1
        for i in range(n):
            if not visited[i] and distances[i] < min_dist:
                min_dist = distances[i]
                current = i
        
        if current == -1:
            break  

        visited[current] = True

        for neighbor in range(n):
            if graph[current, neighbor] > 0 and not visited[neighbor]:
                new_dist = distances[current] + graph[current, neighbor]
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    predecessors[neighbor] = current


    path = []
    node = target
    while node != -1:
        path.append(node)
        node = predecessors[node]
    path.reverse()
    return path, distances[target]

source, target = 0, 8  
dijkstra_path, total_distance = dijkstra_numpy(graph, source, target)

print("Dijkstra's Shortest Path:", [p+1 for p in dijkstra_path]) 
print("Total Distance:", total_distance)
