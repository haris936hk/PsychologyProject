import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Reaction Time Test")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up font
font = pygame.font.Font(None, 36)

def display_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

def reaction_time_test():
    screen.fill(WHITE)
    pygame.display.flip()

    pygame.time.wait(1000)  # Wait for 1 second before the prompt

    screen.fill(WHITE)
    display_text("NOW!", BLACK, WIDTH // 2, HEIGHT // 2)
    pygame.display.flip()

    start_time = pygame.time.get_ticks()

    premature_input = False  # Flag to track premature input

    wait_for_input = True
    while wait_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                end_time = pygame.time.get_ticks()
                reaction_time = end_time - start_time

                if reaction_time < 0:
                    # Set the flag and break out of the loop
                    premature_input = True
                    wait_for_input = False
                else:
                    print(f"Your reaction time: {reaction_time} milliseconds")
                    wait_for_input = False

    if premature_input:
        # Display error message after the loop
        screen.fill(WHITE)
        error_text = font.render("Wait for 'NOW!' before pressing Enter!", RED, BLACK)
        screen.blit(error_text, (WIDTH // 2 - 300, HEIGHT // 2 - 20))
        pygame.display.flip()

def main():
    print("Welcome to the Reaction Time Test!")
    running = True
    while running:
        screen.fill(WHITE)

        play_again_text = font.render("Do you want to play? (Press 'Y' for yes, 'N' for no)", True, BLACK)
        screen.blit(play_again_text, (WIDTH // 2 - 250, HEIGHT // 2 - 20))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    reaction_time_test()
                elif event.key == pygame.K_n:
                    print("Thanks for playing. Goodbye!")
                    running = False

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
