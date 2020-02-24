class Solution:
    def arrangeCoins(self, n: int) -> int:
        d = 1 + 8*n
        return (-1 + int(d**(1/2))) // 2