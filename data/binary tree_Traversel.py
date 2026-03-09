class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
root = Node(10)
root.left =Node(5)
root.right = Node(15)
root.left.left=Node(3)
root.left.right=Node(7)
root.right.right=Node(20)

#pre order traversal print the node before its children

def print_tree(node):        
    if node is None:         # ← indented — INSIDE the function
        return               # ← indented — INSIDE the function
    print(node.value)        # ← indented — INSIDE the function
    print_tree(node.left)    # ← indented — INSIDE the function
    print_tree(node.right)  

print_tree(root)             