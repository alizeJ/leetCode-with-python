class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        min_str = min(strs)
        max_str = max(strs)
        for i, j in enumerate(min_str):
            if j != max_str[i]
                return min_str[:i]
        return min_str