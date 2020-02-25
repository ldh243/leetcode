# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if p.val <= node.val <= q.val:
                return node
            elif node.val < p.val:
                return dfs(node.right)
            elif node.val > q.val:
                return dfs(node.left)
        if p.val > q.val:
            temp = p
            p = q
            q = temp
        return dfs(root)