class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        used = collections.defaultdict(bool)
        def backtrack(curr_list):
            if len(curr_list) == len(nums):
                result.append(curr_list[:])
                return
            
            for i in nums:
                if not used[i]:
                    used[i] = True
                    curr_list.append(i)
                    backtrack(curr_list)
                    curr_list.pop()
                    used[i] = False
            return
        
        backtrack([])
        return result