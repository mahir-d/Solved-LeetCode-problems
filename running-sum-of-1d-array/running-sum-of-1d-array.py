class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        list_len: int = len(nums)
        
        for i in range(1, list_len):
            
            nums[i] = nums[i] + nums[i-1]
            
        return nums
