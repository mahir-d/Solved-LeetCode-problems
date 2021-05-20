class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        if len(s1) == 0 or len(s2) == 0:
            return False
        
        
        s1_l = list(s1)
        s2_l = list(s2)
        
        left = 0
        right = left + len(s1)
        
        while right <= len(s2):
            
            if collections.Counter(s1) == collections.Counter(s2[left:right]):
                return True
            left += 1
            right +=1
            
            
        return False
        
        
        
        