class Solution {
    public boolean canPartition(int[] nums) {
        
        int triangle_sum = 0; 
        
        for(int i : nums){
            triangle_sum += i;
        }
        
        if(triangle_sum % 2 != 0)return false;
        Map<String, Boolean> map = new HashMap<>();
        return dp(nums.length-1, triangle_sum/2, nums, map);
        
        
    }
    
    public static boolean dp(int idx, int target, int[] nums,Map<String, Boolean> map){
        String key = idx + " " + target;
        if(map.containsKey(key))return map.get(key);
        if(target == 0) return true;
        
        if(idx == 0 || target < 0) return false;
        
        map.put(key, dp(idx-1, target-nums[idx-1], nums,map) || dp(idx-1, target, nums,map));
        return map.get(key);
        
    }
}