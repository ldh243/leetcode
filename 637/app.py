# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        queue, arr, count = [], [], []
        queue.append([root, 0])
        while queue:
            cur, lev = queue.pop(0)
            if not cur:
                continue
            if len(arr) <= lev:
                arr.append(0)
                count.append(0)
            arr[lev] += cur.val
            count[lev] += 1
            queue.append([cur.left, lev + 1])
            queue.append([cur.right, lev + 1])
        for i in range(len(arr)):
            arr[i] /= count[i]
        return arr