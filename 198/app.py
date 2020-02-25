class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        F = [nums[0]]
        F.append(max(F[0], nums[1]))
        for i in range(2, len(nums)):
            F.append(max(F[i-1], F[i-2] + nums[i]))
        return F[-1]