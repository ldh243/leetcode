class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        if numRows == 0: return ans
        ans.append([1])
        if numRows == 1: return ans
        for i in range(1, numRows):
            row = ans[-1][:]
            for j in range(1, i):	
                row[j-1] += row[j]
            row.pop(-1)
            row = [1 ]+ row + [1]
            ans.append(row)
        return ans
