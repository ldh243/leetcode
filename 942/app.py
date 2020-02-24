class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        x, y = 0, len(S)
        ans = []
        for i in S:
            if i == 'I':
                ans.append(x)
                x += 1
            else:
                ans.append(y)
                y -= 1
        ans.append(x)
        return ans
