class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {"}": "{", "]": "[", ")": "("}
        for char in s:
            if char in mapping:
                topelem = stack.pop() if stack else "!"
                if mapping[char] != topelem:
                    return False
            else:
                stack.append(char)
        return not stack
