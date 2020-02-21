class Solution:
    def isHappy(self, n: int) -> bool:
        setN = set()
        while n != 1:
            if n in setN:
                return False
            setN.add(n)
            sum = 0
            for i in str(n):
                sum += int(i)**2
            n = sum
        return True