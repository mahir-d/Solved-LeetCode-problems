import heapq

class Solution:

    def connectSticks(self, sticks: List[int]) -> int:
        
        if len(sticks) == 0:
            return 0
        
        heap = []
        
        
        for s in sticks:
            heapq.heappush(heap, s)
        
        cost = 0
        
        while len(heap) > 1:
            f = heapq.heappop(heap)
            s = heapq.heappop(heap)
            curr_sum =  f + s
            cost += curr_sum
            heapq.heappush(heap, curr_sum)
        
            
        return cost
        
        