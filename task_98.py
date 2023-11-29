class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def isValidBST(self, root):
    def judge(node):
        if node is None:
            return True
        if (node.left < node.val or node.left is None) and (node.right > node.val or node.right is None):
            judge(node.left)
            judge(node.right)
        else:
            return False
    return judge(root)