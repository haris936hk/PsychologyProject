import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Sample")

# Set up colors
black = (0, 0, 0)
red = (255, 0, 0)

# Set up the player rectangle
player_width, player_height = 50, 50
player_x, player_y = width // 2 - player_width // 2, height // 2 - player_height // 2
player_speed = 5

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Handle player input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Boundary checks to keep the player within the window
    player_x = max(0, min(player_x, width - player_width))
    player_y = max(0, min(player_y, height - player_height))

    # Clear the screen
    screen.fill(black)

    # Draw the player rectangle
    pygame.draw.rect(screen, red, (player_x, player_y, player_width, player_height))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(60)
