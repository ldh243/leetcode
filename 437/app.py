# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, K: int) -> int:
        self.ans = 0
        def dfs(node, sumRemain):
            if not node: return
            for i in range(len(sumRemain)):
                sumRemain[i] -= node.val
                if not sumRemain[i]:
                    self.ans += 1
            sumRemain += [K]
            dfs(node.left, sumRemain[0:])
            dfs(node.right, sumRemain[0:])
        dfs(root, [K])
        return self.ans
