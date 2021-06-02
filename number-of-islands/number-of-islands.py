class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        direc = [(0,1),(0,-1), (-1,0),(1,0)]
        
        
        
        def dfs(i,j):
            
            grid[i][j] = "0"
            
            for d in range(4):
                
                new_i = i + direc[d][0]
                new_j = j + direc[d][1]
                
                if new_i < 0 or new_i >= m or new_j < 0 or new_j >= n or grid[new_i][new_j] == "0":
                    continue
                dfs(new_i, new_j)
                
            
        num_islands = 0    
        for i in range(m):
            for j in range(n):
                if grid[i][j] != "0":
                    dfs(i,j)
                    num_islands += 1
        return num_islands
    