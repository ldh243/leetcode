class Solution:
    def getSum(self, n: int, m: int) -> int:
        
        mask = 0b11111111111111111111111111111111
        while m&mask:
            carry = (n&m)<<1
            n = n^m
            m = carry

        return n&mask if m > mask else n