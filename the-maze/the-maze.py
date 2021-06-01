class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        
        
        if maze[start[0]][start[1]] == 1 or maze[destination[0]][destination[1]] == 1:
            return False
        
        m = len(maze)
        n = len(maze[0])
        direc = [(0,1), (1,0),(-1,0),(0,-1)]
        block = set()
        
        def dfs(i, j):
            if i == destination[0] and j == destination[1]:
                return True
            
            for d in range(4):
                new_i = direc[d][0] + i 
                new_j = direc[d][1] + j
                
                while new_i >= 0 and new_i < m and new_j >= 0 and new_j < n and maze[new_i][new_j] == 0:
                    
                    new_i += direc[d][0]
                    new_j += direc[d][1]
                    
                if (new_i- direc[d][0], new_j - direc[d][1]) not in block:
                    block.add((new_i- direc[d][0], new_j- direc[d][1]))
                    if dfs(new_i - direc[d][0], new_j - direc[d][1]):
                        return True
                    
            return False
                
                    
                
                
                
#         for i in range(m):
#             for j in range(n):
                
#                 if maze[i][j] == 1:
#                     block.add((i,j))
                    
        
        return dfs(start[0], start[1])
        
                
            