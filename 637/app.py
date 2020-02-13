# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        stack, arr = [], []
        stack.append(root)
        print(root)
        while stack:
            avg = 0
            length = len(stack)
            print(stack)
            for i in range(length):
                if stack[0].val != None:
                    avg += stack[0].val
                if stack[0].left != None:
                    stack.append(stack[0].left)
                if stack[0].right != None:
                    stack.append(stack[0].right)
                stack.pop(0)
            avg /= length
            arr.append(avg)
        return arr