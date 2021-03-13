# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        if root == None:
            return None
        
        
        temp = root.right
        
        if root.left:
            root.right = root.left
            root.left = None
            
            stack = [root.right]
            
            while stack:
                
                curr = stack.pop(0)
                
                if curr.right:
                    stack.append(curr.right)
                else:
                    curr.right = temp
            
        self.flatten(root.right)
            
            
        
                    
                    
        
        
            
        
        
        
        
        