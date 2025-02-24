def path_exists(graph, start, end, visited=None):
    if visited is None:
        visited = set()
    if start == end:
        return True
    visited.add(start)
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            if path_exists(graph, neighbor, end, visited):
                return True
    return False

def main():
    graph = {
        1: [2],
        2: [1, 5],
        5: [2],
        3: [4, 6],
        4: [3, 6, 7],
        6: [3, 4, 7],
        7: [4, 6]
    }
    start = int(input("Enter the start node: "))
    end = int(input("Enter the end node: "))
    if path_exists(graph, start, end):
        print(f"Path exists between {start} and {end}.")
    else:
        print(f"No path exists between {start} and {end}.")


