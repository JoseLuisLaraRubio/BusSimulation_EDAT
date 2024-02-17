import math
from ListaDobleCircular import ListaDobleC

class BusManager():
    def __init__(self, busses):    
        self._busses = busses
        
        #Horas de duracion de la simulacion
        self._initTime = 9
        self._endTime = 12

        self._nodeCount = 6
        self._simulDuration = self._endTime - self._initTime
        self._timeUnit = 1
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

    def RestartSimulation(self):
        if self._simulationFinished:
            self._simulationFinished = False
            self._elapsedTime = 0
            
        actual = self._busses.inicio
        while True:
            bus = actual.dato
            bus._position = bus._startingPos
            if(actual == self._busses.ultimo):
                break 
            actual = actual.siguiente

        self._simulationActive = True

    def SaveInitialPositions(self)->list:
        for bus in self._busses:
            self._bussesInitialPosition.append(bus._position)

    def UpdateBussesPos(self, dt):
        self._elapsedTime += dt / self._timeUnit

        actual = self._busses.inicio
        while True:
            bus = actual.dato
            #if bus._isActive:
            busSpeed =  ((bus._lapCount * self._nodeCount - bus._startingPos) / ((self._simulDuration * self._timeUnit)-(bus._initTime*self._timeUnit))  * dt)
            
            bus._position += busSpeed
            if(bus._position >= self._nodeCount):
                bus._position -= self._nodeCount

            if(actual == self._busses.ultimo):
                break 
            actual = actual.siguiente

    
    def UpdateList(self):
        actual = self._busses.inicio
        while (actual != self._busses.ultimo):
            if(actual.dato._position > actual.siguiente.dato._position):   
                if(actual == self._busses.inicio):
                    self._busses.inicio = actual.siguiente
                
                temp = actual.siguiente.siguiente
                
                actual.siguiente.siguiente.anterior = actual
                actual.siguiente.siguiente = actual
                actual.siguiente.anterior = actual.anterior
                actual.anterior.siguiente = actual.siguiente
                actual.anterior = actual.siguiente
                actual.siguiente = temp

                if(actual.anterior == self._busses.ultimo):
                    self._busses.ultimo = actual
            else:
                actual = actual.siguiente

    def NotifyPosChange(self, bus1, bus2):
        print("Bus " + bus1._name + " surpassed bus " + bus2._name + " at km: %.2f" % 
              (bus1.getPosInCircuit(self._nodeCount, self._circuitLenght)))
        

    def ReadBussesinfo():
        pass

    def PrintResults():
        pass
        
