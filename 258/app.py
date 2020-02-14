class Solution:
    def addDigits(self, num: int) -> int:
        if num<10: return num        
        return 9 if not num%9 else num%9