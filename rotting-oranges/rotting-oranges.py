class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        
        
        direc = [(1,0), (-1,0), (0,1), (0,-1)]
        queue = []
        fresh = 0
        for i in range(m):
            for j in range(n):
            
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0
        
        level = -1
        
        
        while queue:
            # print(queue)
            # print(level)
            len_q = len(queue)
            
            for _ in range(len_q):
                
                i,j = queue.pop(0)
                for d in range(len(direc)):
                    new_i = i + direc[d][0]
                    new_j = j + direc[d][1]
                    
                    if new_i < 0 or new_i >= m or new_j < 0 or new_j >= n or grid[new_i][new_j] != 1:
                        continue
                    grid[new_i][new_j] = 2
                    fresh -= 1
                    queue.append((new_i, new_j))
                        
            level += 1
            
            
        return level if fresh == 0 else -1
            