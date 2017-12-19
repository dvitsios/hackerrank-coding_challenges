""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def is_bst(node, key_min=None, key_max=None):
    if node == None:
        return 1
    
    if key_max is not None and node.data >= key_max:
        return 0
    if key_min is not None and node.data <= key_min:
        return 0
    
    return is_bst(node.left, key_min, node.data) and is_bst(node.right, node.data, key_max)

def checkBST(root):
    return is_bst(root)