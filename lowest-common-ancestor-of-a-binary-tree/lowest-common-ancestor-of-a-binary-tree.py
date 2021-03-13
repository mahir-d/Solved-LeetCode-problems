# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def __init__(self):
            self.ans = None
        
        def dfs(root: TreeNode)->TreeNode:
            if not root:
                return False
            
            left = dfs(root.left)
            right = dfs(root.right)
            mid = root == q or root == p
            
            
            if mid+left+right >= 2:
                self.ans = root
            
            return mid or left or right
                
            
                        
            
            
            
        dfs(root)
        return self.ans
        