# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        
        
        if not root:
            return None

        my_dict = defaultdict(list)


        def dfs(curr_root, parent):


            if curr_root:

                if parent:
                    my_dict[curr_root.val].append(parent.val)
                if curr_root.left:
                    my_dict[curr_root.val].append(curr_root.left.val)
                if curr_root.right:
                    my_dict[curr_root.val].append(curr_root.right.val)

                dfs(curr_root.left, curr_root)

                dfs(curr_root.right, curr_root)

        dfs(root, None)
        
        ans = []
        stack = [target.val]
        visited = {}
        visited[target.val] = True
        level = 0
        while stack:
            size = len(stack)
            
            for i in range(size):
                
                curr = stack.pop(0)
                
                if level == K:
                    ans.append(curr)
                
                for x in my_dict[curr]:
                    if x in visited:
                        continue
                        
                    visited[x] = True
                    stack.append(x)
                    
            level +=1
        return ans
        
        
        
        
    
                
        
                    
            