class Solution {
    public int lengthOfLIS(int[] nums) {
        
        int[] dp = new int[nums.length];
        Arrays.fill(dp, 1);
        int max_len = 1;
        for(int i = 0; i < nums.length; i++){
            
            for(int j = 0; j < i; j++){
                
                if(nums[j] >= nums[i]) continue;
                
                
                dp[i] = Math.max(dp[j] + 1, dp[i]);
                max_len = Math.max(dp[i],max_len);
            }
        }
        
        return max_len;
        
    }
}