# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if not root:
            return []
        
        result = []
        queue = [root]
        
        level = 0
        
        while queue:
            
            len_q = len(queue)
            curr_list = []
            for i in range(len_q):
                
                curr_root = queue.pop(0)
                if level % 2 != 0:
                    curr_list.insert(0, curr_root.val)
                else:
                    curr_list.append(curr_root.val)
                
                if curr_root.left:
                    queue.append(curr_root.left)
                if curr_root.right:
                    queue.append(curr_root.right)
            result.append(curr_list)
            level+=1
        return result
                
                    
                    
    
                
                
                