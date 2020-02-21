class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minNum = float('inf')
        ans = 0
        for i in prices:
            if i >= minNum:
                ans = max(ans, i - minNum)
            else: minNum = i
        return ans
