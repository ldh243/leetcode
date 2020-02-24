class Solution:
    def compress(self, chars: List[str]) -> int:
        x, y = 0, 0
        while y < len(chars):
            chars[x] = chars[y]
            count = 1
            while y + 1 < len(chars) and chars[y] == chars[y+1]:
                y += 1
                count += 1
            if count > 1:
                for i in str(count):
                    x += 1
                    chars[x] = i
            x += 1
            y += 1
        return x