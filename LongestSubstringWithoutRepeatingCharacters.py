class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlength = 0
        for i, _ in enumerate(s):
            uniStr = ''
            count = 0
            for j in s[i:]:
                if j not in uniStr:
                    uniStr += j
                    count += 1
                    if maxlength < count:
                        maxlength = count
                else:
                    break
        return maxlength


def lengthOfLongestSubstring(s):
    start = maxLength = 0
    uniStr = {}
    for index, char in enumerate(s):
        if char in uniStr and start <= uniStr[char]:
            start = uniStr[char] + 1
        else:
            maxLength = max(maxLength, index - start + 1)
        uniStr[char] = index
    return maxLength
