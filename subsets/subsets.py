class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        visited = set()
        
        def backtrack(start, currList):
            
            result.append(currList[:])
            
            if len(currList) == len(nums):
                return 
            
            
            for i in range(start, len(nums)):
                
                if i not in visited:
                    
                    visited.add(i)
                    currList.append(nums[i])
                    backtrack(i+1, currList)
                    currList.pop()
                    visited.remove(i)
        backtrack(0, [])
        return result
            