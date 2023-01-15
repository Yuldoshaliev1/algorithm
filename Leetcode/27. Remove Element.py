# https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        s = nums.count(val)

        for i in range(s):
            nums.remove(val)

        return len(nums)


res = Solution()
print(res.removeElement([3, 2, 2, 3], 3))
