# https://leetcode.com/problems/intersection-of-two-arrays/

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res = []
        n = len(nums1)
        for i in nums1:
            if i in nums2:
                res.append(i)
        return list(set(res))


result = Solution()
print(result.intersection([1, 2, 2, 1], [2, 2]))
