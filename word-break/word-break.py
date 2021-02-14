class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        my_dict = {}
        
        def helper(i):
            if i in my_dict:
                return my_dict[i]
            if i >= len(s):
                    return True
            for word in wordDict:
                if s[i:].startswith(word):
                    if helper(i + len(word)):
                        my_dict[i] = True
                        return True
            my_dict[i] = False
            return False
            
        
        return helper(0)
        
        