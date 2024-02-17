from Bus import Bus 
class Lector():

    def __init__(self,file):
        self.file = file
        self.buses  = []

    def readFile(self):
        arr = []
        color = []
        for line in self.file:
            arr = line.split(",")
            time = arr[0] 
            laps = arr[1]
            position = arr[2]
            name = arr[3]
            color.append(arr[4])
            color.append(arr[5])
            color.append(arr[6])
            self.buses.append(Bus(time,laps,position,name,color))
        
    def getBuses(self)->list:
        return self.buses