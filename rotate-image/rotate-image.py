class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        m = len(matrix)
        n = len(matrix[0])
        
        
        
        def transpose():
            
            for i in range(m):
                for j in range(i, n):
                    
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                    
            
            
            
            
        def reflect():
            
            for i in range(m):
                
                left = 0
                right = n-1
                    
                while left < right:
                    temp = matrix[i][left]
                    matrix[i][left] = matrix[i][right]
                    matrix[i][right] = temp
                    
                    left+=1
                    right-=1
            return 
    
        transpose()
        reflect()
                    