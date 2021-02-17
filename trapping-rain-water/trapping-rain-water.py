class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height:
            return 0
            
        
        left = 0
        right = len(height) - 1
        l_max = height[left]
        r_max = height[right]
        
        
        water = 0
        
        while left < right:
            
            if height[left] < height[right]:
                water +=  min(l_max,r_max) - height[left]
                left+=1
            elif height[right] < height[left]:
                water += min(r_max, l_max) - height[right]
                right-=1
            else:
                right-=1
            
            l_max = max(l_max,height[left])
            r_max = max(r_max, height[right])
            
            
        return water
        
            