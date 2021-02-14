# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        if not root:
            return True
    
        return self.helper(root, float('-inf'), float('inf'))

    def helper(self, root, min_val, max_val):
        
        if not root:
            return True
        
        if root.val >= max_val or root.val <= min_val:
            return False

        return self.helper(root.left, min_val, min(root.val, max_val)) and self.helper(root.right, max(root.val, min_val), max_val)