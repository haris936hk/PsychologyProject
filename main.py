import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1920, 1080
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BACKGROUND_COLOR = (135, 206, 250)  # Light Sky Blue
BUTTON_COLOR = WHITE
BUTTON_HOVER_COLOR = (150, 150, 150)
BUTTON_CLICK_COLOR = (100, 100, 100)
TEXT_COLOR = BLACK

# Game setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Psychology Games by Haris Khan & Furqan Qureshi")
clock = pygame.time.Clock()

# Fonts
font = pygame.font.Font(None, 36)

# Button class
class Button:
    def __init__(self, text, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = BUTTON_COLOR
        self.hover_color = BUTTON_HOVER_COLOR
        self.click_color = BUTTON_CLICK_COLOR
        self.is_hovered = False
        self.is_clicked = False

    def update(self):
        if self.is_clicked:
            target_color = self.click_color
        elif self.is_hovered:
            target_color = self.hover_color
        else:
            target_color = BUTTON_COLOR

        # Smooth color transition
        self.color = [
            int(c + (target_c - c) * 0.1)
            for c, target_c in zip(self.color, target_color)
        ]

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect, border_radius=10)
        draw_text(self.text, TEXT_COLOR, self.rect.centerx, self.rect.centery, center=True)

    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

# Functions
def draw_text(text, color, x, y, center=False, font_size=36):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    if center:
        text_rect.center = (x, y)
    else:
        text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)

# Menu loop
def main_menu():
    menu_running = True
    buttons = [
        Button("Memory Game", WIDTH // 2 - 100, HEIGHT // 2 - 75, 200, 50),
        Button("Attention Game", WIDTH // 2 - 100, HEIGHT // 2, 200, 50),
        Button("Reaction Time Game", WIDTH // 2 - 100, HEIGHT // 2 + 75, 200, 50),
    ]
    selected_button = None

    while menu_running:
        screen.fill(BACKGROUND_COLOR)

        for button in buttons:
            button.update()
            button.draw()

        pygame.display.flip()

        for event in pygame.event.get():
            selected_button, menu_running = handle_event(event, buttons, selected_button, menu_running)

        clock.tick(FPS)

    pygame.quit()
    sys.exit()

def handle_event(event, buttons, selected_button, running):
    if event.type == pygame.QUIT:
        running = False
        pygame.quit()
        sys.exit()
    elif event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:  # Left mouse button
            mouse_pos = pygame.mouse.get_pos()
            for button in buttons:
                if button.rect.collidepoint(mouse_pos):
                    selected_button = button
                    button.is_clicked = True
                    running = False  # This line ensures that the loop exits when a button is clicked
    elif event.type == pygame.MOUSEBUTTONUP:
        for button in buttons:
            button.is_clicked = False
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN and selected_button:
            running = False

    for button in buttons:
        button.check_hover(pygame.mouse.get_pos())

    return selected_button, running

# Run the main menu
if __name__ == "__main__":
    main_menu()
