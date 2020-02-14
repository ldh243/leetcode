class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def check(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or not grid[i][j]:
                return False
            grid[i][j] = 0
            return True		
        def bfs(i, j):
            queue = [[i, j]]
            cur = -1
            while len(queue) - 1 > cur :
                cur += 1
                x, y = queue[cur]
                grid[x][y] = 0
                if check(x-1,y):
                    queue.append([x-1,y])
                if check(x+1,y):
                    queue.append([x+1,y])
                if check(x,y-1):
                    queue.append([x,y-1])
                if check(x,y+1):
                    queue.append([x,y+1])
            return cur + 1
        ans,n, m = 0, len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    ans = max(ans, bfs(i, j))
        return ans

