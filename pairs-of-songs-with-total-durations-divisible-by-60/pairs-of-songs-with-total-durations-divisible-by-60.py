class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        
        my_dict = defaultdict(int)
        count = 0
        
        for duration in time:
            
            
            search = duration % 60
            remain = (abs(60 - search)) % 60
            
            if remain in my_dict:
                count += my_dict[remain]
            my_dict[search] += 1    
            
        return count
            
            