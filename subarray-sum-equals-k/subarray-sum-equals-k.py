class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        
        my_dict = defaultdict(int)
        my_dict[0] = 1
        currsum = 0
        count = 0
        
        for i in range(len(nums)):
            currsum += nums[i]
            diff = currsum - k
            
            if diff in my_dict:
                count += my_dict[diff]
            
            my_dict[currsum] += 1
        
        return count
    
    
    
    
    
    
    
            
            