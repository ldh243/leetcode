# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    ans = 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def maxLength(node):
            if node is None: return 0
            maxLeft = maxLength(node.left)
            maxRight = maxLength(node.right)
            self.ans = max(self.ans, maxLeft + maxRight )               
            return max(maxLeft, maxRight) + 1
        maxLength(root)
        return self.ans