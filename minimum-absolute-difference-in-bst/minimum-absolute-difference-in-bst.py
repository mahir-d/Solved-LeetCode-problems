# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        
        if not root:
            return 2147483647
        
        stack: List[TreeNode] = [root]
        arr = []
        while stack:
            
            curr = stack[-1]
            
            if curr.left:
                stack.append(curr.left)
                curr.left = None
            else:
                stack.pop()
                arr.append(curr.val)
                if curr.right:
                    stack.append(curr.right)
                    
        
        
        min_abs = 2147483647
        
        for i in range(0, len(arr) - 1):
            
            min_abs = min(min_abs, arr[i+1] - arr[i])
            
        return min_abs
