class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        all_min: List[int] = [False] * 24*60
        
        
        for time in timePoints:
            
            in_min = int(time[0:2]) * 60 + int(time[3:])
            
            if all_min[in_min]:
                return 0
            all_min[in_min] = True
            
        
        
        first,last, min_dif = -1, -1, float('inf')
        
        i = 0
        
        while i < 1440:
        
            if all_min[i]:
                if last != -1:
                    
                    min_dif = min(min_dif, i - last)
                
                last = i
                
                if first == -1:
                    first = i
                    
            i+=1
            
        return min(min_dif, 1440 - last + first)
