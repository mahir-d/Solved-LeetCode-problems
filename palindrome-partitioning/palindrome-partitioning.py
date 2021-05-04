class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        result = []
        
        def dfs(start, currList):
            
            if start >= len(s):
                result.append(currList[:])
                return
            
            for i in range(start, len(s)):
                curr_s = s[start: i+1]   
                if self.validPalindrome(curr_s):
                    currList.append(curr_s)
                    dfs(i+1, currList)
                    currList.pop()
        dfs(0, [])
        return result
                
    def validPalindrome(self, s: str):

        mid = len(s)//2

        if len(s) % 2 == 0:

            left = mid-1
            right = mid

            while left >= 0 and right < len(s):

                if s[left] != s[right]:
                    return False

                else:
                    left-=1
                    right+=1
            return True
        else:

            left = mid-1
            right = mid+1

            while left >= 0 and right < len(s):

                if s[left] != s[right]:
                    return False

                else:
                    left-=1
                    right+=1
            return True


                
                    
                