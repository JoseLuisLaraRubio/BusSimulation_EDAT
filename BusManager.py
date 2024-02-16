class BusManager():
    def __init__(self, busses):
        self._busses = busses
        self._nodeCount = 6
        self._simulDuration = 3
        self._timeUnit = 10
        self._circuitLenght = 10

    def UpdateBussesPos(self, dt):
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
                self.NotifyPosChange(current, next)
                temp = current
                self._busses[i] = self._busses[nextIndex]
                self._busses[nextIndex] = temp

    def NotifyPosChange(self, bus1, bus2):
        print("Bus " + bus1._name + " surpassed bus " + bus2._name + " at km: %.2f" % 
              (bus1.getPosInCircuit(self._nodeCount, self._circuitLenght)))
        

    def ReadBussesinfo():
        pass

        