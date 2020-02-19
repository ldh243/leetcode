class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        ans = [0 for i in nums]
        medal = ['Gold Medal', 'Silver Medal', 'Bronze Medal']
        count = -1
        dic = {}
        for i, val in enumerate(nums):
            dic[val] = i
        for i in sorted(dic.keys(), reverse=True):
            count += 1
            ans[dic[i]] = medal[count] if count < 3 else str(count + 1)
        return ans
