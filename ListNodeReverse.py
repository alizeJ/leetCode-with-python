class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def ReverseListNode(head):
    if head is None or head.next is None:
        return head

    # cur = head  # 循环变量
    # tmp = None  # 保存数据的临时变量
    # newhead = None  # 新的翻转单链表的表头
    # while cur:
    #     tmp = cur.next
    #     cur.next = newhead
    #     newhead = cur  # 更新 新链表的表头
    #     cur = tmp
    # return newhead

    next = None
    prev = None
    while head:
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev


def create_ll(arr):
    pre = ListNode(0)
    tmp = pre
    for i in arr:
        tmp.next = ListNode(i)
        tmp = tmp.next
    return pre.next


def print_ll(head):
    tmp = head
    while tmp:
        print(tmp.val, end='')
        tmp = tmp.next



a = create_ll(range(5))
print_ll(a)  # 0 1 2 3 4
b = ReverseListNode(a)
print_ll(b)  # 4 3 2 1 0


