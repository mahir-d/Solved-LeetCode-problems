class Solution:
    def maxDepth(self, s: str) -> int:
        
        
        total: int = 0
        max_nest: int = 0
        s_len: int = len(s)            
        
        for i in range(0, s_len):
            
            if s[i] == '(':
                
                total += 1
                 
            elif s[i] == ')':
                max_nest = max(total, max_nest)
                total -= 1
                
                
        return max_nest
    
            
