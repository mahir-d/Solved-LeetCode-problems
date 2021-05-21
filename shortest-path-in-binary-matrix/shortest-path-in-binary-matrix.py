class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        dire_r = [0,0,-1,1,-1,-1,1,1]
        dire_c = [1,-1,0,0,-1,1,1,-1]
        
        queue = [(0,0)]
        
        level = 1

        m = len(grid)
        n = len(grid[0])
        
        while queue:
        
            len_q = len(queue)
            
            for _ in range(len_q):
                
                curr_i, curr_j = queue.pop(0)
                
                if curr_i == m-1 and curr_j == n-1:
                    return level
                
                for d in range(len(dire_r)):
                    
                    new_i = curr_i + dire_r[d]
                    new_j = curr_j + dire_c[d]
                    
                    if new_i < 0 or new_i >= m or new_j < 0 or new_j >= n or grid[new_i][new_j] != 0:
                        continue
                    grid[new_i][new_j] = 2
                    queue.append((new_i, new_j))
                    
                
            level+=1
        return -1
                    
                    
                    
                    
                