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

sky = pygame.draw.rect(screen, (72, 246, 246), ((0, 0), (800, 350/2)))

sea = pygame.draw.rect(screen, (7, 40, 255), ((0, 0 + 350/2), (800, 350/4)))

sand = pygame.draw.rect(screen, (247, 255, 7), ((0, 0 + 350/2 + 350/4), (800, 350/4)))

sun = pygame.draw.circle(screen, (247, 255, 7), (700, 50), 40)

boat = ()

cloud = ()

parasol = ()

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()