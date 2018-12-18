class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def has_loop(head):
    if head is None or head.next is None:
        return False

    slow = quick = head
    while head and head.next:
        slow = slow.next
        quick = quick.next.next
        if slow == quick:
            print(slow.val)
            return True
    print('没有环')
    return False

if __name__ == '__main__':
    LList = ListNode(1)
    p1 = ListNode(2)
    p2 = ListNode(3)
    p3 = ListNode(4)
    p4 = ListNode(5)
    p5 = ListNode(6)
    LList.next = p1
    p1.next = p2
    p2.next = p3
    p3.next = p4
    p4.next = p5
    p5.next = p2
    print(has_loop(LList))