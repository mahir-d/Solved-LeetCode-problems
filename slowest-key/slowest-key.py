class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        
        max_duration = 0
        
        my_dict = defaultdict(list)
        my_dict[releaseTimes[0]].append(keysPressed[0])
        
        for t in range(1, len(releaseTimes)):
            
            time = releaseTimes[t]-releaseTimes[t-1]
            my_dict[time].append(keysPressed[t])
        
        
        max_time = max(my_dict)
        # print(my_dict)
        # print(max_time)
        return max(my_dict[max_time])
            