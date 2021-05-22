# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        
        result = []
        
        def helper(root):
            
            
            if not root.left and not root.right:
                result.append(root)
                return 
            
            if root.left:
                helper(root.left)
            
            result.append(root)
            
            if root.right:
                helper(root.right)
                
        helper(root)
        idx = -1
        for i in range(len(result)):
            if result[i] == p:
                idx = i
        
          
        return result[idx+1] if idx != -1 and idx < len(result)-1 else None
        
        
        
                
            
            
        