class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ''
        for i in s:
            if i in 'ueoaiUEOAI':
                vowels = i + vowels

        ans, x = '', 0
        for i in s:
            if i in 'ueoaiUEOAI':
                ans += vowels[x]
                x += 1
            else: ans += i 

        return ans