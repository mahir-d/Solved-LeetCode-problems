# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if not root:
            return []
        
        result = []
        queue = [root]
        
        while queue:
        
            len_q = len(queue)
            curr_list = []
            while len_q > 0:
                
                curr_root = queue.pop(0)
                curr_list.append(curr_root.val)
                if curr_root.left:
                    queue.append(curr_root.left)
                if curr_root.right:
                    queue.append(curr_root.right)
                len_q -= 1
            result.append(curr_list)
                             
        return result
                    