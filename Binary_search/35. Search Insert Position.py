# https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchPosition(self, nums: list[int], target: int) -> int:
        if target not in nums:
            nums.append(target)
            nums.sort()
        return nums.index(target)


res = Solution()
print(res.searchPosition([1, 3, 5, 6], 5))
