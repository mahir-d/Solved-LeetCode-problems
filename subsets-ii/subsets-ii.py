class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        
        result = []
        nums.sort()
        
        def helper(curr_list, nums):
            result.append(curr_list[:])
            
            
            for i in range(len(nums)):
                
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                    
                curr_list.append(nums[i])
                helper(curr_list, nums[i+1:])
                curr_list.pop()
                
            return
            
            
            
            
        helper([], nums)
        return result