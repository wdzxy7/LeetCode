class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def isValidBST(self, root):
    def judge(node, small, big):
        if node is None:
            return True
        if not small < node.val < big:
            return False
        if not judge(node.left, small, node.val):
            return False
        if not judge(node.right, node.val, big):
            return False
        return True
    return judge(root, float('-inf'), float('inf'))

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(6)
print(isValidBST(None, root))