class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        # if triangle
        len_t = len(triangle)         
        for i in range(len(triangle)-2, -1, -1):
            
            for j in range(0,len(triangle[i])):                
                total = float('inf')
                total = min(total, triangle[i+1][j])
                total = min(total, triangle[i+1][j+1])
                triangle[i][j] += total
                     
                    
        return triangle[0][0]