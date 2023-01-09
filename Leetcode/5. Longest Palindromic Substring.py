#https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        long = ""
        for center in range(len(s)):
            for offset in [0, 1]:
                start, end = center, center + offset
                while True:
                    if start < 0 or end > len(s) - 1 or s[start] != s[end]:
                        break

                    else:
                        item = s[start:end + 1]
                        long = item if len(item) > len(long) else long
                        start -= 1
                        end += 1
        return long


result = Solution()
print(result.longestPalindrome('babad'))
