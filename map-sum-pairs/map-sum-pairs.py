class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.my_list = [None] * 26
        self.my_dict = defaultdict(int)
        

    def insert(self, key: str, val: int) -> None:
        
        curr_root = self
        
        for c in key:
            c = ord(c)    
            if curr_root.my_list[c - ord('a')] == None:
                curr_root.my_list[c - ord('a')] = MapSum()
            
            curr_root.my_list[c - ord('a')].my_dict[key] = val
            curr_root = curr_root.my_list[c - ord('a')]
            
            
            
            
            
        

    def sum(self, prefix: str) -> int:
        
        
        curr_root = self
        
        for c in prefix:
            c = ord(c)
            if curr_root.my_list[c - ord('a')] != None:
                curr_root = curr_root.my_list[c - ord('a')]
            else:
                return 0
        total = 0
        for i in curr_root.my_dict.values():
            total+= i
        return total


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)