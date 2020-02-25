class Solution:
    def toHex(self, num: int) -> str:
        if num == 0: return "0"
        mp = "0123456789abcdef"
        rs = ""
        for i in range(8):
            rs = mp[num % 16] + rs
            num = num // 16

        return rs.lstrip('0')