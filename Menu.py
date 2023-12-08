import pygame
import sys
import subprocess

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Main Menu")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Set up font
font = pygame.font.Font(pygame.font.get_default_font(), 48)  # Increased font size

def display_menu():
    screen.fill(WHITE)

    # Draw menu text
    menu_text = font.render("Main Menu", True, BLACK)
    menu_rect = menu_text.get_rect(center=(WIDTH // 2, 100))
    screen.blit(menu_text, menu_rect)

    # Draw menu options with a highlighted effect
    options = ["Play Reaction Time Test", "Play Verbal Memory Test", "Quit"]
    option_rects = []  # Fix: Added an empty list to store option_rects
    for i, option in enumerate(options, start=1):
        option_text = font.render(f"{i}. {option}", True, BLACK)
        text_rect = option_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + i * 60))
        option_rects.append(text_rect)  # Fix: Added the rect to option_rects
        # Highlight the option on hover
        if text_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, GRAY, text_rect.inflate(10, 5))
        screen.blit(option_text, text_rect)

    pygame.display.flip()

    return option_rects  # Fix: Returned option_rects

def play_reaction_time_test():
    try:
        subprocess.run(["python", "ReactionTime.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def play_verbal_memory_test():
    try:
        subprocess.run(["python", "VerbalMemory.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def main_menu():
    while True:
        option_rects = display_menu()  # Fix: Retrieve option_rects from display_menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    play_reaction_time_test()
                elif event.key == pygame.K_2:
                    play_verbal_memory_test()
                elif event.key == pygame.K_3:
                    print("Goodbye!")
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    for i, rect in enumerate(option_rects, start=1):
                        if rect.collidepoint(event.pos):
                            if i == 1:
                                play_reaction_time_test()
                            elif i == 2:
                                play_verbal_memory_test()
                            elif i == 3:
                                print("Goodbye!")
                                pygame.quit()
                                sys.exit()

if __name__ == "__main__":
    main_menu()
