class BrowserHistory:
​
    def __init__(self, homepage: str):
        self.curr: List[str] = [homepage]
        self.forward_stack: List[str] = [] 
​
    def visit(self, url: str) -> None:
        self.curr.append(url)
        self.forward_stack = []
​
    def back(self, steps: int) -> str:
        
        stack_len:int = len(self.curr)
        
        while stack_len > 1 and steps > 0:
            url:str = self.curr[-1]
            self.forward_stack.append(url)
    
            self.curr.pop()
            steps -= 1
            stack_len -= 1
        
        return self.curr[-1]
​
    def forward(self, steps: int) -> str:
        stack_len = len(self.forward_stack)
        
        while stack_len > 0 and steps > 0:
            url: str = self.forward_stack[-1]
            self.curr.append(url)
            self.forward_stack.pop()
            steps -= 1
            stack_len -= 1
        
        return self.curr[-1]
    
​
​
​
# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
