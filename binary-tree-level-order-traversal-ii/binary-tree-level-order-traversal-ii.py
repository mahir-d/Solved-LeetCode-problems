# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        
        if not root:
            return []
        
        to_rtrn: List[List[int]] = []
        
        q: List[TreeNode] = [root]
            
        while q:
            
            children_q = []
            curr_list: List[int] = []
                
            while q:
                curr = q.pop(0)
                
                if curr.left:
                    children_q.append(curr.left)
                if curr.right:
                    children_q.append(curr.right)
                    
                curr_list.append(curr.val)
            
            q = children_q
                
            to_rtrn.insert(0,curr_list) 
            
            
        return to_rtrn
