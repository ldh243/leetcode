# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def buildBST(l, r):
            if l > r: return
            mid = (l+r)//2
            newNode = TreeNode(nums[mid])
            newNode.left = buildBST(l, mid-1)
            newNode.right = buildBST(mid+1, r)
            return newNode 
        return buildBST(0, len(nums)-1)
