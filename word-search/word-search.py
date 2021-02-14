class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                
                if board[i][j] == word[0]:
                    if self.helper(i,j,board,word, 0):
                        return True
        
        return False
    def helper(self, row, col, board, word, i):
        
        if i == len(word):
            return True
        
        if row < 0 or row >= len(board) or col >= len(board[0]) or col < 0:
            return False
        
        if word[i] != board[row][col]:
            return False
        
        flag = False
        temp = board[row][col]
        board[row][col] = "*"
        
        flag = self.helper(row+1,col,board,word,i+1) or self.helper(row-1, col, board,word,i+1) or self.helper(row,col+1, board,word,i+1) or self.helper(row, col-1, board, word, i+1)
       
        board[row][col] = temp
        return flag
        
        
        
        
    
            
                
            
            