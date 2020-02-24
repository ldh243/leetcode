class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        sum, ans, minSubArray = 0, nums[0], 0
        for i in nums:
            sum += i
            ans = max(ans, sum - minSubArray)
            minSubArray = min(minSubArray, sum)
        return ans