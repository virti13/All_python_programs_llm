# Import Necessary Libraries
import pygame

# Initialize pygame
pygame.init()

# Setup window
screen = pygame.display.set_mode((400, 500))

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Font
font = pygame.font.Font(None, 40)

done = False

while not done:

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Background
    screen.fill(WHITE)

    # Add rectangle
    pygame.draw.rect(screen, BLUE, (50, 100, 100, 80))

    # Add circle
    pygame.draw.circle(screen, RED, (300, 140), 40)

    # Add line
    pygame.draw.line(screen, GREEN, (50, 250), (350, 250), 5)

    # Add text
    text = font.render("My First Game", True, (0, 0, 0))
    screen.blit(text, (100, 350))

    # Update screen
    pygame.display.flip()

pygame.quit()