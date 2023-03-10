import pygame

pygame.init()

FPS = 30

# Initializing surface
pygame.display.set_caption("Mike - the best coder")
screen = pygame.display.set_mode((800, 350), pygame.RESIZABLE)

sky = pygame.draw.rect(screen, (72, 246, 246), ((0, 0), (800, 350/2)))

sea = pygame.draw.rect(screen, (7, 40, 255), ((0, 0 + 350/2), (800, 350/4)))

sand = pygame.draw.rect(screen, (247, 255, 7), ((0, 0 + 350/2 + 350/4), (800, 350/4)))


def draw_sun(x, y, radius):
    """

    :param x: coordinates the center position of the sun
    :param y: coordinates the center position of the sun
    :param radius: radius-size of the sun
    :return:
    """
    pygame.draw.circle(screen, (247, 255, 7), (x, y), radius)  # 1 - surface, 2 - color, 3 - position, 4 - radius


def draw_cloud(x, y, size):
    """

    :param x:
    :param x, y: center of the first lower left cloud's cell.
    :param size: size of cloud - determinate buy radius of cell.
    :return:
    """
    # cloud constant parameters
    cloud_color = (255, 255, 255)

    for i in range(4):  # 4 lowest cells of 1 cloud
        pygame.draw.circle(screen, cloud_color, (x, y), size)
        x += size

    y -= size
    x -= (size * 3.5)

    for i in range(3):  # 3 highest cells of 1 cloud
        pygame.draw.circle(screen, cloud_color, (x, y), size)
        x += size


def draw_parasol(x, y, width, height):
    """

    :param x:
    :param width:
    :param x, y: height left corner of beginning parasol pillar
    :param width, height : size of parasol
    :return:
    """
    # parasol constant parameters
    parasol_color = (255, 128, 0)
    parasol_color_lines = (0, 0, 0)

    pillar_width = width * 0.05
    head_height = height * 0.15

    # parasol_pillar
    pygame.draw.rect(screen, parasol_color, ((x, y), (pillar_width, height)))

    # parasol head
    pygame.draw.polygon(screen, parasol_color, [(x - (width / 2 + pillar_width / 2), y + head_height),
                                                (x + (width / 2 + pillar_width / 2), y + head_height),
                                                (x + pillar_width, y), (x, y)])

    x_left0 = x  # to define x coordinates for lines in head
    y0 = y  # # to define y coordinates for lines in head

    for i in range(3):  # decor lines, 3 - is a quantity of the left side head parasol
        x -= width / 8
        pygame.draw.aaline(screen, parasol_color_lines, (x_left0, y0), (x, y + head_height))

    x_right0 = x_left0 + pillar_width
    x = x_right0

    for i in range(3):  # decor lines, 3 - is a quantity of the right side head parasol
        x += width / 8
        pygame.draw.aaline(screen, parasol_color_lines, (x_right0, y0), (x, y + head_height))


def draw_boat(x, y, width, height):
    """

    :param x:
    :param width:
    :param x, y:
    :param width, height:
    :return:
    """

    # boat constant parameters
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
        # pygame.draw.polygon(screen, sail_color, [(506, 190), (550, 130), (520, 130)])
    boat_window = pygame.draw.circle(screen, window_color, (610, 205), 10), \
        # pygame.draw.circle(screen, window_border_color, (610, 205), 10, 2)

    pass


draw_sun(700, 60, 25)

draw_cloud(100, 80, 20)

draw_parasol(200, 200, 80, 100)

draw_parasol(400, 220, 50, 80)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
