class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = {}
        odd = 0
        ans = 0
        for i in range(len(s)):
            dic[s[i]] = dic.get(s[i], 0) + 1
        for k,v in dic.items():
            if v%2: odd = 1
            ans += v-v%2
        return ans+odd