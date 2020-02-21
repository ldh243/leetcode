class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums: return 0
        ans = 0
        length = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                length += 1
            else:
                ans = max(length, ans)
                length = 1
        return max(ans, length)
                
            