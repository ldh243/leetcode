class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        for i in range(int(area**0.5), 0, -1):
            if not area % i:
                if i >= int(area/i): return [i, int(area/i)]
                return [int(area/i), i]