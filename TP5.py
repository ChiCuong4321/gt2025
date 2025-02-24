import numpy as np

def dijkstra_numpy(graph, source, target):
    n = graph.shape[0]  
    visited = np.zeros(n, dtype=bool)  
    distances = np.full(n, np.inf)  
    distances[source] = 0  
    predecessors = np.full(n, -1)  

    while not visited[target]:  
        min_dist = np.min(distances[~visited])  
        current = np.where((distances == min_dist) & (~visited))[0][0]
        
        visited[current] = True  

        neighbors = np.where(graph[current] > 0)[0]  
        for neighbor in neighbors:
            if not visited[neighbor]:
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

graph = np.array([
    [0, 4, 1, 0, 0, 0, 0, 0, 0, 0],  
    [4, 0, 0, 0, 0, 3, 0, 0, 0, 0],  
    [1, 0, 0, 8, 0, 7, 0, 0, 0, 0],  
    [0, 0, 8, 0, 0, 0, 0, 5, 0, 0],  
    [0, 0, 0, 0, 0, 0, 0, 2, 2, 0], 
    [0, 3, 7, 0, 0, 0, 0, 1, 0, 0],  
    [0, 0, 0, 0, 0, 0, 0, 3, 4, 0],  
    [0, 0, 0, 5, 2, 1, 3, 0, 6, 7],  
    [0, 0, 0, 0, 2, 0, 4, 6, 0, 1],  
    [0, 0, 0, 0, 0, 0, 0, 7, 1, 0]   
], dtype=float)

source, target = 0, 9

path, total_weight = dijkstra_numpy(graph, source, target)

path_letters = ' -> '.join(chr(65 + p) for p in path)

print(f"Shortest Path: {path_letters}")
print(f"Total Weight: {total_weight}")
