class FirstUnique:

    def __init__(self, nums: List[int]):
        
        # self.my_list = nums[:]
        self.nums = nums
        self.my_counter = Counter(nums)
        self.queue = []
        
        for num in self.nums:
            if self.my_counter[num] == 1:
                self.queue.append(num)

    def showFirstUnique(self) -> int:
        
        while self.queue:
            curr = self.queue[0]
            if self.my_counter[curr] == 1:
                return curr
            else:
                self.queue.pop(0)
        return -1
    
    def add(self, value: int) -> None:
        
        self.nums.append(value)
        
        if value in self.my_counter:
            self.my_counter[value] = False
        
        else:
            self.my_counter[value] = True
            self.queue.append(value)
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)