class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def get_height(self, node: Node)->int:
        if not node:
            return 0
        
        return node.height
    
    def is_balance(self, node: Node)->int:
        if not node:
            return 0
        
        left_node_height = self.get_height(node.left)
        right_node_height = self.get_height(node.right)\
        
        return right_node_height - left_node_height
    
    def right_rotate(self, node: Node):
        