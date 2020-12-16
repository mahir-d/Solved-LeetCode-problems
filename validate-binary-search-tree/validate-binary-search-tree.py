# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        return self.helper(None,None,root)
        
        
    def helper(self, lower_limit: int, upper_limit: int, root: TreeNode) -> bool:
        low: bool = True
        upper: bool = True
            
        if lower_limit != None and lower_limit >= root.val:
            return False
        if upper_limit != None and upper_limit <= root.val:
            return False
        
        if root.left:
            low = self.helper(lower_limit, (root.val), root.left)
            
        if root.right:
            upper = self.helper(root.val, upper_limit, root.right)
            
        return low and upper
