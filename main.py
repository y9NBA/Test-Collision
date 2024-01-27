import pygame as pg
import pygame.display
from  colors import color
from Rectangle import *

pg.init()
width, height = 600, 600
ds = pg.display.set_mode((width, height))
pygame.display.set_caption("Тест столкновений")

fps = pygame.time.Clock()


def main() -> None:

    coord = list()
    move = list()
    limit_coord = list()
    limit_field = {
        "x": [-1, width],
        "y": [-1, height]
    }

    figures = dict({
        "strt": Rectangle(ds, color["red"], [400, 400], [50, 50]),
    })

    while True:

        engine = True

        coord.append([0, 0])
        coord.append([500, 500])

        move.append([1, 1])
        move.append([-1, -1])

        colorMR = color["black"]
        colorMR1 = color["blue"]
        colorST = color["red"]

        while engine:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()

            if (coord[0][0] not in limit_field["x"] and coord[0][1] not in limit_field["y"]) and (coord[0] not in limit_coord):
                coord[0][0] += move[0][0]
                coord[0][1] += move[0][1]
            if (coord[1][0] not in limit_field["x"] and coord[1][1] not in limit_field["y"]) and (coord[1] not in limit_coord):
                coord[1][0] += move[1][0]
                coord[1][1] += move[1][1]

            ds.fill((255, 255, 255))

            figures["strt"].draw()
            movingrect = pygame.draw.rect(ds, colorMR, [coord[0][0], coord[0][1], 300, 300])
            movingrect1 = pygame.draw.rect(ds, colorMR1, [coord[1][0], coord[1][1], 50, 50])

            if movingrect.colliderect(figures["strt"].draw()) is True and (coord[0][0] not in limit_field["x"] and coord[0][1] not in limit_field["y"]):
                coord[0][0] -= move[0][0]
                coord[0][1] -= move[0][1]
                move[0] = [0, 0]
                limit_coord.append(coord[0])
                colorMR = color["green"]
                figures["strt"].get_set_color(color["black"])
                print(coord)
                print(move)

            if movingrect1.colliderect(figures["strt"].draw()) is True and (coord[1][0] not in limit_field["x"] and coord[1][1] not in limit_field["y"]):
                coord[1][0] -= move[1][0]
                coord[1][1] -= move[1][1]
                move[1] = [0, 0]
                limit_coord.append(coord[1])
                colorMR1 = color["green"]
                figures["strt"].get_set_color(color["other"])
                print(coord)
                print(move)

            pygame.display.update()
            fps.tick(60)


if __name__ == '__main__':
    main()
