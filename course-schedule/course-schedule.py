class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        
        my_dict = defaultdict(list)
        
        
        for i, j in prerequisites:
            
            my_dict[i].append(j)
           
        
        
        def dfs(idx)->bool:
            
            visiting.add(idx)
            
            for i in my_dict[idx]:
                
                if i in visited:
                    continue                
                if i in visiting:
                    return False
                
                
                if not dfs(i):
                    return False
                visited.add(i)
                
            visiting.remove(idx)
            visited.add(idx)
            return True
            
                
        visited = set()
        visiting = set()   
            
           
        for i in range(numCourses):
            if i not in visited:
                if not dfs(i):
                    return False
                
        return True
        