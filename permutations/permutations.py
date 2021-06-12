class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        visited = set()
        
        def dfs(currList):
            
            if len(currList) == len(nums):
                result.append(currList[:])
                return 
            
            for i in range(len(nums)):
                
                if i not in visited:    
                    
                    visited.add(i)
                    currList.append(nums[i])
                    dfs(currList)
                    currList.pop()
                    visited.remove(i)
        dfs([])
        return result