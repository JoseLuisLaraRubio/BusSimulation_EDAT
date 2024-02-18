"""
Arturo Cadena Méndez
Mariana Estefanía González Canul
Tyrone Julián Johnson Dorantes
Mauro Arif Kuh Esquivel
José Luis Lara Rubio
"""

import pygame
from Button import Button as btn

class DrawManager():
    def __init__(self, BusManager, screen):

        self._busWidth = 150
        self._busHeight = 90

        self._busSprite = pygame.image.load("Assets/BusWhite.png").convert_alpha()

        self._screen = screen
        self._BusManager = BusManager

    #get a pygame image on a specific size
    def getImage(self, sprite, width, height):
        image = pygame.transform.smoothscale(sprite, (width, height)).convert_alpha()
        return image

    #Display all the static objects on the screen
    def DrawBGObjects(self):
        #Load Sprites
        roadSprite = self.getImage(pygame.image.load("Assets/Road.png"), 650, 650)
        listSign = self.getImage(pygame.image.load("Assets/ListSign.png"), 130, 75)
        timeSign = self.getImage(pygame.image.load("Assets/TimeSign.png"), 130, 75)

        #Draw Sprites
        self._screen.blit(roadSprite, (self._screen.get_width() / 2 - 325, self._screen.get_height() / 2 - 325))
        self._screen.blit(listSign, (80, 50))
        self._screen.blit(timeSign, (1055, 50))
        
    #Get a bus image of a specific color
    def GetColoredBus(self, bus, width, height):
        coloredBus =  self.getImage(self._busSprite, width, height)
        colorRect = pygame.Surface(coloredBus.get_size())
        colorRect.fill(bus._color)

        coloredBus.blit(colorRect,(0, 0), special_flags = pygame.BLEND_RGBA_MULT)

        return coloredBus

    #Display the busses on the circular road
    def DrawBusesSimulation(self, buses):
        actual = buses.inicio
        while True:
            bus = actual.dato
            image =  self.GetColoredBus(bus, self._busWidth, self._busHeight)
            
            self._screen.blit(image,
                 bus.getMappedToCircle(self._BusManager._circuitLenght, 265,
                 ((self._screen.get_width() - self._busWidth)/ 2, (self._screen.get_height() - self._busHeight)/ 2 )))

            if(actual == buses.ultimo):
                break

            actual = actual.siguiente

    #Display the list of busses on its corresponding order
    def DrawBusesList(self, buses):
        MAX_WIDTH = 130

        y = 150
        actual = buses.inicio
        while True:
            bus = actual.dato
            if(700 / buses.len() < MAX_WIDTH):
                self._screen.blit(self.GetColoredBus(bus, 700 / buses.len(), (700 * 3) / (buses.len() * 5)), (85, y))
                y += (700 * 3) / (buses.len() * 5) + 10
            else:
                self._screen.blit(self.GetColoredBus(bus,MAX_WIDTH, MAX_WIDTH * (3/5)), (85, y))
                y += MAX_WIDTH * (3/5) + 10


            if(actual == buses.ultimo):
                break
            
            actual = actual.siguiente

    #Display the clock qith the current time on it
    def DrawClock(self):
        font = pygame.font.Font('freesansbold.ttf', 32)
        clockTxt = self._BusManager.getTimeInHours()

        timeBox = self.getImage(pygame.image.load("Assets/TimeBox.png"), 160, 60)
        text = font.render(clockTxt, True, "green")

        self._screen.blit(timeBox,  (1040, 150))
        self._screen.blit(text, (1070, 165))
        

        
