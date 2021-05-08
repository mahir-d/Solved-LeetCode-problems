class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        m = len(matrix)
        n = len(matrix[0])
        
        max_s = 0
        for i in range(m):
            max_s = max(max_s, int(matrix[i][0]))
            
        
        for i in range(n):
            max_s = max(max_s, int(matrix[0][i]))
        
        for i in range(1, m): 
            for j in range(1, n):
                if matrix[i][j] == "0":
                    continue
                matrix[i][j] = min(min(int(matrix[i-1][j]), int(matrix[i][j-1])), int(matrix[i-1][j-1])) + 1
                max_s = max(max_s, int(matrix[i][j]))
                
                
        return max_s * max_s
            