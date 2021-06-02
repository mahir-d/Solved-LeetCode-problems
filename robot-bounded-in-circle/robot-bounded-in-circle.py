class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        
        
        
        direction = [0,1,2,3]
        direc = [(-1,0), (0,1), (1,0),(0,-1)]
        
        d = 0
        curr_i, curr_j = 0,0
        for ins in instructions:
            
            if ins == "R":
                d = (d + 1) % 4 
            elif ins == "L":
                d = (d + 3) % 4
            else:
                curr_i += direc[d][0]
                curr_j += direc[d][1]
                
        print(d)
        return d != 0 or curr_i == 0 and curr_j == 0