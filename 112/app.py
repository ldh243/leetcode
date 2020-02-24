# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        def dfs(node, subSum):
            if not node:
                return False
            subSum += node.val
            if not node.left and not node.right:
                if subSum == sum: return True
                return False
            return dfs(node.left, subSum) or dfs(node.right, subSum)
        return dfs(root, 0)