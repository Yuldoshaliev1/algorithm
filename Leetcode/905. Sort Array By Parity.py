#https://leetcode.com/problems/sort-array-by-parity/

nums = [3, 1, 2, 4]
a = []
for i in nums:
    if i % 2 == 0:
        a.insert(0, i)
    else:
        a.append(i)
print(a)

#two pointers solution
#
# nums = [3, 1, 2, 4]
# res = len(nums) - 1
# index = 0
# while res > index:
#     num = nums[index]
#     if num % 2 == 0:
#         index += 1
#         continue
#     nums[res], nums[index] = nums[index], nums[res]
#     res -= 1
# print(nums)