class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0 
        for i in range(len(s)):
            
            count += self.helper(i,i,s)
            count+= self.helper(i,i+1,s)
        return count
        
    def helper(self, left, right, s):
        count = 0
        while left >= 0 and right < len(s):

            if s[left] == s[right]:
                count+=1
            else:
                break
            left-=1
            right+=1
        return count
            
        