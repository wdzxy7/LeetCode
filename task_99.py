class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def recoverTree(self, root):
    t_max = None
    keep_node = None
    change_node = None
    def recover(node):
        nonlocal t_max, keep_node, change_node
        if node is None:
            return
        recover(node.left)
        if (t_max is None or t_max < node.val) and change_node is None:
            t_max = node.val
            keep_node = node
        elif t_max < node.val and change_node is not None:
            return
        else:
            change_node = node
        recover(node.right)
    recover(root)
    t = keep_node.val
    keep_node.val = change_node.val
    change_node.val = t
    return root

root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(2)
print(recoverTree(None, root))