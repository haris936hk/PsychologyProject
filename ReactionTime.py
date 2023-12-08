import pygame
import sys
import time
import random

# Initialize Pygame
pygame.init()

# Screen Setup
screen_width, screen_height = 720, 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Reaction Time Game")

# Fonts
font_large = pygame.font.SysFont("Roboto", 90)
font_medium = pygame.font.SysFont("Roboto", 40)

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)

# Texts
title = font_large.render("Reaction Time Game", True, red)
click_to_start_text = font_large.render("Click to Start", True, black)
waiting_text = font_large.render("Wait...", True, black)
click_now_text = font_large.render("Click NOW!", True, black)

# Rectangles
title_rect = title.get_rect(center=(screen_width // 2, 50))
click_to_start_rect = click_to_start_text.get_rect(center=(screen_width // 2, screen_height // 2))
waiting_rect = waiting_text.get_rect(center=(screen_width // 2, screen_height // 2))
click_now_rect = click_now_text.get_rect(center=(screen_width // 2, screen_height // 2))

# Game State
game_state = "Click to Start"

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "Click to Start":
                game_state = "Waiting"
            elif game_state == "Test Starting":
                end_time = time.time()
                game_state = "Showing Results"
            elif game_state == "Showing Results":
                game_state = "Click to Start"

    screen.fill(white)

    # Display Title
    screen.blit(title, title_rect)

    # Game State Logic
    if game_state == "Click to Start":
        screen.blit(click_to_start_text, click_to_start_rect)
    elif game_state == "Waiting":
        screen.fill(yellow)
        screen.blit(waiting_text, waiting_rect)
        pygame.display.update()

        # Introduce a delay before the test starts
        delay_time = random.uniform(1, 3)
        time.sleep(delay_time)

        game_state = "Test Starting"
        start_time = time.time()
    elif game_state == "Test Starting":
        screen.fill(green)
        screen.blit(click_now_text, click_now_rect)
    elif game_state == "Showing Results":
        reaction_time = round((end_time - start_time) * 1000)
        score_text = font_large.render(f"Speed: {reaction_time} ms", True, black)
        screen.blit(score_text, score_text.get_rect(center=(screen_width // 2, screen_height // 2)))

    pygame.display.update()
