class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        B = []
        for i in range(0, len(A)):
            row = []
            for j in reversed(range(len(A[0]))):
                row.append(0 if A[i][j] else 1)
            B.append(row)
        return B