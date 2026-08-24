import pygame
import random

# Initialize pygame
pygame.init()

# Setup screen
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Coin Collector")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Player
player = pygame.image.load("player.png")
player = pygame.transform.scale(player, (60, 60))

player_x = 220
player_y = 400

# Coin
coin_x = random.randint(20, 450)
coin_y = random.randint(50, 350)

# Score, lives and level
score = 0
lives = 3
level = 1

# Font
font = pygame.font.Font(None, 35)

# Custom event
LEVEL_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(LEVEL_EVENT, 5000)

# Game loop
done = False

while not done:

    # Check events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True

        # Level up event
        if event.type == LEVEL_EVENT:
            level = level + 1

    # Player movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x = player_x - 5

    if keys[pygame.K_RIGHT]:
        player_x = player_x + 5

    if keys[pygame.K_UP]:
        player_y = player_y - 5

    if keys[pygame.K_DOWN]:
        player_y = player_y + 5

    # Keep player inside screen
    if player_x < 0:
        player_x = 0

    if player_x > 440:
        player_x = 440

    if player_y < 0:
        player_y = 0

    if player_y > 440:
        player_y = 440

    # Player rectangle
    player_rect = pygame.Rect(player_x, player_y, 60, 60)

    # Coin rectangle
    coin_rect = pygame.Rect(coin_x, coin_y, 30, 30)

    # Collect coin
    if player_rect.colliderect(coin_rect):
        score = score + 1

        coin_x = random.randint(20, 450)
        coin_y = random.randint(50, 400)

    # Draw background
    screen.fill(WHITE)

    # Draw coin
    pygame.draw.circle(screen, YELLOW, (coin_x, coin_y), 15)

    # Draw player
    screen.blit(player, (player_x, player_y))

    # Display information
    score_text = font.render("Score: " + str(score), True, BLACK)
    level_text = font.render("Level: " + str(level), True, BLACK)
    lives_text = font.render("Lives: " + str(lives), True, BLACK)

    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (200, 10))
    screen.blit(lives_text, (380, 10))

    # Update screen
    pygame.display.flip()

pygame.quit()