class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        dic = {}
        for i in A.split(" "):
            if not i in dic:
                dic[i] = True
            else:
                dic[i] = False
        for i in B.split(" "):
            if not i in dic:
                dic[i] = True
            else:
                dic[i] = False
        return [k for k, v in dic.items() if v]