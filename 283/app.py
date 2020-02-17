class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        num0 = 0
        for i in range(len(nums)-1, -1, -1):
            if not nums[i]:
                del nums[i]
                num0 += 1
        while num0:
            nums.append(0)
            num0 -= 1
        return(nums)