class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        maxNum = A[0]
        pos = 0
        for index, val in enumerate(A):
            if (val > maxNum):
                maxNum = val
                pos = index
        return pos