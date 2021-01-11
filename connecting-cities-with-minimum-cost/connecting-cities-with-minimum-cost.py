class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        
        
        my_list = [i for i in range (0, N)]
        print(my_list)
        
        connections.sort(key = lambda x:x[2])
        
        def find_p(c):
            if c != my_list[c]:
                my_list[c] = find_p(my_list[c])
            return my_list[c]
        
        def union(c1,c2):
            my_list[find_p(c2)] = find_p(c1)
        
        
                
        min_cost = 0
        while connections:
            c1,c2,cost = connections.pop(0)
            
            if find_p(c1-1) != find_p(c2-1):
                min_cost += cost
                union(c1-1,c2-1)
