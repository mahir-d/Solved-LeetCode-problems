class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        my_dict = defaultdict(list)
        
        for cell in prerequisites:
            my_dict[cell[0]].append(cell[1])    
            
        
        # to_visit = 0
        # visiting = 1
        # visited = 2
        
        state = [0 for i in range(numCourses)]
        
        def dfs(course)->bool:
            
            if state[course] == 1:
                return False
            if state[course] == 2:
                return True
            state[course] = 1
            
            curr_list = my_dict[course]
            
            for dc in curr_list:
                if not dfs(dc):
                    return False
            
            state[course] = 2
            return True
            
            
            
            
            
            
            
            
            
            
        for i in range(numCourses):    
            if not dfs(i):
                return False
        return True
            
            
            