class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        ans = 0
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    for x in range(i-1, -1, -1):
                        if board[x][j] != '.':
                            if board[x][j] == 'p': ans+=1
                            break
                    for x in range(i+1, 8):
                        if board[x][j] != '.':
                            if board[x][j] == 'p': ans+=1
                            break
                    for x in range(j-1, -1, -1):
                        if board[i][x] != '.':
                            if board[i][x] == 'p': ans+=1
                            break
                    for x in range(j+1, 8):
                        if board[i][x] != '.':
                            if board[i][x] == 'p': ans+=1
                            break
        return ans