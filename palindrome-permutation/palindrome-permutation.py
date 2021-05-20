class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        
        c_s = Counter(s)
        
        l_s = len(s)
        
        count_o = 0
        for k,v in c_s.items():
            if v % 2 != 0:
                count_o+=1
                
                
        if l_s % 2 != 0:
            return count_o <= 1
        else:
            return count_o == 0
        
            
            
        
        
        
        