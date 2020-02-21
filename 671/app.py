# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    setNum = set()
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        def dfs(node):
            if not node: 
                return float('inf')
            self.setNum.add(node.val)
            dfs(node.left)
            dfs(node.right)
        self.setNum.clear()
        dfs(root)
        return -1 if len(self.setNum) < 2 else sorted(self.setNum)[1]