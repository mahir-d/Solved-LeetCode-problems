class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        for i in range(0, len(nums)):
            
​
            val: int = abs(nums[i])
            if nums[val - 1] > 0:
                nums[val - 1] *= -1
            
        print(nums)
        to_rtrn = []   
        for i in range(0, len(nums)):
            if nums[i] > 0:
                to_rtrn.append(i + 1)
                
                
        return to_rtrn
