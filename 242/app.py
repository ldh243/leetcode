class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        if len(s) != len(t): 
            return False
        for i in range(len(s)):
            if s[i] in dic:
                dic[s[i]] += 1
            else: dic[s[i]] = 1
            if t[i] in dic:
                dic[t[i]] -= 1
            else: dic[t[i]] = -1
        for key, val in dic.items():
            if val != 0:
                return False
        return True