class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for i, val in enumerate(numbers):
            if target - val in dic:
                return [dic[target - val] + 1, i + 1]
            if not val in dic:
                dic[val] = i