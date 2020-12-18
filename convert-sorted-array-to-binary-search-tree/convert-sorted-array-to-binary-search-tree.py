# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        nums_len = len(nums)
       
        if nums_len == 0:
             return None
    
        else:
            
            mid: int = nums_len//2
              
            # if mid % 2 == 0:
            #     currNode: TreeNode = TreeNode(nums[mid + 1],
            #                                  self.sortedArrayToBST(nums[0:mid]), self.sortedArrayToBST(nums[mid+1:]))
            #     return currNode
            
                    
            
            currNode: TreeNode = TreeNode(nums[mid],
                                         self.sortedArrayToBST(nums[0:mid]), self.sortedArrayToBST(nums[mid+1:]))
            return currNode
            
                
            
                
    
  
