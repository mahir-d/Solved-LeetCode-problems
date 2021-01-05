# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        
        return self.helper(root)
    
    def helper(self, root: TreeNode)->int:
        
        if root == None:
            return 0
        
        l = 0
        r = 0
        
        if root.left:
            l += self.helper(root.left)
        if root.right:
            r += self.helper(root.right) 
        
        if l == 0:
            return r + 1
        elif r == 0:
            return l + 1
        else:
            return min(l, r) + 1
            
