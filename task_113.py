class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def pathSum(self, root, targetSum):
    res = []

    def search(node, t_sum, path):
        if node is None:
            return
        t_sum += node.val
        t_path = path.copy()
        if t_sum == targetSum and node.left is None and node.right is None:
            t_path.append(node.val)
            res.append(t_path)
            return
        t_path.append(node.val)
        search(node.left, t_sum, t_path)
        search(node.right, t_sum, t_path)

    search(root, 0, [])
    return res

root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(1)
print(pathSum(None, root, 1))