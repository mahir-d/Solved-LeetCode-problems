class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        m =len(grid)
        n = len(grid[0])
        
        direc = [(0,1),(0,-1),(-1,0),(1,0),(1,1),(-1,-1),(-1,1),(1,-1)]
        
        
        queue = [(0,0)]
        
        visited = set()
        level = 1        
        while queue:
            
            len_q = len(queue)
            
            for _ in range(len_q):
                
                curr_i, curr_j = queue.pop(0)
                
                if curr_i == m-1 and curr_j == n-1:
                    return level
                
                for d in range(8):
                    new_i = curr_i + direc[d][0]
                    new_j = curr_j + direc[d][1]
                    
                    if new_i < 0 or new_i >= m or new_j < 0 or new_j >= n or (new_i, new_j) in visited or grid[new_i][new_j]!=0:
                        continue
                    visited.add((new_i, new_j))
                    queue.append((new_i, new_j))
                    
            level += 1
        
        return -1
        