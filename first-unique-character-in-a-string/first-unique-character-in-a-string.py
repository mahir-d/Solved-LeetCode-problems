class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        my_map = defaultdict(list)
        
        
        
        for idx,l in enumerate(s):
            
            my_map[l].append(idx)
            
        
        
        
        for l in s:
            
            if len(my_map[l]) == 1:
                return my_map[l][0]
        
        return -1
            
            
        