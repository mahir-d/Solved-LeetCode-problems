class Solution:
    def numWays(self, n: int, k: int) -> int:
        
        if n == 1:
            return k
        
        dp = [0] * n
        same = [0] * n
        diff = [0] * n
        
        dp[0] = k
        same[0] = k
        dp[1] = k + (k * (k-1))
        diff[1] = k * (k-1)
        
        for i in range(2, n):
            same[i] = diff[i-1]
            diff[i] = dp[i-1] * (k-1)
            dp[i] = same[i] + diff[i]
        
        return dp[-1]
        