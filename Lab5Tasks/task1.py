graph = {
    'A': {'B':2, 'D':1},
    'B': {'E':1, 'C':4},
    'D': {'B':2, 'E':2},
    'E': {'C':3, 'F':2},
    'C': {'F':6},
    'F': {}
}
import heapq

def uniform_cost_search(graph, start, goal):
    frontier = [(0, start)]
    visited = set()
    came_from = {start: None}
    cost_so_far = {start: 0}

    while frontier:
        current_cost, current_node = heapq.heappop(frontier)

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
            print(f"\nGoal reached with UCS. Path: {path}")
            print(f"Total Cost: {current_cost}")
            return path

        for neighbor, cost in graph[current_node].items():
            new_cost = cost_so_far[current_node] + cost

            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                came_from[neighbor] = current_node
                heapq.heappush(frontier, (new_cost, neighbor))

    print("\nGoal not reachable")
    return None