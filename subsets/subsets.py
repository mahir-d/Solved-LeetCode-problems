class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        
        result = []
        
        
        def helper(start, curr_list):
            
            result.append(curr_list[:])
            
            
            for i in range(start, len(nums)):
                curr_list.append(nums[i])
                helper(i+1, curr_list)
                curr_list.pop()
                
            return
            
            
        
        
        helper(0, [])
        return result
            