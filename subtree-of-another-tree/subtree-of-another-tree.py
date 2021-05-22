# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        
        
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
    
        
        return self.helper(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    
    def helper(self, root, subRoot):
        
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        return root.val == subRoot.val and self.helper(root.left, subRoot.left) and self.helper(root.right, subRoot.right)
        
        
    
        
        
        