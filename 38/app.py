class Solution:
    def countAndSay(self, n: int) -> str:
        ans = "1"
        for i in range(2, n+1):
            temp = ans
            ans = ''
            last = temp[0]
            count = 0 

            for j in temp:
                if j == last:
                    count += 1
                else: 
                    ans += str(count) + last
                    count = 1
                    last = j
            ans += str(count) + last
        return ans