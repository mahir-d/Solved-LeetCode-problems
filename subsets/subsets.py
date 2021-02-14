class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        
        result = []
        
        used = defaultdict(bool)
        
        
        def helper(start, curr_list):
            
            result.append(curr_list[:])
            
            
            for i in range(start, len(nums)):
                
                if not used[i]:
                    used[i] = True
                    curr_list.append(nums[i])
                    helper(i+1, curr_list)
                    curr_list.pop()
                    used[i] = False
                    
            return
        
        helper(0, [])
        return result
            