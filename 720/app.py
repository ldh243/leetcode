class Solution:
    def longestWord(self, words: List[str]) -> str:
        words = sorted(words)

        dic = {}
        for i in words:
            if len(i) == 1:
                dic[i] = 1
                continue;
            if i[0:len(i)-1] in dic:
                dic[i] = dic[i[0:len(i)-1]] + 1
        return max(dic, key=dic.get)