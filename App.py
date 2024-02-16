# Example file showing a circle moving on screen
import pygame
from DrawManager import DrawManager
from Bus import Bus
from BusManager import BusManager

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

#TEST BUS INFO
b1 = Bus(initTime = 0, lapCount = 3, startingPos = 2, name = "A")
b2 = Bus(initTime = 0, lapCount = 5, startingPos = 0, name = "B")
b3 = Bus(initTime = 0, lapCount = 7, startingPos = 6, name = "C")
b4 = Bus(initTime = 0, lapCount = 1, startingPos = 3, name = "D")
b5 = Bus(initTime = 0, lapCount = 4, startingPos = 1, name = "E")
b6 = Bus(initTime = 0, lapCount = 9, startingPos = 4, name = "F")

busses = [b1, b2, b3, b4, b5, b6]

#player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
BM = BusManager(busses = busses)
DM = DrawManager(BusManager = BM, screen = screen)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill([197,244,180])

    #Draw Background
    DM.DrawBGObjects()

    #Update positions
    BM.UpdateBussesPos(dt)
    BM.UpdateList()

    #Draw busses
    DM.DrawBussesSimulation(BM._busses)
    DM.DrawBussesList(BM._busses)

    #Draw Misc
    pygame.draw.line(screen, "Black", [940, 300], [960, 300])

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()