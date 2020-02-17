# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        queue = [root]
        setNum = set()
        while queue:
            cur = queue.pop(0)
            if not cur:
                continue    
            if k-cur.val in setNum:
                return True
            setNum.add(cur.val)
            queue.append(cur.left)
            queue.append(cur.right)
        return False