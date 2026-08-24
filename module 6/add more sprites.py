# Import Necessary Libraries
import pygame

# Initialize pygame
pygame.init()

# Setup window
screen = pygame.display.set_mode((400, 500))

# Load sprite
player = pygame.image.load("player.png")

# Change sprite size
player = pygame.transform.scale(player, (80, 80))

# Sprite position
x = 150
y = 200

# Create game loop
done = False

while not done:

    # Check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Background
    screen.fill((200, 200, 200))

    # Display sprite
    screen.blit(player, (x, y))

    # Update screen
    pygame.display.flip()

pygame.quit()