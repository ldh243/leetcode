class Solution:
    def convertToBase7(self, num: int) -> str:
        nega = 1
        if not num: return '0'
        if num < 0: 
            num*=-1
            nega = -1
        ans = ''
        while num:
            ans = str(num%7) + ans
            num //= 7
        return str(int(ans)*nega)