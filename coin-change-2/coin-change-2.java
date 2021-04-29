class Solution {
    public int change(int amount, int[] coins) {
        
        
        int[] dp = new int[amount+1];
        dp[0] = 1;
        
        for (int denom : coins){
            
            for(int i = denom; i < amount + 1; i++){
                int remain = i - denom;
                dp[i] = dp[remain] + dp[i];
            }
        }
        
        
        return dp[amount];
    }
}