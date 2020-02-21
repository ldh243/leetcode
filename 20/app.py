class Solution:
    def isValid(self, s: str) -> bool:
        openBracket = ['(', '{', '[']
        pair = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for i in s:
            if not i in openBracket:
                if not stack or pair[stack[-1]] != i: return False
                stack.pop(-1)
            else:
                stack.append(i)
        return not stack