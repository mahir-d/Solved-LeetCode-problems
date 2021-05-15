class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        visited = set()
        
        for i in range(m):

            for j in range(n):
                
                if board[i][j] == word[0] and self.dfs(i, j, board,word, 0, visited):
                    return True
                
        
        return False
    
    def dfs(self, i, j, board, word,idx, visited):
        
        m = len(board)
        n = len(board[0])
        
        if idx >= len(word):
            return True
        
        if i < 0 or i >= m or j < 0 or j >= n or (i, j) in visited or  word[idx] != board[i][j]:
            return False
        
        visited.add((i,j))
        flag = self.dfs(i+1,j,board, word, idx+1,visited) or self.dfs(i-1,j,board, word, idx+1,visited) or self.dfs(i,j+1,board, word, idx+1,visited) or self.dfs(i,j-1,board, word, idx+1,visited)
        visited.remove((i,j))
        return flag
        
        