import pygame
from pygame import freetype
from pygame import mouse

import random
from player import Player
from word import Word


class Game:
    def __init__(self):
        pygame.init()

        self.FPS = 60
        self.clock = pygame.time.Clock()

        self.player = Player()

        self.DISPLAY_W = 1536
        self.DISPLAY_H = 1152
        self.resolution = (self.DISPLAY_W, self.DISPLAY_H)
        self.display = pygame.display.set_mode(self.resolution)
        self.drawables = list()

        self.font = freetype.Font("font.ttf")

        self.word_file = open('words.txt', 'r')
        self.create_word()
        self.set_letters()

        self.mouse_moves = False
        self.grabbed_letter_idx = -1

        self.running = True

    def tick_clock(self):
        self.clock.tick(self.FPS)

    def set_letters(self):
        self.letters = self.word.get_letters()
        self.letter_rects = [letter.get_rect() for letter in self.letters]

    def set_drawables(self, letter_list):
        self.drawables.clear()
        self.drawables += letter_list
        self.drawables += [letter.get_letter_square() for letter in letter_list]
        print(self.drawables)

    def draw_sprites(self):
        self.display.fill((255, 255, 255))  # background placeholder
        for drawable in self.drawables:
            drawable.draw(self.display)

        pygame.display.update()

    def stop(self):
        self.running = False

    def create_word(self):
        word_str = random.choice(self.word_file.readlines()).strip().upper()
        word = Word(word_str, self.font)
        word.break_down(self.DISPLAY_W, self.DISPLAY_H)
        word.scatter_letters(0, self.DISPLAY_W, 0, self.DISPLAY_H)

        self.word = word
        self.set_letters()

    def mouse_control(self):
        mouse_pos = mouse.get_pos()
        lmb_pressed, _, _ = mouse.get_pressed()

        mouse_rect = pygame.Rect(mouse_pos[0], mouse_pos[1], 1, 1)
        hovered_letter_idx = mouse_rect.collidelist(self.letter_rects)

        if lmb_pressed and hovered_letter_idx != -1 and self.grabbed_letter_idx == -1:
            self.grabbed_letter_idx = hovered_letter_idx
        elif not lmb_pressed:
            self.grabbed_letter_idx = -1

        if self.grabbed_letter_idx != -1:
            self.letters[self.grabbed_letter_idx].move(mouse_pos)

    def run_game(self):
        self.set_drawables(self.letters)  # TODO move it
        print(self.word.word_str)
        while self.running:
            self.tick_clock()

            self.draw_sprites()

            self.mouse_control()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    freetype.quit()
                    pygame.quit()
                    self.stop()


if __name__ == '__main__':
    game = Game()
    game.run_game()
    game.word_file.close()
