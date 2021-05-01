import java.util.Collections;
class Solution {
    public boolean canPartition(int[] nums) {
        
        
        int targetSum = 0;
        Map<String, Boolean> map = new HashMap<>();
        
        for(int i : nums){
            targetSum += i;
        }
        
        if(targetSum % 2 != 0){
            return false;    
        }
        return dfs(nums.length-1, targetSum/2,nums, map);
    }
    
    public static boolean dfs(int idx, int target, int[] nums, Map<String, Boolean> map){
            String k = idx + "," + target;
            if(map.containsKey(k)){
                return map.get(k);
            }
            if(target == 0)return true;
            if(idx == 0 || target < 0) return false;
            
            boolean result = dfs(idx-1, target - nums[idx-1], nums, map) || dfs(idx-1, target, nums, map);
            map.put(k, result);
            return result;
        }
}