# Adjacency matrix for graph G
# Nodes are labeled from 1 to 6
# Assuming the graph is a tree 

# Step 1: Construct the adjacency matrix
# Define the number of nodes
num_nodes = 6
adj_matrix = [[0] * num_nodes for _ in range(num_nodes)]
edges = [
    (1, 2),
    (1, 3),
    (2, 4),
    (2, 5),
    (3, 6)
]
for u, v in edges:
    adj_matrix[u - 1][v - 1] = 1  
    adj_matrix[v - 1][u - 1] = 1  
print("Adjacency Matrix:")
for row in adj_matrix:
    print(row)
def inorder_traversal(node, visited):
    if node is None or visited[node - 1]:
        return

    # Inorder: Left -> Root -> Right
    # For a general tree, we assume the first child is "left" and the next is "right"
    visited[node - 1] = True

    # Traverse the first child (left)
    for neighbor in range(num_nodes):
        if adj_matrix[node - 1][neighbor] == 1 and not visited[neighbor]:
            inorder_traversal(neighbor + 1, visited)  

    print(node, end=" ")

    # Traverse the remaining children (right)
    for neighbor in range(num_nodes):
        if adj_matrix[node - 1][neighbor] == 1 and not visited[neighbor]:
            inorder_traversal(neighbor + 1, visited)  

# Function print the subtree rooted at node x in Inorder
def print_subtree_inorder(x):
    visited = [False] * num_nodes  # Track visited nodes
    print(f"Inorder traversal of subtree rooted at node {x}:")
    inorder_traversal(x, visited)
    print()  

print_subtree_inorder(1)  
print_subtree_inorder(2)  
print_subtree_inorder(3)  