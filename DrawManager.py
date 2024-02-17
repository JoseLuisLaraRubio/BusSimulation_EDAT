import pygame
from Button import Button as btn

class DrawManager():
    def __init__(self, BusManager, screen):

        self._busWidth = 150
        self._busHeight = 90

        self._busSprite = pygame.image.load("Assets/BusWhite.png").convert_alpha()

        self._screen = screen
        self._BusManager = BusManager

    def getImage(self, sprite, width, height):
        image = pygame.transform.smoothscale(sprite, (width, height)).convert_alpha()
        return image

    def DrawBGObjects(self):
        #Load Sprites
        roadSprite = self.getImage(pygame.image.load("Assets/Road.png"), 650, 650)
        listSign = self.getImage(pygame.image.load("Assets/ListSign.png"), 130, 75)
        timeSign = self.getImage(pygame.image.load("Assets/TimeSign.png"), 130, 75)

        #Draw Sprites
        self._screen.blit(roadSprite, (self._screen.get_width() / 2 - 325, self._screen.get_height() / 2 - 325))
        self._screen.blit(listSign, (80, 50))
        self._screen.blit(timeSign, (1055, 50))
        

    def GetColoredBus(self, bus, width, height):
        coloredBus =  self.getImage(self._busSprite, width, height)
        colorRect = pygame.Surface(coloredBus.get_size())
        colorRect.fill(bus._color)

        coloredBus.blit(colorRect,(0, 0), special_flags = pygame.BLEND_RGBA_MULT)

        return coloredBus

    def DrawBussesSimulation(self, busses):
        for bus in busses:

            image =  self.GetColoredBus(bus, self._busWidth, self._busHeight)
            
            self._screen.blit(image,
                 bus.getMappedToCircle(self._BusManager._nodeCount, 265,
                 ((self._screen.get_width() - self._busWidth)/ 2, (self._screen.get_height() - self._busHeight)/ 2 )))

    def DrawBussesList(self, busses):
        y = 150
        for bus in busses:
            self._screen.blit(self.GetColoredBus(bus, 700 / len(busses), (700 * 3) / (len(busses) * 5)), (85, y))
            y += (700 * 3) / (len(busses) * 5) + 10


        
