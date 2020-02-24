class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        odd = 0
        digits[len(digits)-1] += 1
        for i in range(len(digits)-1, -1, -1):
            digits[i] += odd
            odd = digits[i] // 10
            digits[i] %= 10
        return digits if not odd else [1] + digits