class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def sumNumbers(self, root):
    res = 0
    def search(node, t_sum):
        nonlocal res
        if node is None:
            return
        elif node.left is None and node.right is None:
            temp = t_sum + str(node.val)
            res += int(temp)
            return
        else:
            temp = t_sum + str(node.val)
            search(node.left, temp)
            search(node.right, temp)
    search(root, '')
    return res


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(sumNumbers(None, root))