class Solution(object):
    def sortedSquares(self, A):
        return sorted(i*i for i in A)