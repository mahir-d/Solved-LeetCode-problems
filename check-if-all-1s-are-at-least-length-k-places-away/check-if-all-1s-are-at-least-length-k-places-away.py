class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        
        
        i = 0 
        
        prev = -1
        
        while i in range(len(nums)):
            
            if nums[i] == 1 and prev != -1:
                
                dif = i - prev - 1
                if dif < k:
                    return False
                prev = i
                i+=1
            elif nums[i] == 1:
                prev = i
                i+=1
            else:
                i+=1
                
        return True
