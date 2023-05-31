class UndergroundSystem:

    def __init__(self):
        self.average = defaultdict(list)
        self.check_in = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        
        from_to = (self.check_in[id][0], stationName)
        from_to_time = t- self.check_in[id][1]
        self.average[from_to].append(from_to_time)
        # print(self.average[from_to])
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        # print(self.average)
        len_ = len(self.average[(startStation, endStation)])
        total_ = sum(self.average[(startStation, endStation)])
        return total_/len_    


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)