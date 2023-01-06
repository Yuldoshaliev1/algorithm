class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        lh = self.maxDepth(root.left)
        rh = self.maxDepth(root.right)
        return 1+max(lh,rh)