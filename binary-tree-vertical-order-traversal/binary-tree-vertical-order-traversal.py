# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        
        if not root:
            return None
        my_list: List[Tuple[int,int,int]] = []
        self.helper(0,0,root,my_list)
        my_list.sort(key=lambda x: x[0],reverse=True)
        
        min_col = float('inf')
        max_col = float('-inf')
        my_dict: Dict[int,Tuple[int,int,int]] = defaultdict(list)
        for t in my_list:
            max_col = max(max_col, t[1])
            min_col = min(min_col, t[1])
            my_dict[t[1]].append(t[2])
            
        
        result = []
        for i in range(min_col, max_col+1):
            result.append(my_dict[i])
        # my_dict: Dict[int, List[int]] = defaultdict(list)
        
        
        return result
        
    def helper(self, row:int, col:int,root:TreeNode,my_list: List[Tuple[int,int,int]]):
        
        my_list.append((row,col,root.val))
        
        if root.left:
            self.helper(row-1, col-1,root.left,my_list)
        
        if root.right:
            self.helper(row-1,col+1,root.right,my_list)