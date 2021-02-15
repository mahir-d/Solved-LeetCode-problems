class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = []
        queue = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j))
                
        
        #rooteen orange
        if queue:


            time = -1        
            while queue:

                size = len(queue)

                for _ in range(size):

                    curr_cell = queue.pop(0)

                    if curr_cell[0] > 0 and grid[curr_cell[0]-1][curr_cell[1]] == 1:
                        grid[curr_cell[0]-1][curr_cell[1]] = 2
                        queue.append((curr_cell[0] - 1, curr_cell[1])) 

                    if curr_cell[0] < len(grid) - 1 and grid[curr_cell[0]+1][curr_cell[1]] == 1:
                        grid[curr_cell[0]+1][curr_cell[1]] = 2
                        queue.append((curr_cell[0] + 1, curr_cell[1])) 

                    if curr_cell[1] > 0 and grid[curr_cell[0]][curr_cell[1]-1] == 1:
                        grid[curr_cell[0]][curr_cell[1]-1] = 2
                        queue.append((curr_cell[0], curr_cell[1]-1))

                    if curr_cell[1] < len(grid[0])-1 and grid[curr_cell[0]][curr_cell[1]+1] == 1:
                        grid[curr_cell[0]][curr_cell[1]+1] = 2
                        queue.append((curr_cell[0], curr_cell[1]+1))
                time += 1

            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        return -1
            return time 
        else:
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        return -1
            return 0
                
        
        