class Solution:
    def findLHS(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            dic[i] = dic.get(i, 0) + 1
        ans = 0
        for key,val in dic.items():
            if key-1 in dic:
                ans = max(ans, dic[key] + dic[key-1])
        return ans