class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse( i):
            left = i 
            right = len(nums)-1
            while left < right:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
                
                left+=1
                right-=1
        
        idx = len(nums)-2
        
        while idx >= 0:
            
            if nums[idx] < nums[idx+1]:
                break
            
            idx-=1
        if idx==-1:
            nums.sort()
            return 
        
        nextIdx = idx+1
        
        while nextIdx < len(nums) and nums[nextIdx] > nums[idx]:
            nextIdx += 1
            
        nextIdx-=1
        
        temp = nums[nextIdx]
        nums[nextIdx] = nums[idx]
        nums[idx] = temp
        
    
        
        reverse(idx+1)
  
        return
        