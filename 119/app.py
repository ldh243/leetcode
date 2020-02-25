class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1]
        if rowIndex == 1: return [1, 1]
        ans = [1, 1]
        for i in range(2, rowIndex+1):
            for j in range(1, i):
                ans[j-1] += ans[j]
            ans.pop(-1)
            ans = [1] + ans + [1]
        return ans