class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        m = len(image)
        n = len(image[0])
        oldColor = image[sr][sc]
        visited = set()
        
        def dfs(i, j):
            
            if i < 0 or i >= m or j < 0 or j >= n or image[i][j] != oldColor or (i,j) in visited:
                return 
            
            image[i][j] = newColor
            visited.add((i,j))
            
            dfs(i, j+1)
            dfs(i, j-1)
            dfs(i+1, j)
            dfs(i-1, j)
            
        dfs(sr, sc)
        return image