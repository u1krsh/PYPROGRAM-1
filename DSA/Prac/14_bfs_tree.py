from collections import deque

def bfs_graph(graph,start):
    queue = deque([start])
    visited = set()

    while queue:
        node = queue.popleft()

        if node not in visited:
            print(node,end=" ")
            visited.add(node)
            queue.extend(neighbour for neighbour in graph[node] if neighbour not in visited)
    