class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        direR = [0,1,0,-1]
        direC = [1,0,-1,0]
        visited = set()
        directions = [0,1,2,3]
        result = []
        m = len(matrix)
        n = len(matrix[0])
        
        def backtrack(i, j, d):
            
            print(result)
            
            if i < 0 or i >= m or j < 0 or j >= n or (i,j) in visited:
                return 
            
            result.append(matrix[i][j])
            visited.add((i,j))
            
            new_i = direR[d] + i
            new_j = direC[d] + j
            
            
            
            if new_i < 0 or new_i >= m or new_j < 0 or new_j >= n or (new_i,new_j) in visited:
                d = (d+1) % 4
                backtrack(i + direR[d],j + direC[d],d)
                return 
            else:
                backtrack(new_i, new_j, d)
        
        
        backtrack(0,0,0)
        return result
        
                