# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return [0, 0]
            leftAns, leftSum = dfs(node.left)
            rightAns, rightSum = dfs(node.right)
            curSum = leftSum + rightSum + node.val
            curAns = abs(leftSum - rightSum) + leftAns  + rightAns
            return curAns, curSum
        return dfs(root)[0]
         