class Node:
    def __init__(self):
        self.key = 0
        self.val = 0
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.size = 0
        self.max_size = capacity
        self.my_dict = {}
        
    def get(self, key: int) -> int:
        # print(key)
        # print(self.my_dict)
        if key in self.my_dict:
            self.move_to_head(key)
            # print(self.my_dict[key].val)
            return self.my_dict[key].val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        
        if key in self.my_dict:
            self.my_dict[key].val = value
            self.move_to_head(key)
        else:
            self.add_node(key, value)
        
    
    
    def add_node(self, key, value):
        
        temp = self.head.next
        curr = Node()
        curr.key, curr.val = key,value
        self.my_dict[key] = curr
        self.head.next = curr
        curr.prev = self.head
        curr.next = temp
        temp.prev = curr
        
        self.size+=1
        
        if self.size > self.max_size:
            self.pop_tail()
    def remove_node(self,curr):
        
        # curr = self.my_dict[key]
        
        temp = curr.next
        curr.prev.next = temp
        temp.prev = curr.prev
    
    def pop_tail(self):
        curr = self.tail.prev
        del self.my_dict[curr.key]
        temp = curr.prev
        temp.next = self.tail
        self.tail.prev = temp
        self.size-=1
    
    def move_to_head(self,key):
        curr = self.my_dict[key]
        self.remove_node(curr)
        
        temp = self.head.next 
        self.head.next = curr
        curr.prev = self.head
        curr.next = temp
        temp.prev = curr
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)