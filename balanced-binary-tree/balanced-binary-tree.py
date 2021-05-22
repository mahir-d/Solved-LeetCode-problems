# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        if not root:
            return True
        
    
        
        def dfs(root) -> int:
            
            if not root:
                return -1
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            return 1 + max(left, right)
        
        
        return abs(dfs(root.left) - dfs(root.right)) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)
            