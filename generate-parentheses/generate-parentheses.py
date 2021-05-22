class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        
        result = []
        
        def backtrack(op, cl, currList):
            
            if len(currList) == n * 2:
                result.append("".join(currList))
                return 
            
            if op < n:
                currList.append("(")
                backtrack(op+1,cl, currList)
                currList.pop()
            if cl < op:
                currList.append(")")
                backtrack(op,cl+1, currList)
                currList.pop()
        backtrack(0,0,[])
        
        return result