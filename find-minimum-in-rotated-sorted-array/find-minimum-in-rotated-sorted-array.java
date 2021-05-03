class Solution {
    public int findMin(int[] nums) {
       
        int start = 0, end = (nums.length)- 1, idx = -1, last = nums[end];
        
        while(start<=end){
            int mid = (start+end+1)/2;
            
            if(nums[mid] <= last){
                idx = nums[mid];
                end = mid-1;
            }
            else{
                start = mid+1;
            }
        }
        
        return idx;
        
        
        
        
    }
}