class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        
        dp = [[0] * n for _ in range(m)]
        trav = [(0,-1), (0,1), (-1,0), (1,0), (-1,-1), (-1,1),(1,-1),(1,1)]
        
        def helper(i, j):
            
            if i < 0 or i>=m or j < 0 or j >= n:
                return 0
            return board[i][j]        
        
        for i in range(m):
        
            for j in range(n):
                
                count = 0
                
                for k in range(len(trav)):
                    curr_i, curr_j = trav[k] 
                    count += helper(curr_i+i,curr_j+j)
                
                if board[i][j] == 1:
                    if count < 2:
                        dp[i][j] = 0
                    elif  count > 3:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = 1
                    
                else:
                    if count == 3:
                        dp[i][j] = 1
        
        for i in range(m):
            for j in range(n):
                
                board[i][j] = dp[i][j]
                
        

                
        