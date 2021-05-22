# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        
        def dfs(root, curr_min, curr_max):
            
            if not root:
                return True
            
            if root.val <= curr_min or root.val >= curr_max:
                return False
            
            return dfs(root.left,curr_min, root.val) and dfs(root.right, root.val, curr_max)
        
        return dfs(root, float('-inf'), float('inf'))