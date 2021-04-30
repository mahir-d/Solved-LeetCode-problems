class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        
        dp = [1] * len(nums)
        best = 1
        
        for i in range(len(dp)):
            
            for j in range(0, i):
                
                if nums[j] >= nums[i]:
                    continue
                else:
                    dp[i] = max(dp[j]+1, dp[i])
                    best = max(dp[i], best)
                    
                    
        return best