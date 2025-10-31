#Implement any one of the Uninformed search techniques

def breadth_first_search(graph, start, goal):
    from collections import deque

    # Create a queue for BFS
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        # Dequeue a vertex and path
        (vertex, path) = queue.popleft()
        
        if vertex in visited:
            continue
        
        visited.add(vertex)

        # Check if we have reached the goal
        if vertex == goal:
            return path

        # Enqueue all adjacent vertices
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return None  # Return None if there is no path from start to goal



if __name__ == "__main__":
    # Define a sample graph as an adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],    
        'D': ['B'],
        'E': ['B'],
        'F': ['C']
    }

    # Perform BFS to find a path from A to F
    path = breadth_first_search(graph, 'A', 'F')
    if path:
        print("Path found:", " -> ".join(path))
    else:
        print("No path found")