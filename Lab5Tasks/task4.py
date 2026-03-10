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
def a_star_search(graph, start, goal, heuristic):
    visited = set()
    g_costs = {start: 0}
    came_from = {start: None}
    frontier = [(heuristic.get(start, 0), start)]

    while frontier:
        frontier.sort(key=lambda x: x[0])
        current_f, current_node = frontier.pop(0)

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
            print(f"\nGoal found with A*. Path: {path}")
            return path

        for neighbor, cost in graph.get(current_node, {}).items():
            new_g_cost = g_costs[current_node] + cost
            f_cost = new_g_cost + heuristic.get(neighbor, 0)

            if neighbor not in g_costs or new_g_cost < g_costs[neighbor]:
                g_costs[neighbor] = new_g_cost
                came_from[neighbor] = current_node
                frontier.append((f_cost, neighbor))

    print("\nGoal not found")
    return None
print("Following is the A* Search:")
a_star_search(graph, 'A', 'F', heuristic)
