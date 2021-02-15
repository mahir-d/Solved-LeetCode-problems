# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        
        
        if not root:
            return 0
        
        queue = [root]
        level = 1
        while queue:
            
            size = len(queue)
            
            curr_list = []
            for i in range(size):
            
                curr_root= queue.pop(0)
                
                if not curr_root.left and not curr_root.right:
                    return level
                else:
                    if curr_root.left:
                        queue.append(curr_root.left)
                    if curr_root.right:
                        queue.append(curr_root.right)
                        
            level+=1
        return level
                
                