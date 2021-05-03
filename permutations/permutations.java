class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        HashSet<Integer> visited = new HashSet<>();
        
        dfs(new ArrayList<Integer>(), result, nums, visited);
        return result;
    }
    
    public static void dfs(List<Integer> currList, List<List<Integer>> result, int[] nums, HashSet<Integer> visited){
        
        
        if(currList.size() == nums.length){
            result.add(new ArrayList<Integer>(currList));
        }
        
        for(int i = 0; i < nums.length; i++){
            if(!visited.contains(nums[i])){
                visited.add(nums[i]);
                currList.add(nums[i]);
                dfs(currList, result, nums, visited);
                currList.remove(currList.size()-1);
                visited.remove(nums[i]);
            }
        }
    }
}