class Solution {
    public int coinChange(int[] coins, int amount) {
        
        
        int[] dp = new int[amount+1];
        Arrays.fill(dp, Integer.MAX_VALUE - 1);
        dp[0] = 0;
        
        for(int denom : coins){
            for(int i = denom; i < amount+1; i++){
                int remain = i - denom;
                dp[i] = Math.min(dp[remain] + 1, dp[i]);
            }
        }
        
        
        
        
        return dp[amount] != Integer.MAX_VALUE - 1 ? dp[amount] : -1;
        
        
    }
}