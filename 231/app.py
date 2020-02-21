class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return True if bin(n).count('1') == 1 and n > 0 else False