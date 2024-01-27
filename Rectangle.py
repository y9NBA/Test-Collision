import pygame


class Rectangle:
    def __init__(self, display: pygame.Surface, color: tuple[int, int, int],
                 coordinate: list[int | float, int | float], size: list[int | float, int | float]):
        self.display = display
        self.color = color
        self.coordinate = coordinate
        self.size = size

    def draw(self):
        return pygame.draw.rect(self.display, self.color,
                                [self.coordinate[0], self.coordinate[1], self.size[0], self.size[1]])

    def get_set_display(self, display: pygame.Surface = None):
        if display:
            self.display = display
        return self.display

    def get_set_color(self, color: tuple[int, int, int] = None):
        if color:
            self.color = color
        return self.color

    def get_set_coord(self, coordinate: list[int | float, int | float] = None):
        if coordinate:
            self.coordinate = coordinate
        return self.coordinate

    def get_set_size(self, size: list[int | float, int | float] = None):
        if size:
            self.size = size
        return self.size


