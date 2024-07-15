import pygame


class LetterSquare:
    def __init__(self, rect_center):
        self.rect = pygame.Rect(0, 0, 96, 96)
        self.rect.center = rect_center
        self.border_color = (0, 0, 0)

    def move(self, position):
        self.rect.center = position

    def draw(self, display):
        pygame.draw.rect(display, self.border_color, self.rect, 5, 25)

    def get_rect(self):
        return self.rect
