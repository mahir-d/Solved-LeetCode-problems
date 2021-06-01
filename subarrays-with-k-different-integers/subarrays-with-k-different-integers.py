class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        
        
        if len(nums) == 0 or k == 0:
            return 0
        
        
        def helper(k):
            
            
            start = 0
            subArray = 0
            my_dict = defaultdict(int)
            
            for end, num in enumerate(nums):
                
                
                if my_dict[num] == 0:
                    k -= 1
                my_dict[num] += 1
                
                while k < 0:
                    my_dict[nums[start]] -= 1
                    if my_dict[nums[start]] == 0:
                        k += 1
                    start += 1
                
                subArray += end - start + 1
            
            return subArray
        
        return helper(k) - helper(k-1)
            
            