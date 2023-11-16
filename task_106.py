class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(self, inorder, postorder):
    def build(inorder_left, inorder_right, postorder_left, postorder_right):
        if inorder_left > inorder_right:
            return None
        root_node = postorder[postorder_right]
        root = TreeNode(root_node)
        root_in_index = inorder_index[root_node]
        left_tree_size = root_in_index - inorder_left
        right_tree_size = inorder_right - root_in_index
        root.right = build(root_in_index + 1, inorder_right, postorder_right - right_tree_size, postorder_right - 1)
        root.left = build(inorder_left, root_in_index - 1, postorder_left, postorder_left + left_tree_size - 1)
        return root
    n = len(inorder)
    inorder_index = {element: i for i, element in enumerate(inorder)}
    t = build(0, n - 1, 0, n - 1)
    return t

print(buildTree(None, [9,3,15,20,7], [9,15,7,20,3]))