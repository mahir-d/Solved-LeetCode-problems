class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        
        visited = set()
        result = []
        m = len(matrix)
        n = len(matrix[0])
        dir_r = [0,1,0,-1]
        dir_c = [1,0,-1,0]
        
        
        def dfs(i, j,direc):
            print(i, " ", j)
            if i < 0 or i >= m or j < 0 or j>= n or (i, j) in visited:
                return
            
            result.append(matrix[i][j])
            visited.add((i,j))
            new_i = i+dir_r[direc]
            new_j = j+dir_c[direc]
            if new_i < 0 or new_i >= m or new_j < 0 or new_j >= n or (new_i,new_j) in visited:
                new_dir = (direc+1)%4
                dfs(i+dir_r[new_dir],j+dir_c[new_dir],new_dir)
                return
            
            dfs(new_i,new_j,direc)
            return
            
        
        dfs(0,0,0)
        return result
            
        