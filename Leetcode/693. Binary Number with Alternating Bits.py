n = 4
k = -1
while n:
    if n & 1 == k:
        print(False)
        break
    k = n & 1
    n >>= 1
print(True)