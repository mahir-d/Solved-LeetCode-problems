class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        KEYBOARD = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
 
        
        result = []
        s_len = len(digits)
        if s_len == 0:
            return []
        def helper(start, curr_list):
            
            
            if len(curr_list) == s_len:
                result.append("".join(curr_list))
                return
            
            
            for i in KEYBOARD[digits[start]]:
                
                curr_list.append(i)
                helper(start+1, curr_list)
                curr_list.pop()
                
                
            return
        
        helper(0, [])
        return result
        
        