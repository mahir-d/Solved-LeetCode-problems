# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "x"
        result: List[str] = []
        
        stack = [root]
        
        while stack:
            
            
            curr_root = stack.pop()
            
            if not curr_root:
                result.append("x")
            else:
                result.append(str(curr_root.val))
                
                stack.append(curr_root.right)
                stack.append(curr_root.left)
    
        return ",".join(result)       
                
                
                        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        s = data.split(",")
        return self.helper(s)
    
    def helper(self, s_list: List[str]):
        
        curr_val = s_list.pop(0)
        
        if curr_val == "x":
            return None
        
        else:
            new_root: "TreeNode" = TreeNode(curr_val)
                
            if s_list:
                new_root.left = self.helper(s_list)
            if s_list:
                new_root.right = self.helper(s_list)
                
            return new_root
            
            
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))