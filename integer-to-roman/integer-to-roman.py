class Solution:
    def intToRoman(self, num: int) -> str:
        digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), 
                  (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), 
                  (5, "V"), (4, "IV"), (1, "I")]
        
        result = []
        while num > 0:
            
            for d in digits:
                
                diff = num - d[0]
                if diff < 0:
                    continue
                else:
                    num = diff
                    result.append(d[1])
                    break
                    
        return "".join(result)