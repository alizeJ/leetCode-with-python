class LNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def sort_lnode(head):
    if head is None or head.next is None:
        return head
    mid = get_mid(head)
    left = head
    right = mid.next
    mid.next = None
    return merge(sort_lnode(left), sort_lnode(right))



def get_mid(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def merge(left, right):
    head = tmp = LNode(0)
    while left and right:
        if left.val < right.val:
            tmp.next = left
            left = left.next
        else:
            tmp.next = right
            right = right.next
        tmp = tmp.next
    if left:
        tmp.next = left
    elif right:
        tmp.next = right
    return head.next

