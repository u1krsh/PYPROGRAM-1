def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node)  # Process the node
            visited.add(node)
            # Add neighbors in reverse to mimic recursive DFS order
            stack.extend(reversed(graph[node]))

# Run iterative DFS
dfs_iterative(graph, 'A')
