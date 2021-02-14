# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        
        if not root:
            return None
        
        queue = [(0,0,root)]
        my_dict = defaultdict(list)
        
        while queue:
            
            size_q = len(queue)
            
            
            for _ in range(size_q):
                curr_root = queue.pop(0)
                v_level = curr_root[1]
                h_level  = curr_root[0]
                if curr_root[2].left:
                    queue.append((h_level+1, v_level-1, curr_root[2].left))
                if curr_root[2].right:
                    queue.append((h_level+1, v_level+1, curr_root[2].right))
                
                my_dict[v_level].append((curr_root[0], curr_root[1], curr_root[2].val))
                
   
        sorted_dict = sorted(my_dict)
        
        result = []
        for k in sorted_dict:
            curr_list = []
            my_dict[k].sort()
            result.append(t[2] for t in my_dict[k])
            
        return result
        
        
        
                    
                
                    
                
                
            
        
        
        