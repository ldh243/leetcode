class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        setNum, setAns = set(), set()
        n = len(nums)
        for i in range(len(nums)):
            setNum.add(nums[i])
            setAns.add(i+1)
        return(list(setNum.symmetric_difference(setAns)))