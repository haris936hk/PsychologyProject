import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 30
SEQUENCE_LENGTH = 5

# Function to generate a random word
def generate_random_word():
    words = ["apple", "banana", "orange", "grape", "kiwi", "melon", "strawberry", "pineapple"]
    return random.choice(words)

# Function to display the sequence of words
def display_words(sequence, font, screen):
    screen.fill(WHITE)
    for i, word in enumerate(sequence):
        text = font.render(word, True, BLACK)
        screen.blit(text, (300, 200 + i * 50))
    pygame.display.flip()

# Function to play the Verbal Memory Game
def play_verbal_memory_game():
    sequence = [generate_random_word() for _ in range(SEQUENCE_LENGTH)]
    return sequence

# Main function
def main():
    # Set up the Pygame window
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Verbal Memory Game")

    # Set up the font
    font = pygame.font.Font(None, FONT_SIZE)

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Display the start menu
        screen.fill(WHITE)
        title_text = font.render("Verbal Memory Game", True, BLACK)
        start_text = font.render("Start Game", True, BLACK)
        screen.blit(title_text, (200, 100))
        screen.blit(start_text, (300, 300))
        pygame.display.flip()

        # Wait for the player to click the "Start Game" button
        wait_for_click = True
        while wait_for_click:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    wait_for_click = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if 300 <= x <= 500 and 300 <= y <= 350:
                        wait_for_click = False

        if not running:
            break

        # Play the game
        sequence = play_verbal_memory_game()
        display_words(sequence, font, screen)
        pygame.time.delay(5000)  # Display the words for 5 seconds

        # Clear the screen
        screen.fill(WHITE)
        pygame.display.flip()

        # Wait for a moment before restarting the loop
        pygame.time.delay(1000)

    pygame.quit()

if __name__ == "__main__":
    main()
