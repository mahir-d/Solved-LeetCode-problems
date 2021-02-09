# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        
        if not root:
            return None
        self.helper(root, 0)
        return root
        
        
        
    def helper(self, root:TreeNode, total: int)-> int:
        
        if not root.right and not root.left:
            root.val += total
            return root.val
        
        if root.right:
            total = self.helper(root.right, total)
            
        root.val += total
        total = root.val
        
        if root.left:
            total = self.helper(root.left, total)
            
        return total