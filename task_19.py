class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


def removeNthFromEnd(self, head, n):
    t = ListNode(0, head)
    res_head = head
    k = 0
    front_pt = head
    while front_pt and k < n - 1:
        front_pt = front_pt.next
        k += 1
    move_pt = t
    delete_pt = head
    while front_pt.next:
        move_pt = move_pt.next
        delete_pt = delete_pt.next
        front_pt = front_pt.next
    if res_head == delete_pt:
        if delete_pt.next is None:
            return None
        else:
            return delete_pt.next
    move_pt.next = delete_pt.next
    return res_head


l1 = ListNode(1, None)
l2 = ListNode(2, None)
l3 = ListNode(3, None)
l4 = ListNode(4, None)
l5 = ListNode(5, None)
l6 = ListNode(6, None)
l7 = ListNode(7, None)

l1.next = l2
'''
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6
l6.next = l7
'''
h = removeNthFromEnd(None, l1, 2)
while h is not None:
    print(h.val)
    h = h.next