class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        visited = set()
        visiting = set()
        
        my_dict = defaultdict(list)
        
        for pre in prerequisites:
            
            my_dict[pre[0]].append(pre[1])
        
        
        def dfs(idx):
            
            if idx in visiting:
                return False
            
            visiting.add(idx)
            
            for prereq in my_dict[idx]:
                if prereq in visited:
                    continue
                if not dfs(prereq):
                    return False
            visiting.remove(idx)
            visited.add(idx)
            return True
        
        for i in range(numCourses):
            if i not in visited:
                if not dfs(i):
                    return False
        return True
            
        
        
        
        