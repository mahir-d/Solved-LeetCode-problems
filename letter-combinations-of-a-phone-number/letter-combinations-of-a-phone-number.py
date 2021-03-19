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
            '9': 'wxyz'
        }
        curr_d = list(digits)
        visited = set()
        len_d = len(digits)
        result = []
        def dfs(start, curr_d, curr_list):

            if len(curr_list) == len_d:
                if curr_list:
                    result.append("".join(curr_list))
                return

            for d in range(start, len(curr_d)):
                curr_alpha = KEYBOARD[curr_d[d]]

                for alpha in curr_alpha:
                    curr_list.append(alpha)
                    dfs(d+1, curr_d, curr_list)
                    curr_list.pop()

        dfs(0, curr_d, [])
        return result
                    
                
                
                
                
                
                
                
                
                
            