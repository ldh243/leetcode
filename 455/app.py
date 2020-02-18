class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i = j = ans = 0
        g.sort()
        s.sort()
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                ans += 1
                i += 1
                j += 1
            elif g[i] > s[j]:
                j += 1
        return ans