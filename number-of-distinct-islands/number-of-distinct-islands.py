class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        col_len = len(grid)
        row_len = len(grid[0])
        no_islands = 0
        my_set = set()
        
        for i in range(col_len):
            
            for j in range(row_len):
                
                if grid[i][j] == 1:
                    no_islands += 1
                    arr = []
                    self.helper(grid, i, j, arr)
                    my_set.add(''.join(arr))
        return len(my_set)
        
        
    def helper(self, grid: List[List[int]], row: int, col: int, arr: List[str]):
        
        grid[row][col] = 0
        
        #go up
        if row > 0 and grid[row-1][col] == 1:
            arr.append('U')
            self.helper(grid, row-1,col,arr)
            arr.append('0')
        #go down
        if row < len(grid) - 1 and grid[row+1][col] == 1:
            arr.append('D')
            self.helper(grid, row+1, col,arr)
            arr.append('0')
        #go left
        if col > 0 and grid[row][col-1] == 1:
            arr.append('L')
            self.helper(grid, row, col-1,arr)
            arr.append('0')
        #go right
        if col < len(grid[0])-1 and grid[row][col+1] == 1:
            arr.append('R')
            self.helper(grid, row, col+1,arr)
            arr.append('0')
        
        return 