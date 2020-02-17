class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        group, ans = [1], 0
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                if len(group) >= 2:
                    ans += min(group[-1], group[-2])
                group.append(1)
            else:
                group[len(group)-1] += 1
        if len(group) <= 1: return 0
        return (ans + min(group[-1], group[-2]))