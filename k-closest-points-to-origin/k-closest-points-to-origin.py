import heapq
class Solution:
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        def distance(i, j):
            return math.sqrt( ((0 - i) ** 2) + ((0 - j) ** 2))
        
        for i in range(len(points)):
            
            heapq.heappush(heap, (distance(points[i][0], points[i][1]), (points[i][0], points[i][1])))
        
        result = []
        for _ in range(k):
            
            result.append(heapq.heappop(heap)[1])
        return result