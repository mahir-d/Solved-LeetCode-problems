class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        
        result = [[inf] * len(matrix[0]) for i in range(len(matrix))]
        
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    result[row][col] = 0
                else:
                    min_dis = result[row][col]
                    #go up
                    if row > 0:
                        min_dis = min(min_dis, 1 + result[row-1][col])
                    #go left
                    if col > 0:
                        min_dis = min(min_dis, 1 + result[row][col-1])
                    result[row][col] = min_dis

        for row in range(len(matrix) - 1,-1,-1):
            for col in range(len(matrix[0])-1,-1,-1):
                if matrix[row][col] == 0:
                    result[row][col] = 0
                else:
                    min_dis = result[row][col]

                    #go down
                    if row < len(matrix)-1:

                        min_dis = min(min_dis,1 + result[row+1][col])

                    #go right
                    if col < len(matrix[0])-1:
                        min_dis = min(min_dis, 1 + result[row][col+1])
                    result[row][col] = min_dis

        return result
        
        
        
    
        
        
        
        
        
        
        