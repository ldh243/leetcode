# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def bfs():
            ans = 0
            queue = [(root, False)]
            while queue:
                node, isLeft = queue.pop(0)
                if not node:
                    continue
                if node.left is None and node.right is None and isLeft:
                    ans += node.val
                queue.append((node.left, True))
                queue.append((node.right, False))
            return ans
        ans = bfs()
        return ans