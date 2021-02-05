class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.my_dict = {}
        self.flag = False

    def addWord(self, word: str) -> None:
        curr_root = self
        
        for c in word:
            if c not in curr_root.my_dict:
                curr_root.my_dict[c] = WordDictionary()
            curr_root = curr_root.my_dict[c]
        curr_root.flag = True

    def search(self, word: str) -> bool:
        curr_root = self
        i = 0
        for c in word:
            
            if c == '.':
                print(c)
                print(word[i+1:])
                for alpha in curr_root.my_dict.values():
                    if alpha.search(word[i+1:]):
                        return True
                return False
            else:
                if c not in curr_root.my_dict:
                    return False
                curr_root = curr_root.my_dict[c]
                i+=1
        return curr_root.flag
                
                


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)