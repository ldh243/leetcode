class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        reverse = [val for i, val in enumerate(S) if 65 <= ord(val.upper()) <= 90][::-1]
        ans = ""
        j = 0
        for i in range(len(S)):
            if 65 <= ord(S[i].upper()) <= 90:
                ans += reverse[j]
                j+=1
            else:
                ans += S[i]
        return ans