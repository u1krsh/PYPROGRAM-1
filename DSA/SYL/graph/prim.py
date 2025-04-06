INF = 9999999

# Number of nodes
V = 5

# Graph represented as an adjacency matrix
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

selected = [False] * V
selected[0] = True  # Start from the first node

print("Edge \tWeight")

edge_count = 0
total_weight = 0

while edge_count < V - 1:
    minimum = INF
    x = 0
    y = 0

    for i in range(V):
        if selected[i]:
            for j in range(V):
                if not selected[j] and graph[i][j]:
                    if minimum > graph[i][j]:
                        minimum = graph[i][j]
                        x = i
                        y = j

    print(f"{x} - {y} \t{graph[x][y]}")
    total_weight += graph[x][y]
    selected[y] = True
    edge_count += 1

print("Total weight of MST:", total_weight)
