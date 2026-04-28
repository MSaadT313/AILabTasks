import heapq

# Graph representation (Adjacency List with weights)
graph = {
    "Arad": [("Zerind", 75), ("Sibiu", 140), ("Timisoara", 118)],
    "Zerind": [("Oradea", 71)],
    "Oradea": [("Sibiu", 151)],
    "Sibiu": [("Fagaras", 99), ("Rimnicu Vilcea", 80)],
    "Timisoara": [("Lugoj", 111)],
    "Lugoj": [("Mehadia", 70)],
    "Mehadia": [("Drobeta", 75)],
    "Drobeta": [("Craiova", 120)],
    "Craiova": [("Rimnicu Vilcea", 146), ("Pitesti", 138)],
    "Rimnicu Vilcea": [("Pitesti", 97)],
    "Fagaras": [("Bucharest", 211)],
    "Pitesti": [("Bucharest", 101)],
    "Bucharest": [("Giurgiu", 90), ("Urziceni", 85)],
    "Urziceni": [("Hirsova", 98), ("Vaslui", 142)],
    "Hirsova": [("Eforie", 86)],
    "Vaslui": [("Iasi", 92)],
    "Iasi": [("Neamt", 87)],
    "Giurgiu": [],
    "Eforie": [],
    "Neamt": []
}

def uniform_cost_search(start, goal):
    # Priority queue: (cost, current_node, path)
    frontier = [(0, start, [start])]
    
    # To store best cost found so far for each node
    visited = {}

    while frontier:
        cost, node, path = heapq.heappop(frontier)

        # Goal test
        if node == goal:
            return path, cost

        # Skip if we already found a cheaper way to this node
        if node in visited and visited[node] <= cost:
            continue

        visited[node] = cost

        # Expand neighbors
        for neighbor, weight in graph.get(node, []):
            new_cost = cost + weight
            heapq.heappush(frontier, (new_cost, neighbor, path + [neighbor]))

    return None, float("inf")


# Run search
path, cost = uniform_cost_search("Arad", "Bucharest")

print("Optimal Path:", " -> ".join(path))
print("Total Cost:", cost)