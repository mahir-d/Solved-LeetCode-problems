class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []
        KEYBOARD = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'}
        
        result = []
        
        def dfs(idx, currList):
            
            if len(currList) == len(digits):
                result.append("".join(currList[:]))
                return
            curr = KEYBOARD[digits[idx]]
            
            for c in curr:
                currList.append(c)
                dfs(idx+1, currList)
                currList.pop()
        
        dfs(0, [])
        return result