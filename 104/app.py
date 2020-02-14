# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def dfs(root, depth):
            if not root:
                return 0
            return max(dfs(root.left, depth + 1),  dfs(root.right, depth + 1)) + 1
        print(dfs(root, 1))
        return dfs(root, 1)