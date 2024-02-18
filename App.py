# Example file showing a circle moving on screen
import pygame
from Bus import Bus
from Button import Button
from BusManager import BusManager
from DrawManager import DrawManager
from FileReader import FileReader
from ListaDobleCircular import ListaDobleC

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
Reader = FileReader("BusesInfo.csv", "Schedule.csv")
clock = pygame.time.Clock()
running = True
dt = 0

#Returns list of buses
buses = ListaDobleC()
tempBuses = Reader.getBussesData()[0]

iTime = Reader.getBussesData()[1]
eTime = Reader.getBussesData()[2]

#Insert data into buses
for bus in tempBuses:
  buses.inserta_inicio(bus)

BM = BusManager(buses, iTime, eTime)
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

    #Draw buses
    DM.DrawBusesSimulation(BM._buses)
    DM.DrawBusesList(BM._buses)

    #Draw Clock
    DM.DrawClock()

    BM.LimitSimulationTime()
    if(BM._simulationActive):
        #Update positions
        BM.ActivateAndDeactivateBusses()
        BM.UpdateBusesPos()
        BM.UpdateList()

    
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
