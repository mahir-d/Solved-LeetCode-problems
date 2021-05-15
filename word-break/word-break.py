class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        
        def dfs(start):
            
            if start >= len(s):
                return True
            
            if start in memo:
                return memo[start]
            
            for i in range(start, len(s)):
                
                if s[start: i+1] not in wordDict:
                    continue
                res = dfs(i+1)
                if res:
                    memo[start] = True
                    return True
            
            memo[start] = False
            return False
        
        return dfs(0)