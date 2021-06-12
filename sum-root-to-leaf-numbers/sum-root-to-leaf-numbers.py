# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        
        if not root:
            return None
        nums = []
        def dfs(currRoot, currList):
            
            if not currRoot.left and not currRoot.right:
                
                nums.append("".join(currList))
                return 
            
            if currRoot.left:
                currList.append(str(currRoot.left.val))
                dfs(currRoot.left, currList)
                currList.pop()
            
            if currRoot.right:
                currList.append(str(currRoot.right.val))
                dfs(currRoot.right, currList)
                currList.pop()
            
            
            
        
        dfs(root, [str(root.val)])
        
        total = 0
        for num in nums:
            total += int(num)
            
        return total
        