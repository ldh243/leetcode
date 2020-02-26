# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def dfs(node):
            if not node: return 'x'
            return f'r{node.val} {dfs(node.left)} {dfs(node.right)}'
        return dfs(t) in dfs(s)