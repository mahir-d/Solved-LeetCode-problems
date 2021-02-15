class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        #start 0,0
        
        #8 possible moves
        #row-2 col - 1 move
        
        
        
        queue = [(0,0)]
        visited = set()
        level = 0
        def find_neigh(i,col):
            neigh = [(-2, -1), (-1, -2),(+1,-2), (+2,-1), (-2,+1),(-1,+2), (+1,+2), (+2,+1)]
            curr_list = []
            for row,col in neigh:
                r = row+i
                c = col+j
                curr_list.append((r,c))
            return curr_list
            
            
            
        while queue:
            
            size_n = len(queue)
            
            for _ in range(size_n):
                
                i,j = queue.pop(0)
                
                if i == x and j == y:
                    return level
                
                curr_list = find_neigh(i,j)
                
                for n in curr_list:
                    
                    if n not in visited:
                        visited.add(n)
                        queue.append(n)
                        
            level+=1
            
        return level
                
            