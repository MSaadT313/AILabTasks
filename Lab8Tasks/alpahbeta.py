import math
class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = []

def alpha_beta(node, depth, alpha, beta, maximizing_player=True):
    if depth == 0 or not node.children:
        return node.value

    if maximizing_player:
        value = -math.inf
        for child in node.children:
            value = max(value, alpha_beta(child, depth-1, alpha, beta, False))
            alpha = max(alpha, value)
            if beta <= alpha:
                print("Pruned node:", node)
                break
        node.minmax_value = value
        return value
    else:
        value = math.inf
        for child in node.children:
            value = min(value, alpha_beta(child, depth-1, alpha, beta, True))
            beta = min(beta, value)
            if beta < alpha:
                print("Pruned node:", child.value)
                break
        node.minmax_value = value
        return value

# Sample tree
root = Node()
root.value = 'A'

n1 = Node('B')
n2 = Node('C')
root.children = [n1, n2]

n3 = Node('D')
n4 = Node('E')
n5 = Node('F')
n6 = Node('G')
n1.children = [n3, n4]
n2.children = [n5, n6]

n7 = Node(2)
n8 = Node(3)
n9 = Node(5)
n10 = Node(9)
n3.children = [n7, n8]
n4.children = [n9, n10]

n11 = Node(0)
n12 = Node(2)
n13 = Node(7)
n14 = Node(5)
n5.children = [n11, n12]
n6.children = [n13, n14]

# Example usage
alpha_beta(root, 3, -math.inf, math.inf)
print("Minimax values:")
print("A:", root.minmax_value)
print("B:", n1.minmax_value)
print("C:", n2.minmax_value)
print("D:", n3.minmax_value)
print("E:", n4.minmax_value)
print("F:", n5.minmax_value)
# print("G:", n6.minmax_value)
