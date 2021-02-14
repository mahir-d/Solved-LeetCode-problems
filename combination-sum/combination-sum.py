class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        
        result = []
        
        
        def helper(i, curr_list):
            
            curr_sum = sum(curr_list)
            
            if curr_sum == target:
                result.append(curr_list[:])
                return 
            if curr_sum > target:
                return
            
            for i in range(i, len(candidates)):
                
                curr_list.append(candidates[i])
                helper(i, curr_list)
                curr_list.pop()
                
                
            return
            
            
            
                
                
                
        helper(0, [])
        return result