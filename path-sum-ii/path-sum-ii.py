# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        
        if not root:
            return []
        
        result = []
        
        def dfs(root, currList, targetSum):
            
#             if not root or targetSum < 0:
#                 return
            
            if not root.left and not root.right and targetSum == 0:   
                result.append(currList[:])
                return 
            
            if root.left:
                currList.append(root.left.val)
                dfs(root.left, currList, targetSum - root.left.val)
                currList.pop()
            if root.right:
                currList.append(root.right.val)
                dfs(root.right, currList, targetSum -root.right.val)
                currList.pop()
                
            return 
        
        
        dfs(root, [root.val], targetSum - root.val)
        return result
        