class Solution:
    def titleToNumber(self, s: str) -> int:
        powNum = len(s) - 1
        ans = 0
        for i in s:
            res = ord(i.upper()) - 64
            res *= 26**powNum
            powNum -= 1
            ans += res
        return ans
