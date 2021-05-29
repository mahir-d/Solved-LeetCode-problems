class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        
        boxTypes.sort(key = lambda x: -x[1])
        idx = 0
        units = 0
        while idx < len(boxTypes) and truckSize > 0:
            
            if boxTypes[idx][0] <= truckSize:
                units+= boxTypes[idx][0] * boxTypes[idx][1]
                truckSize -= boxTypes[idx][0]
                
            else:
                units += truckSize * boxTypes[idx][1]
                truckSize = 0
            idx+=1
        return units
                
                
                
                
        
        