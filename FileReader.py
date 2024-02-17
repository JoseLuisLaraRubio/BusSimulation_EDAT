from Bus import Bus

class FileReader():

    def __init__(self,file):
        self.file = open(file)
        self.buses  = []

    def readFile(self):
        arr = []
        color = []
        for line in self.file:
            arr = line.split(",")
            time = int(arr[0]) 
            laps = int(arr[1])
            position = int(arr[2])
            name = str(arr[3])
            """
            color.append(arr[4])
            color.append(arr[5])
            color.append(arr[6])
            """
            self.buses.append(Bus(time,laps,position,name))#,color)
        
    def getData(self)->list:
        return self.buses
    