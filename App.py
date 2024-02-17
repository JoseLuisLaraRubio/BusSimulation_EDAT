# Example file showing a circle moving on screen
import pygame
from Bus import Bus
from Button import Button
from BusManager import BusManager
from DrawManager import DrawManager
from FileReader import FileReader

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
Reader = FileReader("BusesInfo.csv")
Reader.readFile()
clock = pygame.time.Clock()
running = True
dt = 0

#TEST BUS INFO
b1 = Bus(initTime = 0, lapCount = 3, startingPos = 2, name = "A")
b2 = Bus(initTime = 0, lapCount = 5, startingPos = 1, name = "B")
b3 = Bus(initTime = 0, lapCount = 7, startingPos = 3, name = "C")
b4 = Bus(initTime = 0, lapCount = 1, startingPos = 3, name = "D")
b5 = Bus(initTime = 0, lapCount = 4, startingPos = 1, name = "E")
b6 = Bus(initTime = 0, lapCount = 9, startingPos = 4, name = "F")
b7 = Bus(initTime = 0, lapCount = 2, startingPos = 5, name = "G")
b8 = Bus(initTime = 0, lapCount = 8, startingPos = 6, name = "H")
b9 = Bus(initTime = 0, lapCount = 6, startingPos = 3, name = "I")

#Returns list of buses
busses = Reader.getData()

BM = BusManager(busses = busses)
DM = DrawManager(BusManager = BM, screen = screen)

playButtonSprite = pygame.image.load("Assets/PlayButton.png")
pauseButtonSprite = pygame.image.load("Assets/PauseButton.png")
restartButtonSprite = pygame.image.load("Assets/RestartButton.svg")


playButton = Button(1070, 310, playButtonSprite, .3, screen)
pauseButton = Button(1085, 470, pauseButtonSprite, .3, screen)
RestartButton = Button(1005, 430, restartButtonSprite, .3, screen)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Fill the screen with a color to wipe away anything from last frame
    screen.fill([197,244,180])

    #Draw Background
    DM.DrawBGObjects()

    #Buttons logic
    if(playButton.draw()):
        BM.StartSimulation()

    if(pauseButton.draw()):
        BM.PauseSimulation()

    if(RestartButton.draw()):
        BM.RestartSimulation()

    #Draw busses
    DM.DrawBussesSimulation(BM._busses)
    DM.DrawBussesList(BM._busses)

    #Draw Clock
    DM.DrawClock()

    if(BM._simulationActive):
        #Update positions
        BM.UpdateBussesPos(dt)
        BM.UpdateList()

    BM.LimitSimulationTime()
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
