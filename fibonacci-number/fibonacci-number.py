class Solution:
    def fib(self, n: int) -> int:
        
        my_dict: Dict[int, int] = {} 
        
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in my_dict:
            return my_dict[n]
        
        res = self.fib(n - 1) + self.fib(n-2)
        my_dict[n] = res
        
        return res