import random
import string
from collections import deque
import heapq

# --- Data Structure: Node ---
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# --- Tree Construction ---
def build_randomized_alphabet_tree():
    """Builds a complete binary tree of 26 nodes with shuffled alphabets."""
    alphabets = list(string.ascii_uppercase)
    random.shuffle(alphabets)
    
    # Create 26 nodes
    nodes = [Node(val) for val in alphabets]
    
    # Link nodes to form a complete binary tree
    for i in range(26):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        
        if left_index < 26:
            nodes[i].left = nodes[left_index]
        if right_index < 26:
            nodes[i].right = nodes[right_index]
            
    return nodes[0], alphabets

# --- a) Breadth First Search (BFS) ---
def bfs(root, goal='G'):
    if not root: return []
    queue = deque([root])
    visited = []
    
    while queue:
        node = queue.popleft()
        visited.append(node.val)
        
        if node.val == goal:
            break
            
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
        
    return visited

# --- b) Depth First Search (DFS) ---
def dfs(root, goal='G'):
    if not root: return []
    stack = [root]
    visited = []
    
    while stack:
        node = stack.pop()
        visited.append(node.val)
        
        if node.val == goal:
            break
            
        # Push right then left so left is evaluated first
        if node.right: stack.append(node.right)
        if node.left: stack.append(node.left)
        
    return visited

# --- c) Depth Limited Search (DLS) ---
def dls(node, goal, limit, visited):
    if not node:
        return False
        
    visited.append(node.val)
    if node.val == goal:
        return True
        
    if limit <= 0:
        return False
        
    # Traverse left
    if dls(node.left, goal, limit - 1, visited):
        return True
    # Traverse right
    if dls(node.right, goal, limit - 1, visited):
        return True
        
    return False

# --- d) Iterative Deepening Search (IDS) ---
def ids(root, goal='G', max_depth=10):
    for limit in range(max_depth):
        visited = []
        if dls(root, goal, limit, visited):
            return visited, limit
    return [], -1

# --- e) Uniform Cost Search (UCS) ---
def ucs(root, goal='G'):
    if not root: return []
    # Priority Queue tuple: (cost, tie_breaker_id, node)
    # Since cost between nodes is equal (1), UCS behaves similarly to BFS.
    pq = [(0, 0, root)]
    visited = []
    tie_breaker = 1
    
    while pq:
        cost, _, node = heapq.heappop(pq)
        visited.append(node.val)
        
        if node.val == goal:
            break
            
        if node.left:
            heapq.heappush(pq, (cost + 1, tie_breaker, node.left))
            tie_breaker += 1
        if node.right:
            heapq.heappush(pq, (cost + 1, tie_breaker, node.right))
            tie_breaker += 1
            
    return visited

# --- Driver Code ---
if __name__ == "__main__":
    # Generate tree
    root, level_order = build_randomized_alphabet_tree()
    print("Level-Order configuration of the generated tree:")
    print(level_order)
    print("-" * 50)
    
    goal_node = 'G'
    print(f"Goal Node to find: {goal_node}\n")
    
    # Execute BFS
    bfs_path = bfs(root, goal_node)
    print(f"a) BFS Visited Nodes ({len(bfs_path)} steps):\n{bfs_path}\n")
    
    # Execute DFS
    dfs_path = dfs(root, goal_node)
    print(f"b) DFS Visited Nodes ({len(dfs_path)} steps):\n{dfs_path}\n")
    
    # Execute DLS
    # Running with an arbitrary limit, e.g., depth of 4
    dls_visited = []
    dls_limit = 4
    found = dls(root, goal_node, dls_limit, dls_visited)
    print(f"c) DLS (Limit={dls_limit}) Visited Nodes:\n{dls_visited} | Found: {found}\n")
    
    # Execute IDS
    ids_path, depth_found = ids(root, goal_node)
    print(f"d) IDS Visited Nodes (Found at depth {depth_found}):\n{ids_path}\n")
    
    # Execute UCS
    ucs_path = ucs(root, goal_node)
    print(f"e) UCS Visited Nodes ({len(ucs_path)} steps):\n{ucs_path}\n")