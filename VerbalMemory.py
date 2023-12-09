import pygame
import random

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Define screen dimensions
WIDTH = 800
HEIGHT = 600

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Verbale Memory")

# Define fonts
font_title = pygame.font.SysFont("Arial", 48)
font_text = pygame.font.SysFont("Arial", 24)

# Define game variables
sequence = []
current_index = 0
score = 0
game_over = False

# Function to show text
def show_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

# Game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Add a random word to the sequence on space key press
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not game_over:
            # Generate random word
            new_word = random.choice(["dog", "cat", "chair", "table", "tree", "house", "bike", "car", "book"])
            sequence.append(new_word)
            current_index = 0
            score += 1
            game_over = False

    # Fill the screen with black
    screen.fill(BLACK)

    # Show game title
    show_text("Verbale Memory", font_title, WHITE, WIDTH // 2, HEIGHT // 5)

    # Show score
    show_text(f"Score: {score}", font_text, WHITE, WIDTH // 2, HEIGHT // 4)

    # Check game state
    if game_over:
        show_text("Game Over!", font_title, RED, WIDTH // 2, HEIGHT // 2)
    elif current_index < len(sequence):
        # Show current word in the sequence
        show_text(sequence[current_index], font_text, GREEN, WIDTH // 2, HEIGHT // 3)

    # Update the screen
    pygame.display.flip()

    # Delay the game
    pygame.time.delay(500)

    # Check for user input
    if not game_over:
        # Get user input
        user_input = input("Enter the next word: ")

        # Check user input
        if user_input == sequence[current_index]:
            current_index += 1
        else:
            game_over = True

# Quit pygame
pygame.quit()
