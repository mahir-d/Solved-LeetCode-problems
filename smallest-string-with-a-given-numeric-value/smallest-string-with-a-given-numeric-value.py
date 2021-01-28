class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        
        alpha = list('abcdefghijklmnopqrstuvwxyz')
        result = ['' for _ in range(n)]
        max_alpha = 25 
        
        for i in range(n-1, -1, -1):
            
            while k - (max_alpha + 1) < i:
                max_alpha -= 1
            result[i] = alpha[max_alpha]
            k -= max_alpha + 1
            
        return ''.join(result)
            
            