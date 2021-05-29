class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(i, j):
            m = len(grid)
            n = len(grid[0])    
            
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != "1":
                return
            
            grid[i][j] = "0"
            
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
            return 
            
        count = 0 
        m = len(grid)
        n = len(grid[0])  
        for i in range(m):
            for j in range(n):
                
                if grid[i][j] == "1":
                    dfs(i, j)
                    count+=1
        return count
        
        