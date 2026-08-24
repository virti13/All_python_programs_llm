# Import Necessary Libraries
import pygame

# Initialize pygame
pygame.init()

# Setup window
screen = pygame.display.set_mode((400, 500))

# Load sprite
player = pygame.image.load("player.png")
player = pygame.transform.scale(player, (80, 80))

# Sprite position
x = 150
y = 200

# Create custom event
MY_EVENT = pygame.USEREVENT + 1

# Set event to happen every 1 second
pygame.time.set_timer(MY_EVENT, 1000)

# Game loop
done = False

while not done:

    # Check events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True

        # Custom event
        if event.type == MY_EVENT:
            x = x + 20

    # Background
    screen.fill((200, 200, 200))

    # Display sprite
    screen.blit(player, (x, y))

    # Update screen
    pygame.display.flip()

pygame.quit()