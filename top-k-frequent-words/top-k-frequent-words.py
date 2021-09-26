import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        
        my_dict = defaultdict(int)
        my_heap = []
        
        for word in words:
            
            my_dict[word] += 1
            
        for key,value in my_dict.items():
            
            heapq.heappush(my_heap, (-value,key))
            
        
        words_toRtrn = []
        
        for i in range(k):
            
            words_toRtrn.append(heapq.heappop(my_heap)[1])
            

        return words_toRtrn