class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        visited = set()
        visiting = set()
        my_dict = defaultdict(list)
        
        for pre in prerequisites:
            my_dict[pre[0]].append(pre[1])
            
        
       
    
        def backtrack(idx):
            print(idx)
            print(visiting)
            if idx in visited:
                return True
            
            for d in my_dict[idx]:
                
                if d in visiting:
                    return False
                visiting.add(d)
                if not backtrack(d):
                    return False
                visiting.remove(d)
            
            visited.add(idx)
            return True
        
        
        for i in range(numCourses):
            visiting.add(i)
            if not backtrack(i):
                return False
            visiting.remove(i)
        return True
            
        
            
            
        