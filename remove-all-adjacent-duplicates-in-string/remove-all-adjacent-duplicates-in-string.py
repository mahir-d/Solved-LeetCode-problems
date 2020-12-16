class Solution:
    
    
    def removeDuplicates(self, S: str) -> str:
        
        stack: List[int] = []
            
            
        for s in S:
            
            if len(stack) != 0:
                if stack[-1] != s:
                    stack.append(s)
                else:
                    stack.pop()
                    
            else:
                stack.append(s)
                
        return "".join([w for w in stack])
                
            
        
