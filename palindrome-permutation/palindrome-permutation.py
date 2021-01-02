class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        my_set = set()
        
        for ch in s:
            if ch in my_set:
                my_set.remove(ch)
            else:
                my_set.add(ch)
                
        return len(my_set) <= 1
