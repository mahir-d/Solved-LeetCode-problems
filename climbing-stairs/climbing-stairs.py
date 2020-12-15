class Solution:
    def climbStairs(self, n: int) -> int:
​
        dp = [1, 1]
​
        return self.helper(n, dp)
​
    def helper(self, n, dp) -> int:
​
        if n <= 1:
            return 1
        else:
            if len(dp) > n:
                return dp[n]
            else:
                dp.append(self.helper(n-1, dp) + self.helper(n-2, dp))
                return dp[n]
        
