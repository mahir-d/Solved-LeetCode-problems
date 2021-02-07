# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        
        
        if not root:
            return None
        
        return self.helper([root], [])
        
        
    def helper(self, curr_stack, to_rtrn):
        
        while curr_stack:
            to_rtrn.append(curr_stack[-1].val)
            size = len(curr_stack)
            
            while size > 0:
                
                curr = curr_stack.pop(0)
                
                if curr.left:
                    curr_stack.append(curr.left)
                if curr.right:
                    curr_stack.append(curr.right)
                size-=1
                
        return to_rtrn