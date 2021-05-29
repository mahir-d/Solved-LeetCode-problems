class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        
        
        my_dict = defaultdict(list)
        
        for i, j in edges:
            my_dict[i].append(j)
            my_dict[j].append(i)
            
        print(my_dict)
        def dfs(idx):
            
            visited.add(idx)
            
            for i in my_dict[idx]:
                if i not in visited:
                    dfs(i)
                    
                
            
        
        count = 0
        visited = set()
        for i in range(n):
            
            if i not in visited:
                count+=1
                dfs(i)
        
        return count