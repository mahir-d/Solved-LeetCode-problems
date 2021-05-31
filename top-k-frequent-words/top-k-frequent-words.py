class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        my_dict = defaultdict(int)
        
        for word in words:
            my_dict[word]+=1
            
        
        
        heap = []
        
        for key, value in my_dict.items():
            
            heapq.heappush(heap, (-value, key))
            
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        return result
            
        