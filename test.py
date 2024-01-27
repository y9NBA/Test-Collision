import pygame

from Rectangle import *

pygame.init()
dis = pygame.display.set_mode((300, 300))
fps = pygame.time.Clock()

rectangle = Rectangle(dis, (0, 0, 0), [150, 150], [50, 50])

x = 0
y = 150
sz = 25

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    if x >= 300:
        x = -50
    else:
        x += 1
    if x % 5 == 0:
        sz += 1
    y -= 1

    dis.fill((255, 255, 255))

    rectangle.draw()

    print(rectangle.get_set_coord([x, y]), rectangle.get_set_size([sz, sz]))

    pygame.display.update()

    fps.tick(60)
