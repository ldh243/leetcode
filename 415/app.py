class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        while len(num1) > len(num2):
            num2 = '0' + num2
        while len(num2) > len(num1):
            num1 = '0' + num1
        n = len(num1)
        odd = 0
        ans = ''
        for i in range(n-1, -1, -1):
            s1 = int(num1[i])
            s2 = int(num2[i])
            sum = s1 + s2 + odd
            odd = sum // 10
            sum = sum % 10
            ans = str(sum) + ans
        return '1'+ans if odd else ans