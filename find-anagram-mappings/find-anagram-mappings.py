class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        
        if len(A) == 1:
            return [1]
            
        my_dict: Dict[int,List[int]] = defaultdict(list)
        l_b = len(B)
        for i in range(l_b):
            
            my_dict[B[i]].append(i)
        
        l_a = len(A)
        
        for j in range(l_a):
            
            A[j] = my_dict[A[j]].pop()
            
        
        return A
        
        
