graph = {
    'A': {'B':2, 'D':1},
    'B': {'E':1, 'C':4},
    'D': {'E':2},
    'E': {'C':3, 'F':2},
    'C': {'F':6},
    'F': {}
}
heuristic = {
    'A':5,
    'B':4,
    'C':2,
    'D':4,
    'E':1,
    'F':0
}
def greedy_Bfs(graph, start, goal):
    frontier = [(start, heuristic[start])]
    visited = set()
    came_from = {start: None}

    while frontier:
        frontier.sort(key=lambda x: x[1])

        current_node, _ = frontier.pop(0)

        if current_node in visited:
            continue

        print(current_node, end=" ")
        visited.add(current_node)

        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = came_from[current_node]
            path.reverse()
            print(f"\nGoal found with GBFS. Path: {path}")
            return

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                came_from[neighbor] = current_node
                frontier.append((neighbor, heuristic[neighbor]))

    print("\nGoal not found")

print("\nFollowing is the Greedy Best-First Search (GBFS):")
greedy_Bfs(graph, 'A', 'F')