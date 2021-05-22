class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        
        for denom in coins:
            
            for i in range(denom, amount+1):
                
                remain = i - denom
                dp[i] = min (dp[remain] + 1, dp[i])
        
        return dp[amount] if dp[amount] != float('inf') else -1
        