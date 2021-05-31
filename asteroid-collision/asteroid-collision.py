class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        
        stack = []
        
        
        for new in asteroids:
            
            while stack and new < 0 < stack[-1]:
                
                if abs(new) > abs(stack[-1]):
                    stack.pop()
                    continue
                if abs(new) == abs(stack[-1]):
                    stack.pop()
                break   
            else:
                stack.append(new)
                
        return stack
        