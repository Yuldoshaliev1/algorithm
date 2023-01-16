# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        s1 = min(strs)
        s2 = max(strs)

        for a, b in enumerate(s1):
            if b != s2[a]:
                return s1[:a]
        return s1


res = Solution()
print(res.longestPrefix(["flower","flow","flight"]))
