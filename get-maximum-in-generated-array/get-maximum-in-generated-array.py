class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        nums = [0 for i in range(n+1)]
        nums[1] = 1
        max_len = 1
        i: int = 1
            
        while 2 * i <= n:
            
            nums[2 * i] = nums[i]
            max_len = max(max_len, nums[i])
            
            if 2*i+1 <= n:
                nums[2*i+1] = nums[i] + nums[i+1]
                max_len = max(max_len, nums[i] + nums[i+1])
            i+=1
            
        print(nums)
        return max_len
