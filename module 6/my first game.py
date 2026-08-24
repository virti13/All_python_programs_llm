# Import Necessary Libraries
import pygame
import random

# Initialize required modules
pygame.init()

# Setup window geometry
screen = pygame.display.set_mode((400, 500))

# Create ball
ball_x = random.randint(0, 380)
ball_y = 0

# Create a loop to run till the game is quit
done = False

while not done:

    # Clear the event queue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Move the ball down
    ball_y = ball_y + 1

    # Draw background
    screen.fill((0, 0, 0))

    # Draw ball
    pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), 20)

    # Reset ball when it reaches the bottom
    if ball_y > 500:
        ball_y = 0
        ball_x = random.randint(0, 380)

    # Make the changes visible
    pygame.display.flip()

pygame.quit()