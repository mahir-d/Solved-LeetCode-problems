class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        
        
        oldColor = image[sr][sc]
        
        def find_neigh(i,j):
            neigh = [(1,0), (-1,0), (0,1), (0,-1)]
            curr_list = []
            
            for row,col in neigh:
                
                if i+row < 0 or i+row > len(image)-1 or j+col<0 or j+col>len(image[0])-1 or image[i+row][j+col] != oldColor:
                    continue
                curr_list.append((i+row, j+col))
            return curr_list
        
        
        queue = [(sr,sc)]
        visited = set((sr,sc))
        while queue:
            
            size = len(queue)
            
            for _ in range(size):
                i,j = queue.pop(0)
                
                image[i][j] = newColor
                
                n_list= find_neigh(i,j)
                
                for n in n_list:
                    if n not in visited:
                        queue.append(n)
                        visited.add(n)
                    
            
        return image
                
                