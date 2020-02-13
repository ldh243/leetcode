class Solution(object):
    def getGroupOfFirstCharacter(self, s):
        g1 = 'qwertyuiop'
        g2 = 'asdfghjkl'
        g3 = 'zxcvbnm'
        if s[0] in g1: return g1
        elif s[0] in g2:
            return g2
        return g3
    def check(self, word, group):
        for i in word:
            if not i in group:
                return False
        return True
    def findWords(self, words):
        for index, word in reversed(list(enumerate(words))):
            g = self.getGroupOfFirstCharacter(word.lower())
            if not self.check(word.lower(), g):
                del words[index]
        return words
