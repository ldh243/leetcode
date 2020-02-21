class Solution:
    def checkRecord(self, s: str) -> bool:
        A = 0
        L = 0
        for i in s:
            if i == 'A':
                A += 1
                if A > 1: return False
            if i == 'L':
                L += 1
                if L > 2: return False
            else: L = 0
        return True