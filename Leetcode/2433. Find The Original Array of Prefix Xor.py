#https://leetcode.com/problems/find-the-original-array-of-prefix-xor/
pref = [5,2,0,3,1]
for i in range(len(pref)-1, 0, -1):
    pref[i]^=pref[i - 1]
print(pref)