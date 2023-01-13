# https://leetcode.com/problems/palindrome-number/

class Solution:
    def numPalindrom(self, x: int) -> bool:
        s = str(x)
        reverse = s[:: - 1]
        if (s == reverse):
            return True
        else:
            return False


res = Solution()
print(res.numPalindrom(121))
