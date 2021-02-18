class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        left = 0
        right = 0
        
        my_dict = {}
        max_len = 0
        
        while left <= right and right < len(s):
            
            if s[right] in my_dict and left <= my_dict[s[right]]:
    
                left = my_dict[s[right]] + 1
                my_dict[s[right]] = right
                max_len = max(max_len, right - left + 1)
                right+=1
                
            else:
                my_dict[s[right]] = right
                max_len = max(max_len, right - left + 1)
                right+=1
                
        return max_len
                            
            