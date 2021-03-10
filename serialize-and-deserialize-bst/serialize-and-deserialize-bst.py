# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        def dfs(root, my_str: List[str]):
            
            if not root:
                my_str.append("x")
                return ",".join(my_str)
            
            my_str.append(str(root.val))
            
            dfs(root.left, my_str)
            dfs(root.right, my_str)

            return ",".join(my_str)
        
        return dfs(root, [])
        
        
        
        
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        my_str = data.split(",")
        print(my_str)
        
        def dfs(my_str: List[str]):
            
            if not my_str or my_str[0] == "x":
                my_str.pop(0)
                return None
            curr_s = my_str.pop(0)
            
            new_root = TreeNode(int(curr_s))
            new_root.left = dfs(my_str)
            new_root.right = dfs(my_str)
            return new_root
                
        return dfs(my_str)
            
            
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans