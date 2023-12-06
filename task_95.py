class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def generateTrees(self, n):
    def build(start, end):
        if start <= end:
            trees = []
            for i in range(start, end + 1):
                left = build(start, i - 1)
                right = build(i + 1, end)
                for l in left:
                    for r in right:
                        node = TreeNode(i)
                        node.left = l
                        node.right = r
                        trees.append(node)
            return trees
        else:
            return [None]
    return build(1, n) if n else []

print(generateTrees(None, 3))