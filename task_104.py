class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def maxDepth(self, root):
    max_depth = 0
    def search(node, depth):
        nonlocal max_depth
        if node is None:
            return
        depth += 1
        if depth > max_depth:
            max_depth = depth
        search(node.left, depth)
        search(node.right, depth)
    search(root, 0)
    return max_depth
