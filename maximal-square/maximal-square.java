class Solution {
    public int maximalSquare(char[][] matrix) {
        
        
        int m = matrix.length;
        int n = matrix[0].length;
        
        int[][] grid = new int[m][n];
        int best = 0;
        for(int i = 0; i < m; i++){
            grid[i][0] = Character.getNumericValue(matrix[i][0]);
            best = Math.max(grid[i][0],best);
        }
        for(int i = 0; i < n; i++){
            grid[0][i] = Character.getNumericValue(matrix[0][i]);
            best = Math.max(grid[0][i],best);
        }
        
        
        for(int[] arr:grid){
            for (int i : arr){
                System.out.print(i + " ");
            }
            System.out.println();
        }
        
        for(int i = 1; i < m; i++){
            for(int j = 1; j < n; j++){
                if(matrix[i][j] == '0'){
                    continue;   
                }
                
                grid[i][j] = Math.min(Math.min(grid[i-1][j], grid[i][j-1]), grid[i-1][j-1]) + 1;
                best = Math.max(best, grid[i][j]);
               
            }
        }
        
        return best* best;
        
        
        
    }
}