class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = {}
        for i in magazine:
            if not i in dic:
                dic[i] = 1
            else: dic[i] += 1
        for i in ransomNote:
            if not i in dic:
                return False
            elif i in dic and dic[i] <= 0:
                return False
            else: dic[i] -= 1
        return True