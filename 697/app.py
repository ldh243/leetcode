class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        index, count = {}, {}
        for i, val in enumerate(nums):
            if val not in index:
                index[val] = [i]
            else: index[val].append(i)
            count[val] = count.get(val, 0) + 1
        degree = max(count.values())
        ans = len(nums)
        for key, val in count.items():
            if val == degree:
                ans = min(ans, index[key][-1] - index[key][0] + 1)
        return ans