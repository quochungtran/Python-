import heapq

def shortest_path(edges, num_nodes, start_node):
    # Build adjacency list
    adjacency_list = {i: [] for i in range(1, num_nodes + 1)}
    for src, dest, weight in edges:
        adjacency_list[src].append((dest, weight))
    
    # Min-heap to get the node with the smallest tentative distance
    min_heap = [(0, start_node)]  # (current_distance, node)
    shortest_distances = {}

    while min_heap:
        current_distance, current_node = heapq.heappop(min_heap)

        if current_node in shortest_distances:
            continue

        shortest_distances[current_node] = current_distance

        for neighbor, edge_weight in adjacency_list[current_node]:
            if neighbor not in shortest_distances:
                heapq.heappush(min_heap, (current_distance + edge_weight, neighbor))

    return shortest_distances

# Time complexity : O(ElogE), worst cases: O(V^2)