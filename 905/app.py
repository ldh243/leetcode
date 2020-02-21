class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        ans = [0] * len(A)
        x,y = 0, len(A)-1
        for i in A:
            if not i % 2: 
                ans[x] = i
                x+=1
            else:
                ans[y] = i
                y-=1
        return ans