class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        fresh = 0
        queue = []
        
        
        for i in range(m):
            for j in range(n):
                
                if grid[i][j] == 2:
                    queue.append((i,j))
                if grid[i][j] == 1:
                    fresh+=1
                    
        print(fresh, queue)
        if fresh == 0:
            return 0
        # if len(queue) == 0:
        #     return 0
        
        level = -1
        direc = [(0,1),(0,-1),(-1,0),(1,0)]
        while queue:
            
            len_q = len(queue)
            for _ in range(len_q):
                
                curr_i, curr_j = queue.pop(0)
                
                
                for d in range(4):
                    new_i = curr_i + direc[d][0]
                    new_j = curr_j + direc[d][1]
                    
                    if new_i < 0 or new_i >= m or new_j < 0 or new_j >= n or grid[new_i][new_j] != 1:
                        continue
                    
                    
                    grid[new_i][new_j] = 2  
                    fresh-=1
                    queue.append((new_i, new_j))
                
                
            level += 1
        
        return level if fresh == 0 else -1
        
    
        