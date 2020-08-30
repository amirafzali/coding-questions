from collections import defaultdict
class UndergroundSystem(object):

    def __init__(self):
        self.checkedin = {}
        self.times = defaultdict(list)

    def checkIn(self, id, stationName, t):
        self.checkedin[id] = {'name': stationName, 'time': t}
        

    def checkOut(self, id, stationName, t):
        checkedin = self.checkedin[id]
        travel = t-checkedin['time']
        key = (checkedin['name'],stationName)
        self.times[(checkedin['name'],stationName)].append(travel)
          
    def getAverageTime(self, startStation, endStation):
        time = self.times[(startStation, endStation)]
        print(time)
        return sum(time)/float(len(time))