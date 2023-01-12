# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            res = int(str(x)[:: -1])
        else:
            res = int(str(x * -1)[::-1]) * -1

        ak = 2 ** 31 * (-1)
        akm = 2 ** 31 - 1

        if res > akm or res < ak:
            return 0
        return res


ans = Solution()
print(ans.reverse(120))
