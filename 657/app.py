class Solution:
    def judgeCircle(self, moves: str) -> bool:
        R = moves.count('R')
        L = moves.count('L')
        U = moves.count('U')
        D = moves.count('D')
        return U == D and L == R