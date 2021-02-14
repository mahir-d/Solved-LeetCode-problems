class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        
        result = []
        def helper(curr_list, counter):
            
            if len(curr_list) == len(nums):
                result.append(curr_list[:])
                return 
            
            for i in counter:
                
                if counter[i] > 0:
                    counter[i] -=1
                    curr_list.append(i)
                    helper(curr_list, counter)
                    curr_list.pop()
                    counter[i] += 1
                
                
        helper([], Counter(nums))
        return result