# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        if len(preorder) == 0:
            return None
        return self.helper(preorder, inorder)
        
    def helper(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        
        curr_root_num = preorder.pop(0)
        
        i = 0
        while i < len(inorder) and inorder[i] != curr_root_num:
            i+=1
            
        
        left_tree = inorder[:i]
        right_tree = inorder[i+1:]
        curr_root = TreeNode(curr_root_num)
        
        if len(left_tree) != 0:
            curr_root.left = self.helper(preorder, left_tree)    
            
        if len(right_tree) != 0:
            curr_root.right = self.helper(preorder, right_tree)
            
