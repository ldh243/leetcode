# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        queue = [root]
        ans = []
        if not root: return ans
        while queue:
            n = len(queue)
            nodeLev = []
            for i in range(n):
                node = queue.pop(0)
                nodeLev.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            ans = [nodeLev] + ans
        return ans