class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


def addTwoNumbers(self, l1, l2):
    l = l1
    sum1 = 0
    d = 1
    while l is not None:
        sum1 = sum1 + l.val * d
        d = d * 10
        l = l.next
    l = l2
    sum2 = 0
    d = 1
    while l is not None:
        sum2 = sum2 + l.val * d
        d = d * 10
        l = l.next
    res = sum1 + sum2
    front_l = ListNode(0, None)
    t = front_l
    while res >= 10:
        k = res % 10
        front_l.val = k
        new_l = ListNode(-1, None)
        front_l.next = new_l
        res = res // 10
        front_l = new_l
    front_l.val = res
    front_l = t
    l = front_l
    while l is not None:
        print(l.val)
        l = l.next
    return front_l


l1 = ListNode(2, None)
l2 = ListNode(4, None)
l3 = ListNode(9, None)
l4 = ListNode(5, None)
l5 = ListNode(6, None)
l6 = ListNode(4, None)
l7 = ListNode(9, None)
l1.next = l2
l2.next = l3
l4.next = l5
l5.next = l6
l6.next = l7
print(addTwoNumbers(None, l1, l4))