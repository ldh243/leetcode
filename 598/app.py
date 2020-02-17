class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        while ops:
            x,y = ops.pop()
            m = min(m, x)
            n = min(n, y)
        return m*n