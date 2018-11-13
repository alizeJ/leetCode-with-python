# 罗马数字转数字
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        if s is None:
            return res
        d = {"M": 1000, "D":500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        for i in range(len(s)-1, -1, -1):
            if i !=len(s) - 1:
                if d[s[i]] < d[s[i+1]]:
                    res -= d[s[i]]
                else:
                    res += d[s[i]]
            else:
                res += d[s[i]]

        return res
