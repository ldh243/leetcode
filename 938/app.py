# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def dfs(node):
            if not node: return 0
            elif L <= node.val <= R:
                return dfs(node.left) + node.val + dfs(node.right)
            elif node.val < L:
                return dfs(node.right)
            elif node.val > R:
                return dfs(node.left)
            else: return 0
        return dfs(root)