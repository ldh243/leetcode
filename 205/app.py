class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dicS, dicT = {}, {}
        for i in range(len(s)):
            if not s[i] in dicS and not t[i] in dicT:
                dicS[s[i]] = t[i]
                dicT[t[i]] = s[i]
            elif s[i] not in dicS and t[i] in dicT or s[i] in dicS and t[i] not in dicT:
                return False
            elif dicS[s[i]] != t[i] or s[i] != dicT[t[i]]:
                return False
        return True
