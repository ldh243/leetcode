class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        print(r, c)
        if r*c > (len(nums) * len(nums[0])):
            return nums
        arr = []
        row = []
        count = 0
        for i in range(0, len(nums)):
            for j in range(0, len(nums[0])):
                row.append(nums[i][j])
                if (i * len(nums[0]) + j + 1) % c == 0:
                    arr.append(row)
                    row = []
        return arr