class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        maxCount = 0
        for i in nums:
            if not i in dic:
                dic[i] = 1
            else: dic[i] += 1
            if maxCount < dic[i]:
                maxCount = dic[i]
                ans = i
        return ans
