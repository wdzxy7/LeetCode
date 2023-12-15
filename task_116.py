import queue

class Node:
    def __init__(self, val: int = 0, left = None, right = None, next = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def connect(self, root):
    if root is None:
        return None
    search_queue = queue.Queue()
    search_queue.put(root)
    while not search_queue.empty():
        copy_queue = queue.Queue()
        s_node = search_queue.get()
        if s_node.left is not None:
            copy_queue.put(s_node.left)
        if s_node.right is not None:
            copy_queue.put(s_node.right)
        while not search_queue.empty():
            next_node = search_queue.get()
            s_node.next = next_node
            if next_node.left is not None:
                copy_queue.put(next_node.left)
            if next_node.right is not None:
                copy_queue.put(next_node.right)
            s_node = next_node
        s_node.next = None
        search_queue = copy_queue
    return root

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print(connect(None, root))
