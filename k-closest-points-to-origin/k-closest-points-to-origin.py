import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []
        
        def distance(f:int , s:int)-> int:
            
            return sqrt(pow((0-f), 2) + pow((0-s),2))
        
        for i in range(len(points)):
            f = points[i][0]
            s = points[i][1]
            
            heapq.heappush(heap, (distance(f,s), points[i]))
        
        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])    
            
        return result
                    
            
        
        