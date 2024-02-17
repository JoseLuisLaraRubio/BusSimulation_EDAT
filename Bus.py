import math
import numpy as np

class Bus():
    def __init__(self, initTime, lapCount, startingPos, name,color):
        self._name = name
        self._initTime = initTime
        self._lapCount = lapCount
        self._startingPos = startingPos
        self._position = startingPos
        #self._isActive = isActive

        self._color = color #list(np.random.choice(range(256), size=3))

    def getMappedToCircle(self, nodeCount, multiplier, offset):
        angle = self._position / nodeCount * 2 * math.pi
        x =  math.cos(angle)
        y =  math.sin(angle)
        return x * multiplier + offset[0],  y * multiplier + offset[1]

    def getPosInCircuit(self, nodeCount, circuitLength):
        return (self._position / nodeCount) * circuitLength


    

