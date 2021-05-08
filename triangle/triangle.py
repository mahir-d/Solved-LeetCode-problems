class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        m = len(triangle)
        
        
        if not triangle:
            return 0
        if len(triangle) == 1:
            return triangle[0][0]
    
    
        for i in range(m-2, -1, -1):
            
            for j in range(len(triangle[i])):
                
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
                
        return triangle[0][0]
            
            