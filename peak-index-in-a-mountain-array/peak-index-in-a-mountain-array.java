class Solution {
    public int peakIndexInMountainArray(int[] arr) {
        
        int start = 0, end = arr.length-1, idx = -1;
        
        
        while(start <= end){
            int mid = (start + end + 1)/2;
            
            if(arr[mid] > arr[mid+1]){
                idx = mid;
                end = mid - 1;
            }
            else{
                start = mid+1;
            }
        }
        
        return idx;
            
        
        
    }
}