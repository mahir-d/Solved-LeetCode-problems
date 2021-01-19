class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        counter: Dict[int, int] = Counter(candidates)
        counter = [(c, counter[c]) for c in counter]
        result: List[List[int]] = []
        self.helper(0, target, counter, [], target, result)
        return result
        
    def helper(self, curr,remain: int, counter: List[Tuple[int]], currList: List[int], target: int, result: List[List[int]]):
        
        
        if remain == 0:
            result.append(list(currList))
            return
        elif remain < 0:
            return
        else:
            
            for nextCurr in range(curr, len(counter)):
                value, freq = counter[nextCurr]
                if freq == 0:
                    continue
                else:
                    currList.append(value)
                    counter[nextCurr] = (value, freq-1) 
                    
                    self.helper(nextCurr, remain - value, counter, currList, target, result)
                    
                    counter[nextCurr] = (value, freq) 
                    currList.pop()
                    
        
            
            
            
