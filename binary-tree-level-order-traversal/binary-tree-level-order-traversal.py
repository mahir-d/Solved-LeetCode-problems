# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        
        if not root:
            return None
        
        queue = [root]
        result = []
        
        while queue:
            size_q = len(queue)    
            
            curr_list = []
            while size_q > 0:
                curr_root = queue.pop(0)
                size_q -= 1
                
                curr_list.append(curr_root.val)
                
                if curr_root.left:
                    queue.append(curr_root.left)
                if curr_root.right:
                    queue.append(curr_root.right)
            result.append(curr_list)
        return result