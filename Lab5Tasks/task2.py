graph = {
    'A': [('D',1), ('B',2)],
    'D': [('B',2), ('E',2)],
    'B': [('E',1), ('C',4)],
    'E': [('C',3), ('F',2)],
    'C': [('F',6)],
    'F': []
}
def h(node):
    heuristics = {
        'A':5,
        'B':4,
        'C':2,
        'D':4,
        'E':1,
        'F':0
    }
    return heuristics[node]
from queue import PriorityQueue

def best_first_search(graph, start, goal, h):
    visited = set()
    pq = PriorityQueue()
    pq.put((h(start), start))

    while not pq.empty():
        cost, node = pq.get()

        if node not in visited:
            print(node, end=' ')
            visited.add(node)

            if node == goal:
                print("\nGoal reached!")
                return True

            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    pq.put((h(neighbor), neighbor))

    print("\nGoal not reachable!")
    return False

print("Best-First Search Path:")
best_first_search(graph, 'A', 'F', h)