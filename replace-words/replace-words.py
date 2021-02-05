class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        my_trie = Trie()
        
        for word in dictionary:
            my_trie.insert(word)
        
        word_list = sentence.split()
        
        
        for i in range(len(word_list)):
            
            curr_word = word_list[i]
        
            word_list[i] = my_trie.search_prefix(curr_word, [])
        
        return ' '.join(word_list)
             
        

class Trie:
    
    def __init__(self):
        self.my_dict = {}
        self.flag = False
        
    def insert(self, word):
        curr_root = self
        
        for c in word:
            if c not in curr_root.my_dict:
                curr_root.my_dict[c] = Trie()
            curr_root = curr_root.my_dict[c]
        
        curr_root.flag = True
        
        
    def search_prefix(self, word, curr_list: List[str])->str:
        
        curr_root = self
        
        for c in word:
            
            if c not in curr_root.my_dict:
                return word
            else:
                curr_list.append(c)
                curr_root = curr_root.my_dict[c]
                if curr_root.flag == True:
                    return ''.join(curr_list)
        
        return word
    
#     def __str__(self):
        
#         return str(self.my_dict)
        
        
        
        
        
        
        
        
            