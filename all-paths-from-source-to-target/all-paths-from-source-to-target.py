class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        to_rtrn: List[List[int]] = []
        self.helper(graph, 0, [0], to_rtrn)
        return to_rtrn
    
    def helper(self, graph: List[List[int]], curr_index: int, curr_list, to_rtrn: List[List[int]])->None:
        target = len(graph) - 1
        new_list: List[int] = curr_list.copy()
            
        if curr_index == target:
            
            to_rtrn.append(new_list.copy())
            new_list.pop()
        else:
            
            for i in graph[curr_index]:
                new_list.append(i)
                self.helper(graph, i, new_list, to_rtrn)
                new_list.pop()
                
            
        
        
