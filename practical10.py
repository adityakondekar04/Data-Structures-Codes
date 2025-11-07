def count(arr):
    return len(arr)

def dfs(matrix, start, visited, nodes):
    print(nodes[start], end=" ")
    visited[start] = True
    for i in range(len(matrix[start])):
        if matrix[start][i] == 1 and not visited[i]:
            dfs(matrix, i, visited, nodes)

def bfs(adj_list, start):
    visited = set()
    queue = [start]
    visited.add(start)
    while queue:
        node = queue.pop(0)
        print(node, end=" ")
        for neighbor in adj_list[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

def main():
    nodes = ["A", "B", "C", "D"]
    adj_matrix = [
        [0, 1, 1, 0],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [0, 1, 1, 0]
    ]
    adj_list = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A", "D"],
        "D": ["B", "C"]
    }
    print("DFS Traversal (Adjacency Matrix, start A):")
    visited = [False] * len(nodes)
    dfs(adj_matrix, 0, visited, nodes)

    print("\n\nBFS Traversal (Adjacency List, start A):")
    bfs(adj_list, "A")

main()
