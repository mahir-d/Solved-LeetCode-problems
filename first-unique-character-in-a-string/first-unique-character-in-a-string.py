class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        my_dict: Dict[int: int] = {} 
        
        for c in s:
            if c in my_dict:
                
                my_dict[c] += 1
            
            else:
                
                my_dict[c] = 1
​
                
        for c in range(0, len(s)):
            
            if my_dict[s[c]] == 1:
                return c
            
            
        return -1
            
