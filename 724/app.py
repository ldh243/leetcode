class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        F, sumNum, curSum = [], sum(nums), 0
        for i, val in enumerate(nums):  
            if curSum*2 == sumNum-val:
                return i
            curSum += val
        return -1