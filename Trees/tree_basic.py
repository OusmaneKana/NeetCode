class TreeNode():
    def __init__(self, val=0, right = None, left = None):
        self.val = val 
        self.right = right
        self.left = left
    
    def addNode(self, node):
        # For BST
        if node.val > self.val:
            if self.right is None:
                self.right = node
            else:
                self.right.addNode(node)
        else:
            if self.left is None:
                self.left = node
            else: 
                self.left.addNode(node)
