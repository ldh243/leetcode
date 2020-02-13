class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        ans = 0
        prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        for i in range(L, R+1):
            count = bin(i).count("1")
            if count in prime: 
                ans += 1
        return ans