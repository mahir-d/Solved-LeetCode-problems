class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        my_set: Set[int] = set()
            
        for i in nums:
            if i in my_set:
                my_set.remove(i)
            else:
                my_set.add(i)
                
        
        for x in my_set:
            return x
        
