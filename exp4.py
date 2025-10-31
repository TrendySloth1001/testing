#4. Implement any one of the Informed search techniques

import heapq
def a_star_search(graph, start, goal, heuristic):
    # Priority queue for A* search
    open_set = []
    heapq.heappush(open_set, (0 + heuristic[start], 0, start, [start]))
    closed_set = set()

    while open_set:
        # Get the node with the lowest f(n) = g(n) + h(n)
        (f, g, current, path) = heapq.heappop(open_set)

        if current in closed_set:
            continue
        
        closed_set.add(current)

        # Check if we have reached the goal
        if current == goal:
            return path

        # Explore neighbors
        for neighbor, cost in graph[current].items():
            if neighbor not in closed_set:
                g_new = g + cost
                f_new = g_new + heuristic[neighbor]
                heapq.heappush(open_set, (f_new, g_new, neighbor, path + [neighbor]))

    return None  # Return None if there is no path from start to goal


if __name__ == "__main__":
    # Define a sample graph as an adjacency list with costs
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'D': 2, 'E': 5},
        'C': {'A': 4, 'F': 1},    
        'D': {'B': 2},
        'E': {'B': 5},
        'F': {'C': 1}
    }

    # Define a heuristic for each node (straight-line distance to goal)
    heuristic = {
        'A': 7,
        'B': 6,
        'C': 2,
        'D': 1,
        'E': 3,
        'F': 0
    }

    # Perform A* search to find a path from A to F
    path = a_star_search(graph, 'A', 'F', heuristic)
    if path:
        print("Path found:", " -> ".join(path))
    else:
        print("No path found")  