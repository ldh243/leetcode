class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n < 5:
            return 0
        ans = 0
        while n: 
            n = n // 5
            ans += n
        return ans