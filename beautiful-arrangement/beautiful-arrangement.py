class Solution:
    def countArrangement(self, n: int) -> int:
        
        count: int = 0
        visited = [False for i in range(n+1)]   
        
        def helper(n:int, pos: int, visited: List[int]) -> None:
            nonlocal count
            if pos > n: 
                count += 1
            else:
                for i in range(1, n+1):
                    
                    if not visited[i] and (i % pos == 0 or pos % i == 0):
                        visited[i] = True
                        helper(n,pos + 1, visited)
                        visited[i] = False
        
        helper(n, 1, visited)
        return count
        
