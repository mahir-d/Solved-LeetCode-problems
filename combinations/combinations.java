class Solution {
    public List<List<Integer>> combine(int n, int k) {
        
        
        
        ArrayDeque<Integer> queue = new ArrayDeque<>();
        List<List<Integer>>result = new ArrayList<>();
        for(int i = 1; i <= n; i++){
            queue.add(i);
        }
        
        while(!queue.isEmpty()){
            ArrayList<Integer> currList = new ArrayList<>();
            currList.add(queue.poll());
            helper(currList, queue.clone(),result, k);
        }
        
        return result;
        
    }
    
    public void helper(ArrayList<Integer> currList,ArrayDeque<Integer> currQ, List<List<Integer>> result,int n){
        
        if( currList.size() == n){
            result.add(currList);
            return;
        }
        
        while(!currQ.isEmpty()){
            
            int currEle = currQ.poll();
            ArrayList<Integer> newList = new ArrayList<>(currList);
            newList.add(currEle);
            helper(newList, currQ.clone(), result, n);
        }
        
        
        
        
    }
}
