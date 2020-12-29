class UndergroundSystem:
​
    def __init__(self):
        self.in_transit: Dict[int, Tuple[str, int]] = {}
        self.transit_time: Dict[Tuple[str,str], Tuple[int, int, int]] = {}     
​
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.in_transit[id] = (stationName, t)
​
    def checkOut(self, id: int, stationName: str, t: int) -> None:        
        dep_station, dep_time = self.in_transit[id] 
        curr_time = t - dep_time
        
        if (dep_station, stationName) in self.transit_time:
            curr_avg, total_time, total_trips = self.transit_time[(dep_station, stationName)]
            total_time += curr_time
            total_trips += 1
            curr_avg = total_time/total_trips
            self.transit_time[(dep_station, stationName)] = (curr_avg, total_time, total_trips)
        else:
            self.transit_time[(dep_station, stationName)] = (curr_time, curr_time, 1)
            
            
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        
        return self.transit_time[startStation, endStation][0]
​
​
# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
