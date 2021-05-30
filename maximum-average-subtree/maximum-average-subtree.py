# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def maximumAverageSubtree(self, root: TreeNode) -> float:
        if not root:
            return 0
        
        max_avg = [0]
        def helper(root):

            if not root:
                return (0 , 0)

            curr_sum = root.val
            curr_count = 1

            left_sum, left_count = helper(root.left)
            right_sum, right_count = helper(root.right)

            curr_count = right_count+left_count + 1
            curr_sum = root.val + left_sum + right_sum

            curr_avg = curr_sum/curr_count
            print(max_avg[0])
            max_avg[0] = max(max_avg[0], curr_avg)

            return (curr_sum, curr_count)

        helper(root)
        return max_avg[0]
        

    
    
        
        