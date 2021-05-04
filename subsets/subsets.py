class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        
        result = []
        # visited = set()
        
        def dfs(idx, currList):
            
            result.append(currList[:])
            
            if len(currList) == len(nums):
                return 
            
            for i in range(idx,len(nums)):
                # if nums[i] not in visited:  
                    # visited.add(nums[i])
                    currList.append(nums[i])
                    dfs(i+1, currList)
                    currList.pop()
                    # visited.remove(nums[i])
                
        dfs(0, [])
        return result
        
        