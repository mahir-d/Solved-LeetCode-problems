class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        visiting = set()
        
        my_dict = defaultdict(list)
        
        for i, j in prerequisites:
            
            my_dict[i].append(j)
        
        order = []
        
        def dfs(idx):
            
            if idx in visiting:
                return 
            
            visiting.add(idx)
            
            for i in my_dict[idx]:
                if i in visiting:
                    return    
                if i not in visited:
                    dfs(i)
                    
            visiting.remove(idx)
            visited.add(idx)
            order.append(idx)
            
            
            
            
        
        visited = set()
        for i in range(numCourses):
            
            if i not in visited:
                dfs(i)
                
                
        return order if len(order) == numCourses else []