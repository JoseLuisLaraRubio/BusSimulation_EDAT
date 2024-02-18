
from Bus import Bus

class FileReader():

    def __init__(self, busInfo, schedule):
        self.busInfo = open(busInfo)
        self.scheduleInfo = open(schedule)
        self.buses = []

        self.ReadBusInfo()
        self.ReadScheduleInfo()

    def ReadBusInfo(self):
        arr = []
        for line in self.busInfo:
            color = []
            arr = line.split(",")
            laps = int(arr[0])
            position = int(arr[1])
            name = str(arr[2])
            
            color.append(int(arr[3]))
            color.append(int(arr[4]))
            color.append(int(arr[5]))
            
            self.buses.append(Bus(laps,position,name,color))
        
    def ReadScheduleInfo(self):
        
        for line in self.scheduleInfo:
            arr = line.split(",")
            self._iTime = self.TimeToInt(arr[0])
            self._eTime = self.TimeToInt(arr[1])
            break
        
        arr = []

        for line in self.scheduleInfo:
            schedule = []
            arr = line.split(",")
            
            for str in arr[1:]:
                if "\n" in str:
                    str = str[:-1]
                schedule.append(str)

            for bus in self.buses:
                if(bus._name == arr[0]):
                    bus.CalculateActiveTime(schedule)

    def getBussesData(self)->list:
        return self.buses, self._iTime, self._eTime

    def TimeToInt(self, time):
        arr = time.split(":")
        hour = arr[0]
        minute = arr[1]
        return int(hour) + int(minute) / 60

