import math

class BusManager():
    def __init__(self, busses):
        
        self._initTime = 9
        self._endTime = 12


        self._busses = busses
        self._nodeCount = 6
        self._simulDuration = self._endTime - self._initTime
        self._timeUnit = 10
        self._circuitLenght = 10
        self._elapsedTime = 0

        self._simulationFinished = False

        self._simulationActive = False

    def getTimeInHours(self):
        return str(math.floor(self._initTime + self._elapsedTime)) + " : " + str(math.floor((self._elapsedTime - math.floor(self._elapsedTime)) * 60))

    def LimitSimulationTime(self):
        if (self._elapsedTime >= self._simulDuration):
            self._elapsedTime = self._simulDuration
            self.PauseSimulation()
            self._simulationFinished = True

    def StartSimulation(self):
        if not self._simulationFinished:
            self._simulationActive = True
    
    def PauseSimulation(self):
        self._simulationActive = False

    def UpdateBussesPos(self, dt):
        self._elapsedTime += dt / self._timeUnit

        for bus in self._busses:
            #if bus._isActive:
            busSpeed =  ((bus._lapCount * self._nodeCount - bus._startingPos) / 
                         (self._simulDuration * self._timeUnit))  * dt
            
            bus._position += busSpeed
            if(bus._position >= self._nodeCount):
                bus._position -= self._nodeCount
    
    def UpdateList(self):
        for i in range(len(self._busses) - 1):
            
            nextIndex = i + 1
            if i + 1 == len(self._busses):
                nextIndex = 0

            current = self._busses[i]
            next = self._busses[nextIndex]

            if(current._position > next._position):
                #self.NotifyPosChange(current, next)
                temp = current
                self._busses[i] = self._busses[nextIndex]
                self._busses[nextIndex] = temp

    def NotifyPosChange(self, bus1, bus2):
        print("Bus " + bus1._name + " surpassed bus " + bus2._name + " at km: %.2f" % 
              (bus1.getPosInCircuit(self._nodeCount, self._circuitLenght)))
        

    def ReadBussesinfo():
        pass

    def PrintResults():
        pass
        