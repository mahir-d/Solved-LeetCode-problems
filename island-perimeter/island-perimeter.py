class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        total: int = 0
        for i in range(0, len(grid)):
            
            for j in range(0, len(grid[i])):
                if grid[i][j] == 0:
                    continue
                sum: int = 0
                
                if i > 0:
                  sum += 1 if self.helper(i-1, j, grid) else 0
                else: sum+=1
                # Going down
                if i < len(grid) - 1:
                    sum += 1 if self.helper(i+1, j, grid) else 0
                else: sum+=1
                #Going left
                if j > 0:  
                    sum += 1 if self.helper(i, j-1, grid) else 0
                else: sum+=1
                #Going right                    
                if j < len(grid[i]) - 1:
                    sum += 1 if self.helper(i, j+1, grid) else 0
                else: sum+=1
                total += sum
        return total
        
        
    def helper(self, i:int, j:int, grid: List[List[int]])-> bool:
        
            if grid[i][j] == 0:
                return True
            else: return False
            
                
                
                
    
