class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        def toBin(n):
          return bin(n)[2:]

        binX = toBin(x)
        binY = toBin(y)

        while len(binX) > len(binY):
          binY = '0' + binY

        while len(binY) > len(binX):
          binX = '0' + binX

        print(binX)
        print(binY)
        ans = 0
        for i in range(0, len(binX)):
          if binX[i] != binY[i]:
            ans += 1
        return ans