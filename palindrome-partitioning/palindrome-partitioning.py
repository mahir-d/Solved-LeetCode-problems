class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        result = []
        
        def dfs(idx, currList):
            
            if idx >= len(s):
                result.append(currList[:])
                return
            
            for i in range(idx, len(s)):
                
                if not self.validPalindrome(s[idx: i+1]):
                    continue
                currList.append(s[idx: i+1])
                dfs(i+1, currList)
                currList.pop()
        
        dfs(0, [])
        return result
        
        
        
    def validPalindrome(self, s):

        len_s = len(s)

        left = 0
        right = len(s)-1
        mid = (left + right + 1) // 2

        if len_s % 2 == 0:
            left = mid-1
            right = mid
        else:
            left = mid-1
            right = mid + 1

        while left >= 0 and right < len(s):
                if s[left] != s[right]:
                    return False
                left-=1
                right+=1

        return True