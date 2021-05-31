class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        direc = [(0,1), (0,-1), (1,0),(-1,0)]
        
        def dfs(i, j):
            
            count = 1
            
            grid[i][j] = 0
            
            for d in range(4):
                
                new_i = direc[d][0] + i
                new_j = direc[d][1] + j
                
                if new_i < 0 or new_j < 0 or new_i >= m or new_j >= n or grid[new_i][new_j] == 0:
                    continue
                
                count+=dfs(new_i, new_j)
            return count 
        
                
        m = len(grid)
        n = len(grid[0])
        max_area = 0
        for i in range(m):
            for j in range(n):  
                
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))
        return max_area