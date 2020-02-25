class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dic = set()
        for i in nums:
            if i in dic:
                temp = i
                break
            dic.add(i)
        return [temp, sum(range(len(nums)+1)) - sum(nums) + temp]