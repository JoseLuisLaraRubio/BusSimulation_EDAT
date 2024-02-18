import pygame

class Button():
    def __init__(self, x, y, image, scale, surface):

        width = image.get_width()
        height = image.get_height()

        self._surface = surface
        self._image = pygame.transform.smoothscale(
            image, (int(width * scale), int(height * scale))
        )

        self.rect = self._image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()

        if(self.rect.collidepoint(pos)):
            if(pygame.mouse.get_pressed()[0] == 1 and self.clicked == False):
                self.clicked = True
                action = True

        if(pygame.mouse.get_pressed()[0] == 0):
            self.clicked = False

        self._surface.blit(self._image, (self.rect.x, self.rect.y))
        return action