class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        to_rtrn: List[str] = []
        
        for i in range(1,n + 1):
            
            if i % 15 == 0:
                to_rtrn.append("FizzBuzz")
            elif i % 5 == 0:
                to_rtrn.append("Buzz")
            elif i%3 == 0:
                to_rtrn.append("Fizz")
                
            else:
                to_rtrn.append(str(i))
                
        return to_rtrn
