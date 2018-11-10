class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2

        if l2 is None:
            return l1

        tmp = ListNode(0)
        dev = tmp
        flag = 0
        while l1 or l2:
            tmpnum = 0
            if l1:
                tmpnum = l1.val
                l1 = l1.next
            if l2:
                tmpnum += l2.val
                l2 = l2.next

            tmpend = (tmpnum + flag) % 10
            flag = (tmpnum + flag) // 10
            dev.next = ListNode(tmpend)
            dev = dev.next
            if flag:
                dev.next = ListNode(1)

        dev = tmp.next
        del  tmp
        return dev