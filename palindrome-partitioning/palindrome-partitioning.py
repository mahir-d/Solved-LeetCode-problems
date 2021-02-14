class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        
        
        result = []
        
        def helper(i ,combo):
            
            if i == len(s):
                result.append(combo[:])
                
            for j in range(i, len(s)):
                
                temp = s[i:j+1]
                
                if temp == temp[::-1]:
                    combo.append(temp)
                    helper(j+1, combo)
                    combo.pop()
            return
                    
                
                
            
            
        helper(0, [])
        return result