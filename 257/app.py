# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        queue = [(root, '')]
        ans = []
        while queue:
            node, path = queue.pop(0)
            curPath = path + '->' + str(node.val)
            if not node.left and not node.right:
                ans.append(curPath[2:])
                continue
            if node.left: queue.append((node.left, curPath))
            if node.right: queue.append((node.right, curPath))
        return ans