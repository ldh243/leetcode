# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    pre, ans = float('inf'), float('inf')
    def getMinimumDifference(self, root: TreeNode) -> int:
        def dfs(node):
            if node:
                dfs(node.left)
                self.ans, self.pre = min(self.ans, abs(self.pre-node.val)), node.val
                dfs(node.right)
        dfs(root)
        return self.ans