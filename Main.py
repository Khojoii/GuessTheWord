import pygame
import sys
from random import choice

# Setting up the game window
pygame.init()
WIDTH, HEIGHT = 600, 400  # Dimensions of the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Create the game window
pygame.display.set_caption('Guess The Word')  # Title of the game window
clock = pygame.time.Clock()  # Clock to manage time in the game

# Defining colors
WHITE = (255, 255, 255)  # White color
BLACK = (0, 0, 0)  # Black color
RED = (255, 0, 0)  # Red color
GREEN = (0, 255, 0)  # Green color

# List of words for the game
word_list = ['funbyte', 'python', 'like', 'subscribe']  # Words that players will guess

# Font for rendering text
font = pygame.font.Font(None, 36)

# Function to render and display text on the screen
def draw_text(text, x, y, color=BLACK):
    rendered_text = font.render(text, True, color)  # Render the text
    screen.blit(rendered_text, (x, y))  # Draw the text at the specified position

# Function to get the number of rounds from the player
def get_rounds():
    input_text = ''  # Input string for the number of rounds
    while True:
        screen.fill(WHITE)  # Clear the screen with a white background
        draw_text('Enter number of rounds:', 50, 100)  # Prompt the player
        draw_text(input_text, 50, 150, RED)  # Display the current input
        pygame.display.flip()  # Update the display

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Quit the game if the close button is clicked
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:  # Handle keyboard input
                if event.unicode.isdigit():  # Check if the key is a digit
                    input_text += event.unicode  # Append the digit to the input string
                elif event.key == pygame.K_BACKSPACE and input_text:  # Handle backspace
                    input_text = input_text[:-1]  # Remove the last character
                elif event.key == pygame.K_RETURN and input_text.isdigit():  # Confirm input
                    return int(input_text)  # Return the number of rounds as an integer

# Function to play a single round
def play_rounds(secret_word):
    guessed_letters = []  # List of guessed letters
    wrong_guesses = 0  # Counter for wrong guesses
    max_wrong_guesses = 6  # Maximum allowed wrong guesses

    while True:
        screen.fill(WHITE)  # Clear the screen with a white background
        # Display the word with guessed letters or underscores
        display_word = " ".join([letter if letter in guessed_letters else "_" for letter in secret_word])
        draw_text(display_word, 50, 100)  # Draw the current state of the word
        draw_text(f'Wrong guesses: {wrong_guesses}/{max_wrong_guesses}', 50, 150, RED)  # Show the guess count
        pygame.display.flip()  # Update the display

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Quit the game if the close button is clicked
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:  # Handle keyboard input
                if event.unicode.isalpha():  # Check if the key is a letter
                    letter = event.unicode.lower()  # Convert the letter to lowercase
                    if letter not in guessed_letters:  # Check if the letter is new
                        guessed_letters.append(letter)  # Add the letter to guessed letters
                        if letter not in secret_word:  # Check if the letter is incorrect
                            wrong_guesses += 1  # Increment wrong guess count
                            if wrong_guesses >= max_wrong_guesses:  # Check if player lost
                                draw_text('Game Over!', 50, 200, RED)  # Display game over message
                                pygame.display.flip()
                                pygame.time.wait(1000)  # Wait before ending the round
                                return False  # Indicate the round was lost
                        elif all(l in guessed_letters for l in secret_word):  # Check if player won
                            # Update screen to show the full word before displaying "You Win!"
                            screen.fill(WHITE)
                            display_word = " ".join([letter if letter in guessed_letters else "_" for letter in secret_word])
                            draw_text(display_word, 50, 100)
                            draw_text(f'Wrong guesses: {wrong_guesses}/{max_wrong_guesses}', 50, 150, RED)
                            pygame.display.flip()

                            draw_text('You Win!', 50, 200, GREEN)  # Display win message
                            pygame.display.flip()
                            pygame.time.wait(2000)  # Wait before ending the round
                            return True  # Indicate the round was won

# Main function to start the game
def main():
    total_rounds = get_rounds()  # Get the number of rounds from the player
    score = 0  # Initialize the score

    for _ in range(total_rounds):  # Loop through the specified number of rounds
        secret_word = choice(word_list)  # Select a random word
        if play_rounds(secret_word):  # Play a round
            score += 1  # Increment score if the round was won

    # Display the final score
    screen.fill(WHITE)  # Clear the screen
    draw_text(f'Game Over! Final Score: {score}/{total_rounds}', 50, 150, GREEN)  # Show the score
    pygame.display.flip()
    pygame.time.wait(3000)  # Wait before exiting
    pygame.quit()  # Quit the game
    sys.exit()

main()  # Run the main function
