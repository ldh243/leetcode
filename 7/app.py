class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0: 
            x *= -1
            sign = -1
        ans = int(str(x)[::-1])*sign
        return ans if -2**31 < ans < 2**31-1 else 0