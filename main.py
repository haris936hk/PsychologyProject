import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Psychology Games")
clock = pygame.time.Clock()

# Fonts
font = pygame.font.Font(None, 36)


# Functions
def draw_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))


# Menu loop
menu_running = True
while menu_running:
    screen.fill(WHITE)

    draw_text("Select a Game:", BLACK, WIDTH // 4, HEIGHT // 4)

    for i, game in enumerate(["Memory Game", "Attention Game", "Reaction Time Game"]):
        draw_text(f"{i + 1}. {game}", BLACK, WIDTH // 4, HEIGHT // 2 + i * 50)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                menu_running = False

    clock.tick(FPS)

pygame.quit()
sys.exit()
