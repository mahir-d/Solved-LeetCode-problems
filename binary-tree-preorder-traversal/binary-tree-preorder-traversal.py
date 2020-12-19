# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
#         if not root:
#             return []
#         to_rtrn = [root.val]
        
#         if root.left:
#             to_rtrn.extend(self.preorderTraversal(root.left))
#         if root.right:
#             to_rtrn.extend(self.preorderTraversal(root.right))
            
#         return to_rtrn
    
        if not root: 
            return []
        
        stack: List[TreeNode] = [root]    
        to_rtrn: List[int] = []
        while stack:
            curr = stack.pop()
​
            to_rtrn.append(curr.val)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
            
​
        return to_rtrn
        
        
