# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def check(L, R):
            if not L and not R: return True
            elif L and R and L.val == R.val: 
                return check(L.left, R.right) and check(L.right, R.left)
            return False
        return check(root, root)