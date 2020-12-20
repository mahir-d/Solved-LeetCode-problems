class Solution:
    def climbStairs(self, n: int) -> int:
        my_dict = {}
        return self.helper(n , my_dict)
        
        
    def helper(self, n, my_dict):
        
        if n <= 1:
            return 1
        
        else: 
            if n in my_dict:
                return my_dict[n]
            else:
                my_dict[n] = self.helper(n - 1, my_dict) + self.helper(n - 2, my_dict)
            return my_dict[n]
            
