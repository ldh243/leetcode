class Solution:
    def nextGreaterElement(self, arr1, arr2):
        stack = []
        dic = {}
        for i in arr2:
            while stack and stack[-1] < i:
                dic[stack[-1]] = i 
                stack.pop()
            stack.append(i)
        ans = []
        for i in arr1:
            if i not in dic:
                ans.append(-1)
            else: 
                ans.append(dic[i])
        return ans
    