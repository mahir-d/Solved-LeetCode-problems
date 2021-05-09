class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        if not text1 and not text2:
            return False
        if not text1 or not text2:
            return False
        
        
        dp = [[0] * (len(text2)+1) for _ in range(len(text1)+1)]
        
        for i in range(len(dp)-2, -1,-1):
            
            for j in range(len(dp[0])-2, -1,-1):
                
                
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
                    
        return dp[0][0]
        
        