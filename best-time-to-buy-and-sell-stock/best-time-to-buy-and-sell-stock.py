​
​
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) == 0:
            return 0
        min_price = prices[0]
        dif = 0
        
        for i in range(1, len(prices)):
            
            prof =  prices[i] - min_price 
            dif = max(prof, dif)
            min_price = min(min_price, prices[i])
            
        
        return dif
