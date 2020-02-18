class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def check(row, col, oldColor):
            if row < 0 or col < 0 or row >= len(image) or col >= len(image[0]) or not image[row][col] == oldColor:
                return False
            return True
        def bfs(row, col):
            queue = [[row, col]]
            direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            oldColor = image[row][col]
            while queue:
                row, col = queue.pop(0)
                for i in direction:
                    if check(row + i[0], col + i[1], oldColor):
                        queue.append([row + i[0], col + i[1]])
                image[row][col] = newColor
        if image[sr][sc] == newColor:
            return image
        bfs(sr, sc)
        return image