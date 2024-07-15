import pygame
import random


def get_color():
    return random.randint(125, 255)


class Letter:
    def __init__(self, letter, letter_square, font):
        self.letter = letter
        self.rect = pygame.Rect(0, 0, 96, 96)
        self.color = [get_color() for _ in range(6)]
        self.c = [random.choice(self.color) for _ in range(3)]

        self.letter_square = self.set_letter_square(letter_square)

        self.font = font
        self.font_size = 64
        self.font_fgcolor = (40, 42, 46)
        self.render = self.font.render(self.letter, fgcolor=self.font_fgcolor, size=self.font_size)
        self.font_surface = self.render[0]
        self.font_rect = self.render[1]
        self.update_text_position()

    # Update text position
    def update_text_position(self):
        self.font_rect.center = self.rect.center

    def draw(self, display):
        # Inner layer
        pygame.draw.rect(surface=display, color=self.c, rect=self.rect, width=64, border_radius=25)
        # Outer layer
        pygame.draw.rect(display, (40, 42, 46), self.rect, 5, 25)

        # Draw letter on top of everything
        display.blit(self.font_surface, self.font_rect)

    # Move to a new position
    def move(self, position):
        self.rect.center = position
        self.update_text_position()

    def set_letter_square(self, letter_square):
        self.letter_square = letter_square

    def get_letter_square(self):
        return self.letter_square

    def get_rect(self):
        return self.rect
