#https://leetcode.com/problems/squares-of-a-sorted-array/
nums = [-7,-3,2,3,11]
sq2 = list(map(lambda n: n ** 2, nums))
sq2.sort()
print(sq2)