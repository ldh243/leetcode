class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        t = [s[i:i+k] for i in range(0, len(s), k)]
        for i in range(0,len(t),2):
            print(t[i])
            t[i] = t[i][::-1]
        ans = "".join(t)
        return ans