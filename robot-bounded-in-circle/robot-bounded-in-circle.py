class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        
        direc_idx = 0
        direc = [(-1,0), (0,1), (1,0),(0,-1)]
        
        i = 0
        j = 0
        
        for ins in instructions:
            
            if ins == "G":
                i += direc[direc_idx][0]
                j += direc[direc_idx][1]
            
            else:
                if ins == "R":
                    direc_idx = (direc_idx + 1) % 4
                else:
                    direc_idx = (direc_idx + 3) % 4
        
        
        if i == 0 and j == 0 or direc_idx != 0:
            return True
        
        return False
                
        