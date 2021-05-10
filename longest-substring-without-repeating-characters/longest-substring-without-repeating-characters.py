class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        my_dict = {}
        
        left = 0
        right = 0
        max_len = 0
        while right < len(s):
            
            if s[right] in my_dict and my_dict[s[right]] >= left:
                left = my_dict[s[right]]+1
                my_dict[s[right]] = right
                right+=1
                
            else:
                my_dict[s[right]] = right
                max_len = max(max_len, right-left+1)
                right+=1
                
            
        return max_len