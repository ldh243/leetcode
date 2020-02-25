class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        subSum, ans = 0, 0
        for i in range(k):
            ans += nums[i]
        subSum = ans
        for i in range(k, len(nums)):
            subSum += (nums[i] - nums[i-k])
            ans = max(ans, subSum)
        return ans/k
