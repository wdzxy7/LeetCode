import queue


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def reverseOddLevels(self, root):
    high = 0
    node_queue = queue.Queue()
    value_stack = []
    search_queue = queue.Queue()
    search_queue.put(root)
    while not search_queue.empty():
        t_queue = queue.Queue()
        if high % 2 == 0:
            while not search_queue.empty():
                node = search_queue.get()
                if node.left is not None:
                    t_queue.put(node.left)
                    t_queue.put(node.right)
        else:
            while not search_queue.empty():
                node = search_queue.get()
                node_queue.put(node)
                value_stack.append(node.val)
                if node.left is not None:
                    t_queue.put(node.left)
                    t_queue.put(node.right)
            while not node_queue.empty():
                node = node_queue.get()
                node.val = value_stack.pop()
        search_queue = t_queue
        high += 1
    return root

root = TreeNode(2)
root.left = TreeNode(3)
root.right = TreeNode(5)
root.left.left = TreeNode(8)
root.left.right = TreeNode(13)
root.right.left = TreeNode(21)
root.right.right = TreeNode(34)
print(reverseOddLevels(None, root))