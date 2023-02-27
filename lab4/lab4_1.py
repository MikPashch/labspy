import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 400))

# smile's face
circle(screen, (255, 255, 50), (400, 175), 150)
circle(screen, (0, 0, 0), (400, 175), 150, 2)

# smile's eys
circle(screen, (255, 0, 0), (460, 120), 30)     # left
circle(screen, (0, 0, 0), (460, 120), 14)

circle(screen, (255, 0, 0), (340, 120), 35)     # right
circle(screen, (0, 0, 0), (340, 120), 18)

# mouse
rect(screen, (0, 0, 0), (300, 160, 200, 150))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()