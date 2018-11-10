class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x%10 == 0 and x != 0):
            return False

        tmpnum = 0
        while x > tmpnum:
            tmpnum = tmpnum*10 + x%10
            x = x // 10

        return x == tmpnum or x == tmpnum // 10