import heapq

# Graph representation (Adjacency List with Costs)
graph = {
    'A': [('B', 3), ('C', 6), ('D', 5)],
    'B': [('E', 9), ('F', 8)],
    'C': [('G', 12), ('H', 14)],
    'D': [('I', 7)],
    'I': [('J', 5), ('K', 6)],
    'J': [('L', 1), ('M', 10), ('N', 2)],
    'E': [], 'F': [], 'G': [], 'H': [],
    'K': [], 'L': [], 'M': [], 'N': []
}

def beam_search(start, goal, beam_width=3):
    """
    Beam Search Algorithm to find lowest cost path.
    
    Args:
        start (str): Starting node (A)
        goal (str): Goal node
        beam_width (int): Number of best paths to keep
    
    Returns:
        path, cost
    """

    # Initialize beam with start node
    beam = [(0, [start])]

    while beam:
        candidates = []

        # Expand all paths in current beam
        for cost, path in beam:
            current = path[-1]

            # Goal check
            if current == goal:
                return path, cost

            # Explore neighbors
            for neighbor, weight in graph.get(current, []):
                new_cost = cost + weight
                new_path = path + [neighbor]
                candidates.append((new_cost, new_path))

        # Select top-k lowest cost paths
        beam = heapq.nsmallest(beam_width, candidates, key=lambda x: x[0])

    return None, float('inf')


# ---- Execution ----
start_node = 'A'
goal_node = 'L'   # You can change goal if needed
beam_width = 3

path, cost = beam_search(start_node, goal_node, beam_width)

# Output
if path:
    print("Path found:", " → ".join(path))
    print("Total Cost:", cost)
else:
    print("No path found.")