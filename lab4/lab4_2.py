import pygame
from pygame.draw import *
pygame.init()

FPS = 30

# Initializing surface
pygame.display.set_caption("Mike - the best coder")
screen = pygame.display.set_mode((800, 350), pygame.RESIZABLE)

sky = pygame.draw.rect(screen, (72, 246, 246), ((0, 0), (800, 350/2)))

sea = pygame.draw.rect(screen, (7, 40, 255), ((0, 0 + 350/2), (800, 350/4)))

sand = pygame.draw.rect(screen, (247, 255, 7), ((0, 0 + 350/2 + 350/4), (800, 350/4)))

# cloud parameters
cloud_color = (255, 255, 255)
cloud_board_color = (0, 0, 0)
cloud_radius = 15
cloud_board_size = 1
cloud_x = 200
cloud_y = 60
step_y = 5
step_x = 20

cloud = pygame.draw.circle(screen, cloud_color, (cloud_x, cloud_y), cloud_radius), \
        pygame.draw.circle(screen, cloud_board_color, (cloud_x, cloud_y), cloud_radius, cloud_board_size)

cloud2 = pygame.draw.circle(screen, cloud_color, (cloud_x + step_x, 60), cloud_radius), \
        pygame.draw.circle(screen, cloud_board_color, (cloud_x + step_x, 60), cloud_radius, cloud_board_size)

cloud3 = pygame.draw.circle(screen, cloud_color, (240, 60), 15), \
        pygame.draw.circle(screen, cloud_board_color, (240, 60), cloud_radius, cloud_board_size)

cloud4 = pygame.draw.circle(screen, cloud_color, (190, 70), 15), \
        pygame.draw.circle(screen, cloud_board_color, (190, 70), cloud_radius, cloud_board_size)

cloud5 = pygame.draw.circle(screen, cloud_color, (210, 70), 15), \
        pygame.draw.circle(screen, cloud_board_color, (210, 70), cloud_radius, cloud_board_size)

cloud6 = pygame.draw.circle(screen, cloud_color, (230, 70), 15), \
        pygame.draw.circle(screen, cloud_board_color, (230, 70), cloud_radius, cloud_board_size)

cloud7 = pygame.draw.circle(screen, cloud_color, (250, 70), cloud_radius), \
        pygame.draw.circle(screen, cloud_board_color, (250, 70), cloud_radius, cloud_board_size)

# parasol parameters
parasol_color = (255, 128, 0)
parasol_color_lines = (0, 0, 0)
parasol_pillar = pygame.draw.rect(screen, parasol_color, ((150, 150), (10, 150)))
parasol_head = pygame.draw.polygon(screen, parasol_color, [(80, 150), (230, 150), (160, 120), (150, 120)])
parasol_head_line1 = pygame.draw.aaline(screen, parasol_color_lines, (105, 150), (150, 120))
parasol_head_line2 = pygame.draw.aaline(screen, parasol_color_lines, (125, 150), (150, 120))
parasol_head_line3 = pygame.draw.aaline(screen, parasol_color_lines, (140, 150), (150, 120))
parasol_head_line4 = pygame.draw.aaline(screen, parasol_color_lines, (170, 150), (160, 120))
parasol_head_line5 = pygame.draw.aaline(screen, parasol_color_lines, (185, 150), (160, 120))
parasol_head_line6 = pygame.draw.aaline(screen, parasol_color_lines, (205, 150), (160, 120))

# boat parameters
boat_color = (153, 76, 0)
mast_color = (0, 0, 0)
sail_color = (192, 192, 192)
window_color = (255, 255, 255)
window_border_color = (0, 0, 0)

boat_center = pygame.draw.rect(screen, boat_color, ((450, 190), (150, 40)))
boat_front = pygame.draw.polygon(screen, boat_color, [(600, 190), (650, 190), (600, 230)])
boat_rear = pygame.draw.circle(screen, boat_color, (450, 190), 40, draw_bottom_left=True)
boat_mast = pygame.draw.rect(screen, mast_color, ((500, 70), (6, 120)))
boat_sail = pygame.draw.polygon(screen, sail_color, [(506, 70), (550, 130), (520, 130)]), \
            pygame.draw.polygon(screen, sail_color, [(506, 190), (550, 130), (520, 130)])
boat_window = pygame.draw.circle(screen, window_color, (610, 205), 10), \
              pygame.draw.circle(screen, window_border_color, (610, 205), 10, 2)


def draw_sun(surface, x, y, radius):
    """

    :param surface: sun locates only on the sky surface
    :param x, y: coordinates the center position of the sun
    :param radius: radius-size of the sun
    :return:
    """
    pygame.draw.circle(surface, (247, 255, 7), (x, y), radius) # 1 - surface, 2 - color, 3 - position, 4 - radius


def draw_cloud(surface, x, y, size, form):
    """

    :param surface: cloud locates only on the sky surface
    :param x, y: lower left corner of beginning cloud.
    :param size: size of cloud - determinate buy radius of cell.
    :param form: shape of form cloud sells (circle or ellipse)
    :return:
    """
    pass


def draw_parasol(surface, x, y, width, height):
    """

    :param surface: parasol locates only on the sand surface
    :param x, y: lower left corner of beginning parasol pillar
    :param width, height : size of parasol
    :return:
    """
    pass


def draw_ship(surface, x, y, width, height):
    """

    :param surface:
    :param x, y:
    :param width, height:
    :return:
    """
    pass


draw_sun(screen, 300, 100, 25)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
