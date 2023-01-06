#https://leetcode.com/problems/make-the-string-great/
from collections import deque

s = "s"

stack = deque()

for i in s:
    if stack and abs(ord(stack[ - 1]) - ord(i)) == 32:
        stack.pop()

    else:
        stack.append(i)
print(''.join(stack))