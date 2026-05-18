import pygame
import random

# Initialize pygame
pygame.init()

# Screen size
width = 600
height = 600

# Create screen
game_screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snake settings
snake_size = 10

snake_x = width // 2
snake_y = height // 2

change_x = 0
change_y = 0

# Snake body
snake_body = []
snake_length = 1

# Food position
food_x = random.randrange(0, width - snake_size, snake_size)
food_y = random.randrange(0, height - snake_size, snake_size)

# Clock
clock = pygame.time.Clock()

# Font
font = pygame.font.SysFont(None, 40)

# Score
score = 0

# Game loop
running = True

while running:

    # Game speed
    clock.tick(15)

    # Events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                change_x = -10
                change_y = 0

            elif event.key == pygame.K_RIGHT:
                change_x = 10
                change_y = 0

            elif event.key == pygame.K_UP:
                change_x = 0
                change_y = -10

            elif event.key == pygame.K_DOWN:
                change_x = 0
                change_y = 10

    # Move snake
    snake_x += change_x
    snake_y += change_y

    # Game over if wall hit
    if snake_x < 0 or snake_x >= width or snake_y < 0 or snake_y >= height:
        print("GAME OVER")
        running = False

    # Fill screen
    game_screen.fill(BLACK)

    # Draw food
    pygame.draw.rect(game_screen, RED, [food_x, food_y, snake_size, snake_size])

    # Snake head
    snake_head = []
    snake_head.append(snake_x)
    snake_head.append(snake_y)

    snake_body.append(snake_head)

    # Remove old body parts
    if len(snake_body) > snake_length:
        del snake_body[0]

    # Self collision
    for block in snake_body[:-1]:
        if block == snake_head:
            print("GAME OVER")
            running = False

    # Draw snake
    for block in snake_body:
        pygame.draw.rect(game_screen, GREEN, [block[0], block[1], snake_size, snake_size])

    # Eat food
    if snake_x == food_x and snake_y == food_y:

        food_x = random.randrange(0, width - snake_size, snake_size)
        food_y = random.randrange(0, height - snake_size, snake_size)

        snake_length += 1
        score += 1

    # Score text
    score_text = font.render("Score: " + str(score), True, WHITE)
    game_screen.blit(score_text, [10, 10])

    # Update display
    pygame.display.update()

# Quit game
pygame.quit()
quit()
