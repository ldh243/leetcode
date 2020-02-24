class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            if nums[ans] < i:
                ans += 1
                nums[ans] = i
        return ans+1