class Solution(object):
    def backspaceCompare(self, S, T):
        s = t = ''
        for i in range(max(len(S), len(T))):
            if (i < len(S)):
                if S[i] == "#":
                    s = s[:-1]
                else:
                    s += S[i]
            if (i < len(T)):
                if T[i] == "#":
                    t = t[:-1]
                else:
                    t += T[i]
        return s == t
        