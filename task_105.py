class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(self, preorder, inorder) -> TreeNode:
    def myBuildTree(preorder_left: int, preorder_right: int, inorder_left: int, inorder_right: int):
        if preorder_left > preorder_right:
            return None
        preorder_root = preorder_left
        inorder_root = index[preorder[preorder_root]]
        root = TreeNode(preorder[preorder_root])
        size_left_subtree = inorder_root - inorder_left
        root.left = myBuildTree(preorder_left + 1, preorder_left + size_left_subtree, inorder_left,
                                inorder_root - 1)
        root.right = myBuildTree(preorder_left + size_left_subtree + 1, preorder_right, inorder_root + 1,
                                 inorder_right)
        return root

    n = len(preorder)
    index = {element: i for i, element in enumerate(inorder)}
    return myBuildTree(0, n - 1, 0, n - 1)


print(buildTree(None, [3,9,20,15,7], [9,3,15,20,7]))