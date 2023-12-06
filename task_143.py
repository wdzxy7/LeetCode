import math

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(self, head):
    t = head
    count = 0
    while t is not None:
        t = t.next
        count += 1
    half = int(math.ceil(count / 2))
    tail = head
    for i in range(half - 1):
        tail = tail.next
    t = tail.next
    tail.next = None
    tail_head = ListNode()
    tail = t
    while tail is not None:
        t = tail.next
        tail.next = tail_head.next
        tail_head.next = tail
        tail = t
    tail = tail_head.next
    res_head = ListNode()
    move = res_head
    while head is not None and tail is not None:
        head_next = head.next
        tail_next = tail.next
        move.next = head
        move = move.next
        move.next = tail
        move = move.next
        head = head_next
        tail = tail_next
    if head is not None:
        move.next = head
    return res_head.next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
print(reorderList(None, head))