# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        max_path, max_depth = self.helper(root)
        return max(max_path, max_depth)
        
        
    def helper(self, root: TreeNode) -> Tuple[int,int]:
        
        
        if root.left == None and root.right == None:
            return (0,0)
        
        left_path, left_depth = 0, 0
        right_path, right_depth = 0,0
        
        if root.left:
            left_path, left_depth = self.helper(root.left)
            left_depth += 1
        if root.right:
            right_path, right_depth =self.helper(root.right)
            right_depth += 1
        
        return (max(max(left_path, right_path) , left_depth + right_depth ), max(left_depth, right_depth))
        
        
        
