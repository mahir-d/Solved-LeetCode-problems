class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        visited = set()
        
        def backtrack(currList):
            
            if len(currList) == len(nums):
                result.append(currList[:])
                return 
            
            for i in range(len(nums)):                
                
                if i not in visited:
                    
                    currList.append(nums[i])
                    visited.add(i)
                    backtrack(currList)
                    visited.remove(i)
                    currList.pop()
        
        backtrack( [])
        return result