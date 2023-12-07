import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
FONT_SIZE = 30
SEQUENCE_LENGTH = 3  # Reduced for testing purposes

# Button Colors
BUTTON_NORMAL_COLOR = (0, 150, 0)
BUTTON_HOVER_COLOR = (0, 200, 0)
BUTTON_PRESS_COLOR = (0, 100, 0)

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

# Function to create a button
def draw_button(screen, rect, color, text, font):
    pygame.draw.rect(screen, color, rect)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

# Function to get user input for a given word
def get_user_input(word, font, screen):
    input_text = ""
    input_rect = pygame.Rect(300, 500, 200, 30)
    input_active = True

    # Display the first word
    screen.fill(WHITE)
    display_words([word], font, screen)

    while input_active:
        pygame.time.delay(10)  # Small delay to reduce CPU usage

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        # Clear the screen once the player starts typing
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLACK, input_rect, 2)
        text_surface = font.render(input_text, True, BLACK)
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        pygame.display.flip()

    return input_text.lower()

# Function to play the Verbal Memory Game with user input, feedback, and scoring
def play_verbal_memory_game_advanced():
    score = 0
    max_sequence_length = 5
    current_sequence_length = 2  # Starting difficulty

    while current_sequence_length <= max_sequence_length:
        sequence = [generate_random_word() for _ in range(current_sequence_length)]

        display_words(sequence, font, screen)
        pygame.time.delay(2000)  # Display each word for 2 seconds

        for word in sequence:
            user_input = get_user_input(word, font, screen)

            # Check user input against the correct word
            if user_input == word:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct word was {word}")

        print(f"Score: {score}/{current_sequence_length}")
        pygame.time.delay(2000)  # Pause for 2 seconds between sequences

        # Increase difficulty for the next sequence
        current_sequence_length += 1

    print("Game Over")
    return score

# Function to display end game report and ask for play again or exit
def end_game_report(score):
    screen.fill(GRAY)
    report_text = font.render(f"Your final score is: {score}", True, BLACK)
    feedback_text = font.render("Great job! Keep exercising your verbal memory.", True, BLACK)
    play_again_text = font.render("Press 'P' to play again or 'Q' to quit.", True, BLACK)
    
    screen.blit(report_text, (200, 200))
    screen.blit(feedback_text, (150, 250))
    screen.blit(play_again_text, (150, 300))
    pygame.display.flip()

    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    waiting_for_input = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

# Set up the Pygame window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Verbal Memory Game")

# Set up the font
font = pygame.font.Font(None, FONT_SIZE)

# Set up the button
button_rect = pygame.Rect(300, 300, 200, 50)
button_color = BUTTON_NORMAL_COLOR

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Display the start menu
    screen.fill(GRAY)
    title_text = font.render("Verbal Memory Game", True, BLACK)
    instruction_text1 = font.render("Memorize the sequence of words", True, BLACK)
    instruction_text2 = font.render("Type them in the input box below", True, BLACK)
    screen.blit(title_text, (200, 50))
    screen.blit(instruction_text1, (150, 200))
    screen.blit(instruction_text2, (150, 250))

    # Check if the mouse is over the button
    if button_rect.collidepoint(pygame.mouse.get_pos()):
        button_color = BUTTON_HOVER_COLOR
    else:
        button_color = BUTTON_NORMAL_COLOR

    # Check if the button is pressed
    if pygame.mouse.get_pressed()[0] and button_rect.collidepoint(pygame.mouse.get_pos()):
        button_color = BUTTON_PRESS_COLOR

        # Wait for the player to release the button
        while pygame.mouse.get_pressed()[0]:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        # Play the game
        score = play_verbal_memory_game_advanced()

        # Display end game report and ask for play again or exit
        end_game_report(score)

        # Clear the screen
        screen.fill(GRAY)

    # Draw the button
    draw_button(screen, button_rect, button_color, "Start Game", font)

    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(60)

pygame.quit()
