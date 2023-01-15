# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToint(self, s: str) -> int:
        table = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": -2,
            "IX": -2,
            "XL": -20,
            "XC": -20,
            "CD": -200,
            "CM": -200,
        }

        result = 0
        for ans, val in table.items():
            result += s.count(ans) * val

        return result


res = Solution()
print(res.romanToint('III'))
