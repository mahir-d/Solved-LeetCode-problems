class Solution:
    def minCost(self, cost: List[List[int]]) -> int:
        
        
        
        m = len(cost)
        n = len(cost[0])
        
        for i in range(1,m):
            for j in range(n):
                
                
                if j == 0:
                    cost[i][j] += min(cost[i-1][j+1], cost[i-1][j+2])
                if j == 1:
                    cost[i][j] += min(cost[i-1][j-1], cost[i-1][j+1])
                if j == 2:
                    cost[i][j] += min(cost[i-1][j-2], cost[i-1][j-1])
              
        print(cost)
        return min(cost[-1])
                
        
        