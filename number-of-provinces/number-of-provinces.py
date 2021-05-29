class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        visited = set()
        province = 0
        
        
        def dfs(i):
            visited.add(i)
            for j in range(len(isConnected[i])):
                
                if j == i or j in visited:
                    continue
                if isConnected[i][j] == 1:
                    dfs(j)
                
        
        
        
        
        
        
        for i in range(len(isConnected)):
            
            if i not in visited:
                province += 1
                dfs(i)
    
        return province