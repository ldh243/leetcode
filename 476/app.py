class Solution:
    def flip(self, i):
        if i == '0': return '1'
        return '0'
    def findComplement(self, num: int) -> int:
        a = bin(num)[2:]
        return (int(''.join(self.flip(i) 
                    for i in a), 2))
