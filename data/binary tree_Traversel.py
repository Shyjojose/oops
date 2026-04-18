from typing import Optional

class Node:
    def __init__(self, value):
        self.value = value
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None
root = Node(10)
left_child = Node(5)
right_child = Node(15)
root.left = left_child
root.right = right_child
left_child.left = Node(3)
left_child.right = Node(7)
right_child.right = Node(20)

#pre order traversal print the node before its children

def print_tree(node):        
    if node is None:         # ← indented — INSIDE the function
        return               # ← indented — INSIDE the function
    print(node.value)        # ← indented — INSIDE the function
    print_tree(node.left)    # ← indented — INSIDE the function
    print_tree(node.right)  

print_tree(root)             