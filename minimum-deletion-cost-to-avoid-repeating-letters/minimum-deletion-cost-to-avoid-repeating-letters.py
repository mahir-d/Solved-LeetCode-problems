class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        
        i:int = 0
        total_cost: int = 0
            
        while i < len(s) - 1:
            
            
            if s[i] == s[i+1]:
                
                total: int = cost[i]
                max_cost: int = cost[i]
                
                while i < len(s)-1 and s[i] == s[i+1]:
                    i+=1
                    total+=cost[i]
                    max_cost = max(max_cost, cost[i])
                
                total -= max_cost
                total_cost += total
            
            i += 1
            
        return total_cost
