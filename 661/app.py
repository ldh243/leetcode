class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        n, m = len(M), len(M[0])
        ans = [[0] * m for i in range(n)]
        for i in range(n):
            for j in range(m):
                count = 0
                for x in (i-1, i, i+1):
                    for y in (j-1, j, j+1):
                        if 0 <= x < n and 0 <= y < m:
                            ans[i][j] += M[x][y]
                            count += 1
                ans[i][j] //= count
        return ans