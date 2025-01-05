import pygame
import sys
from random import choice

pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Word Guess")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

word_list = ["PYTHON", "JAVA", "KOTLIN", "SWIFT", "JAVASCRIPT"]

font = pygame.font.Font(None, 36)

def draw_text(text, x, y, color=BLACK):
    rendered_text = font.render(text, True, color)
    screen.blit(rendered_text, (x, y))

def get_rounds():
    input_text = ""
    while True:
        screen.fill(WHITE)
        draw_text("Enter number of rounds:", 50, 100)
        draw_text(input_text, 50, 150, RED)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.unicode.isdigit():
                    input_text += event.unicode
                elif event.key == pygame.K_BACKSPACE and input_text:
                    input_text = input_text[:-1]
                elif event.key == pygame.K_RETURN and input_text.isdigit():
                    return int(input_text)

def play_round(secret_word):
    guessed_letters = []
    wrong_guesses = 0
    max_wrong_guesses = 6

    while True:
        screen.fill(WHITE)
        display_word = " ".join([letter if letter in guessed_letters else "_" for letter in secret_word])
        draw_text(display_word, 50, 100)
        draw_text(f"Wrong guesses: {wrong_guesses}/{max_wrong_guesses}", 50, 150, RED)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    letter = event.unicode.upper()
                    if letter not in guessed_letters:
                        guessed_letters.append(letter)
                        if letter not in secret_word:
                            wrong_guesses += 1
                            if wrong_guesses >= max_wrong_guesses:
                                draw_text("Game Over!", 50, 200, RED)
                                pygame.display.flip()
                                pygame.time.wait(2000)
                                return False
                        elif all(l in guessed_letters for l in secret_word):
                            draw_text("You Win!", 50, 200, GREEN)
                            pygame.display.flip()
                            pygame.time.wait(2000)
                            return True

def main():
    total_rounds = get_rounds()
    score = 0

    for _ in range(total_rounds):
        secret_word = choice(word_list)
        if play_round(secret_word):
            score += 1

    screen.fill(WHITE)
    draw_text(f"Game Over! Final Score: {score}/{total_rounds}", 50, 150, GREEN)
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()

main()
