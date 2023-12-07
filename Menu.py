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

# Set up font
font = pygame.font.Font(None, 36)

def display_menu():
    screen.fill(WHITE)

    menu_text = font.render("Main Menu:", True, BLACK)
    screen.blit(menu_text, (WIDTH // 2 - 100, 50))

    option1_text = font.render("1. Play Reaction Time Test", True, BLACK)
    screen.blit(option1_text, (WIDTH // 2 - 200, HEIGHT // 2 - 20))

    option2_text = font.render("2. Play Verbal Memory Test", True, BLACK)
    screen.blit(option2_text, (WIDTH // 2 - 200, HEIGHT // 2 + 20))

    option3_text = font.render("3. Quit", True, BLACK)
    screen.blit(option3_text, (WIDTH // 2 - 200, HEIGHT // 2 + 60))

    pygame.display.flip()

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
        display_menu()

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

if __name__ == "__main__":
    main_menu()
