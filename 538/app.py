# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    sum = 0
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.sum = 0
        def dfs(node):
            if not node: return 0
            dfs(node.right)
            self.sum += node.val
            node.val = self.sum
            dfs(node.left)
        dfs(root)
        return root