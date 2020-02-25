# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        queue, dic, maxAns = [root], {}, 0
        while queue:
            node = queue.pop(0)
            if not node: continue
            dic[node.val] = dic.get(node.val, 0) + 1
            maxAns = max(maxAns, dic[node.val])
            queue.append(node.left)
            queue.append(node.right)
        return [k for k,v in dic.items() if v == maxAns]