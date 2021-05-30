class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height:
            return 0
        
        max_left = [0] * len(height)
        max_right = [0] * len(height)
        
        max_height = height[0]
        
        for i in range(1, len(height)):
            
            max_left[i] = max_height
            max_height = max(max_height, height[i])
            
        max_height = height[-1]
        
        for i in range(len(height)-2,-1, -1):
            max_right[i] = max_height
            max_height = max(max_height, height[i])
            
        # print(max_left)
        # print(max_right)
        
        
        total = 0
        for i in range(1, len(height)-1):
            if min(max_left[i], max_right[i]) > height[i]:
                total += (min(max_left[i], max_right[i])  - height[i])
            
            
        return total