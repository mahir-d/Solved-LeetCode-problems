class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
     
        
        
        int t_len = triangle.size();
        if(t_len == 0){
            return 0;
        }
        if(t_len == 1){
            return triangle.get(0).get(0); 
        }
        
        List<Integer> prev = triangle.get(t_len - 1);
        
        for(int i = t_len-2; i>= 0; i--){
            List<Integer> curr = new ArrayList<Integer>();
            
            for (int j = 0; j < triangle.get(i).size(); j++){
                curr.add(Math.min((prev.get(j) + triangle.get(i).get(j)), (prev.get(j+1) + triangle.get(i).get(j)) ));
            }
            
            prev = curr;
            
        }
        
        return prev.get(0);
        
    }
}