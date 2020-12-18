class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        
        
        for i in range(0, len(nums) - 2):
            prev = i
            counter = 1
            for j in range(i + 1, len(nums)):
                
                if nums[i] < nums[j]:
                    if nums[prev] < nums[j]:
                        prev = j
                        counter += 1
                    else:
                        prev = j
                 
                if counter >=3:
                    return True
                
        return False
