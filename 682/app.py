class Solution(object):
    def calPoints(self, ops):
        arr = []
        ans = 0
        for i in ops:
            if i == '+':
                ans += arr[-1] + arr[-2]
                arr.append(int(arr[-1] + arr[-2]))
            elif i == 'C':
                ans -= arr[-1]
                del arr[-1]
            elif i == 'D':
                ans += arr[-1] * 2
                point = arr[-1] * 2
                arr.append(int(arr[-1] * 2))

            else:
                ans += int(i)
                point = i
                arr.append(int(i))
        return ans