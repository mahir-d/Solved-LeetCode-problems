class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        t_len  = len(triangle)
        
        if t_len == 0:
            return 0
        
        if t_len == 1:
            return triangle[0][0]
        
        for i in range(t_len-2, -1,-1):
            
            for j in range(len(triangle[i])):
                
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
                
        return triangle[0][0]