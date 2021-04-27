class Solution:
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # coins.sort()
        
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0
        for denom in coins:
            
            for i in range(len(dp)):
                
                if denom > i:
                    continue
                remain = i - denom
                
                dp[i] = min(1 + dp[remain], dp[i])
            
        print(dp)
                
        
        return -1 if dp[-1] == float('inf') else dp[-1]