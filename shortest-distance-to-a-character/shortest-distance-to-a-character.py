class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        
        s_len = len(s)
        answer: List[int] = [inf] * s_len
        last_idx = -1
        
        i = 0
        
        while i < s_len:
            if s[i] == c:
                last_idx = i
            
            if last_idx != -1 and abs(i - last_idx) < answer[i]:
                answer[i] = abs(i - last_idx)
            
            i+=1
            
        
        i = s_len - 1
        
        while i >= 0:
            if s[i] == c:
                last_idx = i
            
            if last_idx != -1 and abs(i - last_idx) < answer[i]:
                answer[i] = abs(i - last_idx)
            
            i-=1
            
        return answer