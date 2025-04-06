def dijkstra_simple(graph, start):
    unvisited = list(graph.keys())  # All nodes are initially unvisited
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  # Distance to start node is 0

    while unvisited:
        # Find the unvisited node with the smallest known distance
        current = min(unvisited, key=lambda node: distances[node])

        for neighbor, weight in graph[current]:
            new_distance = distances[current] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance

        unvisited.remove(current)

    return distances
