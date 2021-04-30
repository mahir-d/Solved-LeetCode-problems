class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2 != 0:
            return False
        
        target_sum = sum(nums) // 2
        
        my_dict = {}
        
        def dp(idx, target):
            
            if target == 0:
                return True
            if idx == 0 or target < 0:
                return False
            if (idx, target) in my_dict:
                return my_dict[(idx, target)]
            my_dict[(idx, target)] = dp(idx-1, target-nums[idx-1]) or dp(idx-1, target)
            return my_dict[(idx, target)]
        
        return dp(len(nums)-1, target_sum)