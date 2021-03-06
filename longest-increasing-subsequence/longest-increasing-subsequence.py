class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [1] * len(nums)
        max_l = 1
        for i in range(1, len(nums)):
            
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j]+1, dp[i])
                    max_l = max(max_l, dp[i])   
        return max_l
        