import pygame
from pygame.draw import *

# Initializing Pygame
pygame.init()

FPS = 30

# Initializing surface
screen = pygame.display.set_mode((800, 350))

# Initializing RGB Color for screen
color = (210, 210, 210)

# Changing surface color
screen.fill(color)
pygame.display.flip()

# smile's face
circle(screen, (255, 255, 50), (400, 175), 150)
circle(screen, (0, 0, 0), (400, 175), 150, 2)

# smile's eys
circle(screen, (255, 0, 0), (460, 130), 30)     # left
circle(screen, (0, 0, 0), (460, 130), 14)

circle(screen, (255, 0, 0), (340, 130), 35)     # right
circle(screen, (0, 0, 0), (340, 130), 18)

# brows
brow_left = rect(screen, (0, 0, 0), ((460-120/2, 130-30-15), (120, 15)))   # left
brow_right = rect(screen, (0, 0, 0), ((340-120/2, 130-35-15), (120, 15)))   # right

# mouse
rect(screen, (0, 0, 0), (325, 250, 150, 25))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()