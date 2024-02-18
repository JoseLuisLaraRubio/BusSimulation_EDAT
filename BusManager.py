"""
Arturo Cadena Méndez
Mariana Estefanía González Canul
Tyrone Julián Johnson Dorantes
Mauro Arif Kuh Esquivel
José Luis Lara Rubio
"""
import math
class BusManager():
    def __init__(self, buses, itime, etime): 
        self._buses = buses
        
        #Simulation start and end time
        self._initTime = itime
        self._endTime = etime

        self._simulDuration = self._endTime - self._initTime

        self._nodeCount = 10
        self._circuitLenght = 20

        self._timeUnit = 50
        self._elapsedTime = 0

        self._simulationFinished = False
        self._simulationActive = False

        self._busEvents = ""

        self.CorrectStartPos()
        self.SetBusSpeed()

    #Change the startPos format from a node value to a position on the circuit
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

    #Calculate the bus speed based on the distance 
    #it has to travel and the amount of time it will be active
    def SetBusSpeed(self):
        actual = self._buses.inicio
        while True:
            bus = actual.dato
            distance = (bus._lapCount * self._circuitLenght - bus._startingPos)     
            time = (bus._activeTime * self._timeUnit)    
            bus._speed = distance / time        

            bus._theoreticalUpdates = time

            if(actual == self._buses.ultimo):
                break 
            actual = actual.siguiente

    #Update the active buses position
    def UpdateBusesPos(self):
        self._elapsedTime += 1 / self._timeUnit

        actual = self._buses.inicio
        while True:
            bus = actual.dato
            if bus._isActive:
                if(bus._numberOfUpdates < bus._theoreticalUpdates):
                    bus._position += bus._speed

                    if(bus._position >= self._circuitLenght):
                        bus._position -= self._circuitLenght
                bus._numberOfUpdates += 1

            if(actual == self._buses.ultimo):
                break 
            actual = actual.siguiente

    #Check if the simulation has finished to stop calculaationg buses positions
    def LimitSimulationTime(self):
        if (self._elapsedTime >= self._simulDuration and self._simulationFinished == False):
            self._elapsedTime = self._simulDuration            
            self._simulationFinished = True
            self.PauseSimulation()
            self.PrintResults()

    #Start the simulation
    def StartSimulation(self):
        if not self._simulationFinished:           
            self._simulationActive = True
    
    #Pause the simulation
    def PauseSimulation(self):
        self._simulationActive = False

    #Restart the simulation only after it has been completed at least once
    def RestartSimulation(self):
        if self._simulationFinished:
            actual = self._buses.inicio
            while True:
                bus = actual.dato
                bus._isActive = False
                bus._position = bus._startingPos
                bus._currentStop = 0
                bus._numberOfUpdates = 0
                if(actual == self._buses.ultimo):
                    break 
                actual = actual.siguiente
            self._busEvents = ""
            self._elapsedTime = 0
            self._simulationFinished = False
            self._simulationActive = True

    #make busses check their schedule and activate / deactivate them accordingly
    def ActivateAndDeactivateBusses(self):
        actual = self._buses.inicio
        while True:
            bus = actual.dato
            bus.CheckSchedule(self._elapsedTime + self._initTime)
            if(actual == self._buses.ultimo):
                break 
            actual = actual.siguiente

    #Sort the position of the busses on the list
    def UpdateList(self):
        while True:
            sorted = True
            actual = self._buses.inicio
            while (actual != self._buses.ultimo):
                if(actual.dato._position > actual.siguiente.dato._position):   
                    sorted = False

                    diference = actual.dato._position - actual.siguiente.dato._position

                    if(actual == self._buses.inicio):
                        self._buses.inicio = actual.siguiente
                    
                    temp = actual.siguiente.siguiente
                    
                    actual.siguiente.siguiente.anterior = actual
                    actual.siguiente.siguiente = actual
                    actual.siguiente.anterior = actual.anterior
                    actual.anterior.siguiente = actual.siguiente
                    actual.anterior = actual.siguiente
                    actual.siguiente = temp

                    if(diference <= actual.dato._speed):
                        self.NotifyOvertaking(actual.dato, actual.siguiente.dato)

                    if(actual.anterior == self._buses.ultimo):
                        self._buses.ultimo = actual
                else:
                    actual = actual.siguiente

            if(sorted):
                break

    #Notify if a bus has overtaken another
    def NotifyOvertaking(self, bus1, bus2):
        self._busEvents += self.getTimeInHours() + " .- La unidad " + bus1._name + " revaso a la unidad  " + bus2._name + " en el kilometro " + str(bus1._position)[:5]
        self._busEvents += "\n"

    #Return the game time as a string with the format HH/MM
    def getTimeInHours(self):
        hour = math.floor(self._initTime + self._elapsedTime)
        minute = math.floor((self._elapsedTime - math.floor(self._elapsedTime)) * 60)

        if(hour < 10):
            hourStr = "0" + str(hour)
        else:
            hourStr = str(hour)

        if(minute < 10):
            minuteStr = "0" + str(minute)
        else:
            minuteStr = str(minute)

        return hourStr + " : " + minuteStr

    #Generate the file with the results of the simulation
    def PrintResults(self):
        actual = self._buses.inicio
        f= open("Results.txt","w+")
        while True:
            bus = actual.dato
            
            line = "Unidad " + bus._name + " realizo " + str(bus._lapCount) + " vueltas al circuito, a una velocidad promedio de " + str(bus._speed * bus._theoreticalUpdates)[:5] + " Km/H\n"
            
            f.write(line)

            if(actual == self._buses.ultimo):
                break 
            actual = actual.siguiente

        f.write("\n" + self._busEvents)
        f.close()
        
        
