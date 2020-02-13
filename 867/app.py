class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        n = len(A)
        m = len(A[0])
        ans = [[0] * n for i in range(m)]
        for i in range(n):
            for j in range(m):
                ans[j][i] = A[i][j]
        return ans