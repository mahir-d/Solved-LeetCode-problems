class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        
        len_s = len(s)
        len_t = len(t)

        if abs(len_s-len_t) > 1:
                return False
        
        if len_s == 0 and len_t == 0:
                return False
            
        if len_s > len_t:
            return self.helper(t, s)
        else:
            return self.helper(s,t)
        
    def helper(self, s, t):
        len_s = len(s)
        len_t = len(t)

        if abs(len_s-len_t) > 1:
            return False
        if len_s == 0 and len_t == 0:
            return False

        for i in range(len_s):

            if s[i] != t[i]:

                if len_s == len_t:
                    return s[i+1:] == t[i+1:]

                else:
                    return s[i:] == t[i+1:]
        return len_s+1 == len_t

        
        
        
        