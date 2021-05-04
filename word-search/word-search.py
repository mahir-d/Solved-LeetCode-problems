class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        x = len(board)
        y = len(board[0])
        
        def dfs(i,j,index):
            if index == len(word):
                return True
            if i<0 or i>= len(board) or j<0 or j>=len(board[0]) or board[i][j] != word[index]:
                return False
            temp = board[i][j]
            board[i][j] = "*"
            
            x = dfs(i-1,j,index+1) or dfs(i+1,j,index+1) or dfs(i,j+1,index+1) or dfs(i,j-1,index+1)
            
            board[i][j] = temp
            return x
        for i in range(x):
            for j in range(y):
                if board[i][j] == word[0]:
                    if dfs(i,j,0):
                        return True
        return False






