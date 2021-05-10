class Solution:
    def trap(self, height: List[int]) -> int:
        
        
        max_left = height[:]
        max_right = height[:]
        
        curr_max = 0
        for i in range(0, len(max_left)):
            
            max_left[i] = curr_max
            curr_max = max(curr_max, height[i])
            
        curr_max = 0
        for i in range(len(height)-1, -1,-1):
            max_right[i] = curr_max
            curr_max = max(curr_max, height[i])
            
        
        curr_volume = 0
        
        for i in range(len(height)):
            min_h = min(max_left[i], max_right[i])
            if min_h > height[i]:
                curr_volume += min_h - height[i]
            
        return curr_volume
            
            
            
            
            
            