class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        
        len_r = len(nums)
        visited = set()
        result = []
        
        def dfs(curr_list):
            
            if len(curr_list) == len_r:
                result.append(curr_list[:])
                return 
            
            for n in nums:
                if n not in visited:
                    visited.add(n)
                    curr_list.append(n)
                    dfs(curr_list)
                    curr_list.pop()
                    visited.remove(n)
        dfs([])
        return result
            