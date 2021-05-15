class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        visited = set()
        def dfs(start, currList):
            
            result.append(currList[:])    
            
            if start >= len(nums):
                return 
            
            
            for i in range(start, len(nums)):
                
                if nums[i] not in visited:
                    currList.append(nums[i])
                    visited.add(nums[i])
                    dfs(i+1, currList)
                    currList.pop()
                    visited.remove(nums[i])
                
        
        dfs(0,[])
        return result
                