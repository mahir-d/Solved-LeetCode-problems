import heapq
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        
        heap = []
        min_n = float('inf')
        
        max_deviation = float('inf')
        
        for n in nums:
            if n%2 != 0:
                heapq.heappush(heap, -n*2)
                min_n = min(min_n, n*2)
            else:
                heapq.heappush(heap, -n)
                min_n = min(min_n, n)
                
        print(min_n)
        curr = heapq.heappop(heap) * -1
        while curr % 2 == 0:
            max_deviation = min(max_deviation,curr - min_n)
            
            min_n = min(curr//2, min_n)
            heapq.heappush(heap, -curr//2)
            
            curr = heapq.heappop(heap) * -1
        
        
        max_deviation = min(max_deviation,curr - min_n)
        return max_deviation