class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        grid = [[0] * n for _ in range(m)]
        
        for i in range(m):
            
            if obstacleGrid[i][0] == 1:
                break
            
            grid[i][0] = 1
            
        for i in range(n):
            
            if obstacleGrid[0][i] == 1:
                break
            grid[0][i] = 1
            
        
        for i in range(1, m):
            for j in range(1, n):
                
                if obstacleGrid[i][j] == 1:
                    continue
                
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
                
        return grid[-1][-1]
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                
            
            