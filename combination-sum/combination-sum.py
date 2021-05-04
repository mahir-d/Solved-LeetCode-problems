class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []
        
        
        def dfs(idx, currList, currSum):
            
            if currSum == 0:
                result.append(currList[:])
                return 
            if currSum < 0:
                return
            
            
            for i in range(idx, len(candidates)):
                
                currList.append(candidates[i])
                currSum -= candidates[i]
                dfs(i, currList, currSum)
                currList.pop()
                currSum+= candidates[i]
        
        dfs(0, [], target)
        
        return result
            
                
            