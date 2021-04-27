class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1
        
        
        for denom in coins:
            
            for i in range(denom, amount+1):
                
                remain = i - denom
                dp[i] = dp[i] + dp[remain]
                
        return dp[-1]
            
        
        
        