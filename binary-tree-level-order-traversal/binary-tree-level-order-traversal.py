# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if root == None:
            return []
​
        q: List[TreeNode] = [root]
        to_rtrn: List[List[int]] = []
        
        while q:
            
            children_q: List[TreeNode] = []
            curr_list = []
            
            while q:
                curr = q.pop(0)
                curr_list.append(curr.val)
                
                if curr.left:
                    children_q.append(curr.left)
                if curr.right:
                    children_q.append(curr.right)
​
            to_rtrn.append(curr_list)
            q = children_q
            
        return to_rtrn
                
                
                
