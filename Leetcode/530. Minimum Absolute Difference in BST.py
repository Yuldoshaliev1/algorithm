#https://leetcode.com/problems/minimum-absolute-difference-in-bst/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        l = []
        def dfs(root):
            if root.left: dfs(root.left)
            l.append(root.val)
            if root.right: dfs(root.right)
        dfs(root)
        return min(b - a for a, b in zip(l, l[1:]))