class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        
        slow = 0
        
        
        
        for fast in range(len(nums)):
            
            
            if nums[slow] == nums[fast]:
                continue
            slow+=1
            nums[slow] = nums[fast]
            
            
        return slow+1