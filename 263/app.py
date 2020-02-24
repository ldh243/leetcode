class Solution:
    def isUgly(self, num: int) -> bool:
        if not num: return False
        while not num % 5:
            num //= 5
        while not num % 3:
            num //= 3
        while not num % 2:
            num //= 2
        return True if num == 1 else False