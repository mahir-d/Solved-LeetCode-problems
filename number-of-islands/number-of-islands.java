class Solution {
    public int numIslands(char[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int count = 0;
        for (int i = 0; i < m; i++){
            
            for(int j = 0 ; j < n; j++){
                
                if(grid[i][j] == '1'){
                    
                    if (helper(i,j, grid) == true){
                        count++;
                    }
                }
                
            }
        }
        return count;
    }
    
    public boolean helper(int i, int j, char[][] grid){
        int m = grid.length;
        int n = grid[0].length;
        if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] != '1') return false;
        
        grid[i][j] = 'a';
        
        helper(i+1, j, grid);
        helper(i-1, j, grid);
        helper(i,j+1, grid);
        helper(i, j-1, grid);
        
        return true;
        
        
    }
}