# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        def dfs(t):
            if not t:
                return ''
            elif not t.left and not t.right:
                return str(t.val)
            elif t.left and not t.right:
                return str(t.val) + '(' + dfs(t.left) + ')'
            elif not t.left and t.right:
                return str(t.val) + '()(' + dfs(t.right) + ')'
            else:
                return str(t.val) + '(' + dfs(t.left) + ')' + '(' + dfs(t.right) + ')'
        return dfs(t)