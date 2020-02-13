# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trim(self, node, L, R):
        if not node:
            return None
        elif node.val > R:
            return self.trim(node.left, L, R)
        elif node.val < L:
            return self.trim(node.right, L, R)
        else:
            node.left = self.trim(node.left, L, R)
            node.right=  self.trim(node.right, L, R)
            return node
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        return self.trim(root, L, R)
                