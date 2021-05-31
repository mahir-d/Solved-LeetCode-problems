class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        start = (0,0)
        
        direc = [(0,1),(0,-1),(1,0),(-1,0)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "*":
                    start = (i, j)
                    break
        
        queue = [start]
        
        
        
        def bfs():
            level = 0
            while queue:
                len_q = len(queue)
            
            
                for _ in range(len_q):
                    
                    i,j = queue.pop(0)
                    if grid[i][j] == "#":
                        return level
                    
                    grid[i][j] = "X"
                    
                    for d in range(4):
                        new_i = i + direc[d][0]
                        new_j = j + direc[d][1]
                        
                        if new_i < 0 or new_i >= m or new_j < 0 or new_j >= n or grid[new_i][new_j] == "X":
                            continue
                        if grid[new_i][new_j] == "#":
                            return level+1
                        queue.append((new_i,new_j))
                        grid[new_i][new_j] = "X"
                
                level+=1
            return -1
        
        return bfs()
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            