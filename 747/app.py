class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        s1 = s2 = float('-inf')
        ans = -1
        for i, val in enumerate(nums):
            if val > s1:
                s2 = s1
                s1 = val
                ans = i
            elif val > s2: s2 = val
        if s1 >= s2*2:
            return ans
        else: return -1