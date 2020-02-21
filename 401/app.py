class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        ans = []
        for h in range(12):
            for m in range(60):
                if bin(h)[2:].count('1') + bin(m)[2:].count('1') == num:
                    ans.append("{}:{}{}".format(h,m//10,m%10))
        return ans