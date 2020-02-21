class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0
        for i in points:
            dis = {}
            for j in points:
                if i == j: continue
                distance = (i[0] - j[0])**2 + (i[1] - j[1])**2
                temp = dis.get(distance, 0)
                ans += temp * 2
                dis[distance] = temp + 1
        return ans
