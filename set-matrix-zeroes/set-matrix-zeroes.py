class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        row_z = [0] * m
        col_z = [0] * n
        
        def check_zero_row(row) -> bool:
            
            for j in range(n):
                
                if matrix[row][j] == 0:
                    return True
            return False
        
        def check_zero_col(col):
                
            for i in range(m):
                if matrix[i][col] == 0:
                    return True
            return False
        
        for i in range(m):
            
            if check_zero_row(i):
                row_z[i] = 0
            else:
                row_z[i] = matrix[i][0]
        for j in range(n):
            
            if check_zero_col(j):
                col_z[j] = 0
            else:
                col_z[j] = matrix[0][j]
        
        
        for i in range(m):
            if row_z[i] == 0:
                for j in range(n):
                    matrix[i][j] = 0
        for j in range(n):
            if col_z[j] == 0:
                for i in range(m):
                    matrix[i][j] = 0
        
        return 
            
            
            
            
            
            
            
        
        