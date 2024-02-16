import pygame

class DrawManager():
    def __init__(self, BusManager, screen):

        self._busWidth = 150
        self._busHeight = 90

        self._busSprite = pygame.image.load("Assets/BusWhite.png").convert_alpha()

        self._screen = screen
        self._BusManager = BusManager

    def getImage(self, sprite, width, height):
        image = pygame.transform.smoothscale(sprite, (width, height))
        return image

    def DrawBGObjects(self):
        #Load Sprites
        roadSprite = self.getImage(pygame.image.load("Assets/Road.png").convert_alpha(), 650, 650)

        #Draw Sprites
        self._screen.blit(roadSprite, (self._screen.get_width() / 2 - 325, self._screen.get_height() / 2 - 325))
        

    def GetColoredBus(self, bus):

        coloredBus =  self.getImage(self._busSprite, self._busWidth, self._busHeight)
        colorRect = pygame.Surface(coloredBus.get_size())
        colorRect.fill(bus._color)

        coloredBus.blit(colorRect,(0, 0), special_flags = pygame.BLEND_RGBA_MULT)

        return coloredBus

        
        
        


    def DrawBussesSimulation(self, busses):
        for bus in busses:

            image =  self.GetColoredBus(bus)
            
            self._screen.blit(image,
                 bus.getMappedToCircle(self._BusManager._nodeCount, 265,
                 ((self._screen.get_width() - self._busWidth)/ 2, (self._screen.get_height() - self._busHeight)/ 2 )))

    def DrawBussesList(self, busses):
        y = 100
        for bus in busses:
            pygame.draw.circle(self._screen, bus._color,[20, y] , 20)
            y += 50

    def DrawBussesDebug(self, busses):
        offset = 0
        for bus in busses:
            pygame.draw.circle(self._screen, bus._color,[100 + offset, bus._position * 100 + 30], 30)
            offset += 100

