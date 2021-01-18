class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> result= new ArrayList<>();
        helper(target, 0, candidates, new LinkedList<Integer>(), result);
        return result;
        
    }
    public void helper(int target, int first, int[] candidates, LinkedList<Integer> currList,List<List<Integer>> result){
        int sum = 0;
        for(int i : currList){
            sum+=i;
        }
        
        if(sum == target){
            result.add(new ArrayList(currList));
            return;
        }
        else if(sum>target){
            return;
        }
        else{
            
            while(first<candidates.length){
                
                currList.add(candidates[first]);
                helper(target, first, candidates, currList,result);
                currList.removeLast();
                first++;
            }
            
            
        }
        
    }
