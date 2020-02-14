class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i in dic:
                dic.pop(i)
            else: 
                dic[i] = True
        return list(dic.keys())[0]