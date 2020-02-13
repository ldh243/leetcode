class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        def checkSelf(number):
            temp = number
            while temp > 0:
                digit = temp % 10
                if number % digit != 0: return False    
                temp //= 10
            return True
        for i in range(left, right + 1):
            if '0' not in str(i) and checkSelf(i): 
                ans.append(i)
        return ans