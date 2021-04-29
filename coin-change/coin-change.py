class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        
        for denom in coins:
            
            
            for i in range(denom, amount+1):
                remain = i - denom
                dp[i] = min(dp[remain] + 1, dp[i])
                
        
        
        print(dp)
        
        return -1 if dp[-1] == float('inf') else dp[-1]
        