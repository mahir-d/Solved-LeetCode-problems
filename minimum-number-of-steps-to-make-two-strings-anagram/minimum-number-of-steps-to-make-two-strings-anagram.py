class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        
        s_counter: Dict[str, int] = Counter(s)
        t_counter = Counter(t)
        
        
        steps:int = 0
            
        for k in s_counter.keys():
            
            if k in t_counter:
                dif = s_counter[k] - t_counter[k]
                if dif > 0:
                    steps += dif
            else:
                steps += s_counter[k]
            
        return steps
        
