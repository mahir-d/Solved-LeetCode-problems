class Solution:
    
    def __init__(self):
        self.max_len = 0
        self.max_tuple = (0,0)  
    
    def longestPalindrome(self, s: str) -> str:
            
        for i in range(0, len(s)):
            odd = self.longestPalindromeSub(s,i,i)
            even = self.longestPalindromeSub(s,i,i+1)
        
        return s[self.max_tuple[0]:self.max_tuple[1]+1]
            
        
    def longestPalindromeSub(self, s:str, start:int, end:int)->int:
            
            while start >= 0 and end < len(s) and s[start]==s[end]:
                start-=1
                end+=1
            
            if self.max_len < (end-1) - (start+1) + 1:
                self.max_len = (end-1) - (start+1) + 1
                self.max_tuple = (start+1,end-1)
            
    
        
            
