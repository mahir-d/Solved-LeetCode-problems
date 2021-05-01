class Solution {
    public int maximalSquare(char[][] matrix) {
        
        
        int m = matrix.length; 
        int n = matrix[0].length;
        
        int[][] grid = new int[m][n];
        int max_s = 0;
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                grid[i][j] = matrix[i][j] - '0';
                max_s = Math.max(grid[i][j], max_s);
            }
        }
        
        
        
        for(int i = 1; i < m; i++){
            for(int j = 1; j < n; j++){
                if(grid[i][j] == 0)continue;
                
                grid[i][j] = Math.min(Math.min(grid[i-1][j], grid[i][j-1]), grid[i-1][j-1]) + 1;
                max_s = Math.max(grid[i][j], max_s);
            }
        }
        
        return max_s * max_s;
        
        
        
    }
}