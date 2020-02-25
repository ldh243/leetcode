# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.ans = True
        def dfs(node):
            if not node: return 0
            x = dfs(node.left)
            y = dfs(node.right)
            if abs(x-y) > 1:
                self.ans = False
            return max(x, y) + 1
        dfs(root)
        return self.ans