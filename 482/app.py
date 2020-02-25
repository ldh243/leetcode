class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        ans, count = '', 0
        S = S.replace("-", "").upper()
        if not S: return ""
        i = len(S)-1
        while i >= 0:
            count = 0
            for j in range(i, max(i-K, -1), -1):	
                ans += S[j]
            i -= K
            ans += '-'
        return ans[::-1][1:] if ans[-1] == '-' else ans[::-1]