class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        
        
        my_dict = Counter()
        my_dict[0] = 1
        currSum = 0
        count = 0

        for i in range(len(nums)):
            
            currSum += nums[i]
            
            diff = currSum - k
            
            if diff in my_dict:
                count+= my_dict[diff]
            
            my_dict[currSum] += 1
            
        return count