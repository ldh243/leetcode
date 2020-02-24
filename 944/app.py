class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        n, m = len(A), len(A[0])
        ans = 0
        for j in range(m):
            stack = [A[i][j] for i in range(n)]
            if stack != sorted(stack):
                ans += 1
        return ans