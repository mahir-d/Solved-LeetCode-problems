# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.result = TreeNode(0)
        self.dummyHead = self.result
        
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(root):
            if not root:
                return None
        
            if root.left:
                self.increasingBST(root.left)
                root.left = None
        
            self.dummyHead.right = root
            self.dummyHead = self.dummyHead.right         
            if root.right:
                self.increasingBST(root.right)
                
    
        inorder(root)
        return self.result.right
        
        
        