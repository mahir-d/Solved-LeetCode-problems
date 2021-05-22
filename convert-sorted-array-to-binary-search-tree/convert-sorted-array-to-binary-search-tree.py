# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    
        if not nums:
            return None
        
        root = TreeNode()
        
        len_t = len(nums)
        
        mid = len_t // 2
        
        root.val = nums[mid]
        
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        
        return root
        
        
        
            
        