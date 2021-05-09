class Solution:
    def numDecodings(self, s: str) -> int:
        
        memo = {}
        def dfs(idx):
            
            if idx in memo:
                return memo[idx]
            
            if idx >= len(s):
                return 1
            
            if s[idx] == "0":
                return 0
            
            if idx == len(s) -1:
                return 1
            
            count = 0
            count = dfs(idx+1)
            
            if 10 <= int(s[idx: idx+2]) <= 26:
                count += dfs(idx+2)
            
            memo[idx] = count
            return count
        
        return dfs(0)
    
    
        
            
            
            
        