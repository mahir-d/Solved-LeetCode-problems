#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
​
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        
            curr_stack: List[NestedInteger] = [nestedList]
            k = 1
            total = 0
            
            while curr_stack: 
                new_stack = []
                
                while curr_stack:
                        
                    curr_list = curr_stack.pop(0)
                    
                    i = 0
                    l = len(curr_list)
                    for i in range(l):
                        
                        if curr_list[i].isInteger():
                            total += curr_list[i].getInteger() * k
                        else:
                            new_stack.append(curr_list[i].getList())
                
                curr_stack = new_stack
                k += 1
            return total
        
        
        
        
        
        
        
        
