class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
        zero_idx: int = 0
        nums_len: int = len(nums)
        
        while zero_idx < nums_len:
            
            while zero_idx < nums_len and nums[zero_idx] != 0:
                zero_idx += 1
            
            
            
            non_zero = zero_idx + 1
            
            while non_zero < nums_len and nums[non_zero] == 0:
                non_zero += 1
                
             
            if non_zero < nums_len and non_zero > zero_idx:
                
                nums[zero_idx] = nums[non_zero]
                nums[non_zero] = 0
                
            zero_idx += 1
            
