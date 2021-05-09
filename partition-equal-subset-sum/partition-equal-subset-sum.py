class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        targetSum = sum(nums)
        
        if targetSum % 2 != 0:
            return False
        memo = {}
        
        def dfs(idx, currSum):
            
            if (idx, currSum) in memo:
                return memo[(idx, currSum)]
            
            if currSum == 0:
                return True
            
            if idx == 0 or currSum < 0:
                return False
            memo[(idx, currSum)] = dfs(idx-1, currSum - nums[idx]) or dfs(idx-1, currSum)
            return memo[(idx, currSum)]
        
        return dfs(len(nums)-1, targetSum //2)
        