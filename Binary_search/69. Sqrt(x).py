# https://leetcode.com/problems/sqrtx/
class Solution:
    def resSqrt(self, x: int) -> int:
        if x == 0:
            return 0
        n = 1
        while n ** 2 <= x:
            n += 1
        return n - 1


res = Solution()
print(res.resSqrt(8))
