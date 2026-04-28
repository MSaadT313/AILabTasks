import heapq

# -----------------------------
# Goal State
# -----------------------------
goal_state = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8)
)

# -----------------------------
# Start State
# -----------------------------
start_state = (
    (7, 2, 4),
    (5, 0, 6),
    (8, 3, 1)
)

# -----------------------------
# Goal positions for heuristic
# -----------------------------
goal_positions = {}
for i in range(3):
    for j in range(3):
        value = goal_state[i][j]
        goal_positions[value] = (i, j)

# -----------------------------
# Heuristic: Manhattan Distance
# -----------------------------
def manhattan(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_i, goal_j = goal_positions[value]
                distance += abs(i - goal_i) + abs(j - goal_j)
    return distance

# -----------------------------
# Find blank position
# -----------------------------
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# -----------------------------
# Generate neighbors
# -----------------------------
def get_neighbors(state):
    i, j = find_blank(state)
    moves = []
    
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    
    for di, dj in directions:
        ni, nj = i + di, j + dj
        
        if 0 <= ni < 3 and 0 <= nj < 3:
            new_state = [list(row) for row in state]
            
            # swap blank
            new_state[i][j], new_state[ni][nj] = new_state[ni][nj], new_state[i][j]
            
            moves.append(tuple(tuple(row) for row in new_state))
    
    return moves

# -----------------------------
# A* Search Algorithm
# -----------------------------
def a_star(start):
    pq = []
    heapq.heappush(pq, (manhattan(start), 0, start, []))
    
    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if state == goal_state:
            return path + [state]

        if state in visited:
            continue
        visited.add(state)

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                new_g = g + 1
                new_f = new_g + manhattan(neighbor)
                heapq.heappush(pq, (new_f, new_g, neighbor, path + [state]))

    return None

# -----------------------------
# Run the solver
# -----------------------------
solution = a_star(start_state)

# -----------------------------
# Print result
# -----------------------------
def print_state(state):
    for row in state:
        print(row)
    print()

if solution:
    print("Solution found!\n")
    for step, state in enumerate(solution):
        print(f"Step {step}:")
        print_state(state)
else:
    print("No solution found.")