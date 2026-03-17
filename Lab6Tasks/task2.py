import random
import copy

# Goal State
GOAL_STATE = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]   # 0 represents blank
]

# Heuristic: Number of misplaced tiles
def calculate_heuristic(state):
    misplaced = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != GOAL_STATE[i][j]:
                misplaced += 1
    return misplaced


# Generate neighbors (move blank up, down, left, right)
def get_neighbors(state):
    neighbors = []
    
    # Find blank (0)
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                x, y = i, j

    moves = [(-1,0), (1,0), (0,-1), (0,1)]  # up, down, left, right

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = copy.deepcopy(state)
            # Swap blank
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)

    return neighbors


# Generate random initial state
def generate_initial_state():
    nums = list(range(9))
    random.shuffle(nums)
    return [nums[i:i+3] for i in range(0, 9, 3)]


# Hill Climbing Algorithm
def hill_climbing():
    current_state = generate_initial_state()
    current_h = calculate_heuristic(current_state)

    while True:
        neighbors = get_neighbors(current_state)
        next_state = None
        next_h = current_h

        for neighbor in neighbors:
            h = calculate_heuristic(neighbor)
            if h < next_h:
                next_state = neighbor
                next_h = h

        # Stop if no better neighbor
        if next_state is None:
            break

        current_state = next_state
        current_h = next_h

        # Stop if goal reached
        if current_h == 0:
            break

    return current_state, current_h


# Print function
def print_state(state):
    for row in state:
        print(row)
    print()


# ---- Execution ----
if __name__ == "__main__":
    solution, h = hill_climbing()

    print("Final State:")
    print_state(solution)

    print("Heuristic (misplaced tiles):", h)

    if h == 0:
        print("Goal state reached!")
    else:
        print("Stuck in local optimum.")