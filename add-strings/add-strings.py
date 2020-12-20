class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        i = len(num1) - 1
        j = len(num2) - 1
        carr: int = 0
        to_rtrn: List[str] = []
        
        while i >= 0 or j >= 0:
            
            
            
            d1 = num1[i] if i >= 0 else 0
            d2 = num2[j] if j >= 0 else 0
            
            sum = int(d1) + int(d2) + carr
            if sum > 9:
                carr = 1
                to_rtrn.append(str(sum - 10))
            else:
                to_rtrn.append(str(sum))
                carr = 0
                
            i -= 1
            j -= 1
            
        if carr == 1:
            to_rtrn.append("1")
            
        
        return "".join(to_rtrn)[len(to_rtrn) - 1: : -1]
                
            
                
​
        
