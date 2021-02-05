class Solution:
    def simplifyPath(self, path: str) -> str:
        
        
        stack1 = path.split('/')
        stack2 = []
        print(stack1)
        
        while stack1:
            curr= stack1.pop(0)
            if curr == '.' or curr == '':
                continue
            if curr == '..':
                if stack2:
                    stack2.pop()
            else:
                stack2.append(curr)
            
        
        # print(stack2)
        result = "/"+"/".join(stack2)
        return result
            