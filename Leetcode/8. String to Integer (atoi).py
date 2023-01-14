# https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def resAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0
        sign = -1 if s[0] == '-' else 1
        ret = 0
        i = 1 if s[0] in ['-', '+'] else 0

        while i < len(s) and s[i].isdigit():
            ret = ret * 10 + int(s[i])
            i += 1
        return max(-2 ** 31, min(sign * ret, 2 ** 31 - 1))


res = Solution()
print(res.resAtoi('4193 with hhbd'))
