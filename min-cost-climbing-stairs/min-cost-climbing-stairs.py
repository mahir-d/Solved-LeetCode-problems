class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        
        # if len(cost) == 2:
        #      return min(cost[0], cost[1])
         
        i = 2
        
        while i < len(cost):
            
            cost[i] += min(cost[i-1], cost[i-2])    
            i += 1
        
        return min(cost[i - 1], cost[i-2])
        
                
