class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        result = []
        diag = set()
        antiDiag = set()
        c = set()
        
        board = [["."] * n for _ in range(n)]
        
        
        
        def backtrack(row):
            # print(row)
            if row >= n:
                temp = ["".join(line) for line in board]
                result.append(temp)
                return 
            
            
            for j in range(n):
                
                if j in c or row-j in diag or row+j in antiDiag:
                    continue
                c.add(j)
                diag.add(row-j)
                antiDiag.add(row+j)
                board[row][j] = "Q"
                backtrack(row+1)
                c.remove(j)
                diag.remove(row-j)
                antiDiag.remove(row+j)
                board[row][j] = "."
        backtrack(0)
        return result
                
                
                
                
                
                
        