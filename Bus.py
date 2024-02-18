"""
Arturo Cadena Méndez
Mariana Estefanía González Canul
Tyrone Julián Johnson Dorantes
Mauro Arif Kuh Esquivel
José Luis Lara Rubio
"""

import math
import numpy as np

class Bus():
    def __init__(self, lapCount, startingPos, name, color):        
        self._name = name

        self._isActive = False

        self._lapCount = lapCount
        self._startingPos = startingPos
        self._position = startingPos
        self._color = color

        self._speed = 0
        self._currentStop = 0

        self._numberOfUpdates = 0
        self._theoreticalUpdates = 0

    #Check if the bus has to be activated/deactivated according to schedule
    def CheckSchedule(self, elapsedTime):
        if(self._currentStop < len(self._numSchedule)
           and elapsedTime >= self._numSchedule[self._currentStop]):
        
            self._currentStop += 1
            if(self._isActive):
                self._isActive = False
            else:
                self._isActive = True

    #get the possition mapped to a circle to display on screen
    def getMappedToCircle(self, circuitLenght, multiplier, offset):
        angle = self._position / circuitLenght * 2 * math.pi
        x =  math.cos(angle)
        y =  math.sin(angle)
        return x * multiplier + offset[0],  y * multiplier + offset[1]

    #calculate the time the bus will be active during the simulation
    def CalculateActiveTime(self, schedule):
        self._activeTime = 0
        self._schedule = schedule

        self._numSchedule = []

        for time in schedule:
            self._numSchedule.append(self.TimeToInt(time))

        totalTime = 0
        i = 0
        for time in self._numSchedule:  
            if(i % 2):
                totalTime += time
            else:
                totalTime -= time
            i += 1
        self._activeTime = totalTime
    
    #Change the time from the format HH:MM into a integer
    def TimeToInt(self, time):
        arr = time.split(":")
        hour = int(arr[0])
        minute = int(arr[1])
        return hour + minute / 60
        
