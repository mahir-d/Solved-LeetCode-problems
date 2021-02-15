from string import ascii_lowercase

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        
        
        queue = [beginWord]
        
        
        visited = set(wordList)
        level = 1
        while queue:
            size_q = len(queue)
            
            for _ in range(size_q):
                
                curr_word = queue.pop(0)
                
                if curr_word == endWord:
                    return level
                
                for i in range(len(curr_word)):
                    for c in ascii_lowercase:
                        
                        temp = curr_word[:i]+c+curr_word[i+1:]
                        
                        if temp in visited:
                            queue.append(temp)
                            visited.remove(temp)
                            
            level+=1
            
            
        return 0
                        
                        
        