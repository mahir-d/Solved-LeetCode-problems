class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_p = 0
        
        non_z = 0
        
        
        while non_z < len(nums) and zero_p < len(nums):
            while zero_p < len(nums) and nums[zero_p] != 0:
                zero_p +=1
            
            #z = 1

            while non_z < len(nums) and nums[non_z] == 0:
                non_z+=1
            # non = 0
            

            if zero_p < len(nums) and non_z < len(nums)  and zero_p < non_z:
                nums[zero_p] = nums[non_z]
                nums[non_z] = 0
                zero_p+=1
                non_z+=1
                
            else:
                if non_z < len(nums):
                    non_z+=1
                
                
