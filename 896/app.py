class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if len(A) <= 2: return True
        isIncrease = True if A[-1] - A[0] >= 0 else False
        for i in range(1, len(A)):
            if isIncrease and A[i-1] - A[i]>0:
                return False
            elif not isIncrease and A[i] - A[i-1]>0:
                return False
        return True
