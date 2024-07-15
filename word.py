from letter import Letter
from lettersquare import LetterSquare
from random import randint


class Word:
    def __init__(self, word, font):
        self.word_str = word
        self.letters = list()
        self.font = font

    # Break into letters
    def break_down(self, WIDTH, HEIGHT):
        # (64 * len(self.word_str) - 1) + 96 * len(self.word_str)
        letter_idx = 0
        total_square_width = (64 * len(self.word_str) - 1) + 96 * len(self.word_str)
        for letter in self.word_str:
            letter_square = LetterSquare(((WIDTH - total_square_width) // 2 + 96 * letter_idx + 96 // 2 + 64 * letter_idx, HEIGHT // 2))
            print("lQ", letter_square)
            self.letters.append(Letter(letter, letter_square, self.font))
            self.letters[-1].set_letter_square(letter_square)
            print(self.letters[-1].get_letter_square(), "herere")
            letter_idx += 1

    def scatter_letters(self, x_low, x_high, y_low, y_high):
        for letter in self.letters:
            letter.move((randint(x_low, x_high), randint(y_low, y_high)))

    def get_letters(self):
        return self.letters
