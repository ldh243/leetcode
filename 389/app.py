class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dic = {}
        for i in s:
            if not i in dic:
                dic[i] = 1
            else: dic[i] += 1
        for i in t:
            if not i in dic:
                return i
            else:
                if dic[i]:
                    dic[i] -= 1
                else:
                    return i