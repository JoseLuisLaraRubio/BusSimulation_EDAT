import math

class BusManager():
    def __init__(self, buses, itime, etime): 
        self._buses = buses
        
        #Horas de duracion de la simulacion
        self._initTime = itime
        self._endTime = etime

        self._simulDuration = self._endTime - self._initTime

        self._nodeCount = 10
        self._circuitLenght = 10

        self._timeUnit = 6
        self._elapsedTime = 0

        self._simulationFinished = False
        self._simulationActive = False

        self.CorrectStartPos()
        self.SetBusSpeed()

    def CorrectStartPos(self):
        actual = self._buses.inicio
        while True:
            bus = actual.dato
            bus._startingPos *= self._circuitLenght / self._nodeCount
            bus._position = bus._startingPos
            bus._currentStop = 0
            if(actual == self._buses.ultimo):
                break 
            actual = actual.siguiente

    def SetBusSpeed(self):
        actual = self._buses.inicio
        while True:
            bus = actual.dato

            distance = (bus._lapCount * self._circuitLenght - bus._startingPos)     
            time = (bus._activeTime * self._timeUnit)    
            bus._speed = distance / time

            print(time)

            #realDistance = 0
            #for i in range(time):
            #    realDistance += bus._speed
                
            
            #print(realDistance)

            if(actual == self._buses.ultimo):
                break 
            actual = actual.siguiente

    def getTimeInHours(self):
        return str(math.floor(self._initTime + self._elapsedTime)) + " : " + str(math.floor((self._elapsedTime - math.floor(self._elapsedTime)) * 60))

    def LimitSimulationTime(self):
        if (self._elapsedTime >= self._simulDuration):
            #self._elapsedTime = self._simulDuration

            self.PauseSimulation()
            self._simulationFinished = True

    def StartSimulation(self):
        if not self._simulationFinished:
            self._simulationActive = True
    
    def PauseSimulation(self):
        self._simulationActive = False

    def RestartSimulation(self):
        if self._simulationFinished:
            
            actual = self._buses.inicio
            while True:
                bus = actual.dato
                bus._isActive = False
                bus._position = bus._startingPos
                bus._currentStop = 0
                if(actual == self._buses.ultimo):
                    break 
                actual = actual.siguiente

            self._elapsedTime = 0
            self._simulationFinished = False
            self._simulationActive = True

    def UpdateBusesPos(self):
        self._elapsedTime += 1 / self._timeUnit

        actual = self._buses.inicio
        while True:
            bus = actual.dato
            if bus._isActive:
                bus._position += bus._speed
                #if(bus._position >= self._circuitLenght):
                #    bus._position -= self._circuitLenght

            if(actual == self._buses.ultimo):
                break 
            actual = actual.siguiente

    def ActivateAndDeactivateBusses(self):
        actual = self._buses.inicio
        while True:
            bus = actual.dato
            bus.CheckSchedule(self._elapsedTime + self._initTime)
            if(actual == self._buses.ultimo):
                break 
            actual = actual.siguiente

    def UpdateList(self):
        actual = self._buses.inicio
        while (actual != self._buses.ultimo):
            if(actual.dato._position > actual.siguiente.dato._position):   
                                
                if(actual == self._buses.inicio):
                    self._buses.inicio = actual.siguiente
                
                temp = actual.siguiente.siguiente
                
                actual.siguiente.siguiente.anterior = actual
                actual.siguiente.siguiente = actual
                actual.siguiente.anterior = actual.anterior
                actual.anterior.siguiente = actual.siguiente
                actual.anterior = actual.siguiente
                actual.siguiente = temp

                if(actual.anterior == self._buses.ultimo):
                    self._buses.ultimo = actual
            else:
                actual = actual.siguiente

    def NotifyPosChange(self, bus1, bus2):
        print("Bus " + bus1._name + " surpassed bus "
               + bus2._name + " at km: %.2f" % bus1._position)

    def PrintResults():
        pass
        
