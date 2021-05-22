class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        m = len(graph)
        n = len(graph[0])
        result = []
        visited = set()
        
        def dfs(i, currList):
            print(i)
            if i == m - 1:
                
                result.append(currList[:])
                
                return 
            
            
            
            for neigh in graph[i]:
                if neigh not in visited:
                    visited.add(neigh)
                    currList.append(neigh)
                    dfs(neigh, currList)
                    currList.pop()
                    visited.remove(neigh)
            
        
        dfs(0,[0])
        return result
                    
                
            