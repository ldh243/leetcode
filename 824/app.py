class Solution:
    def convert(self, word):
        if word[0] not in 'ueoaiUEOAI':
            word = word[1:] + word[:1]
        return word + 'ma'
    def toGoatLatin(self, S: str) -> str:
        ans = ''
        for i, word in enumerate(S.split(), 1):
            ans += self.convert(word) + 'a' * i + " "
        return ans.strip()