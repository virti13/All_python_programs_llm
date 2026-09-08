import pygame
import random

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Rock Paper Scissors")

font = pygame.font.Font(None, 40)

choices = ["Rock", "Paper", "Scissors"]

player = "Rock"
computer = random.choice(choices)

# Check winner
if player == computer:
    result = "Draw!"
elif player == "Rock" and computer == "Scissors":
    result = "You Win!"
elif player == "Paper" and computer == "Rock":
    result = "You Win!"
elif player == "Scissors" and computer == "Paper":
    result = "You Win!"
else:
    result = "Computer Wins!"

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    title = font.render("Rock Paper Scissors", True, (0, 0, 0))
    player_text = font.render("You: " + player, True, (0, 0, 0))
    computer_text = font.render("Computer: " + computer, True, (0, 0, 0))
    result_text = font.render(result, True, (0, 0, 0))

    screen.blit(title, (160, 60))
    screen.blit(player_text, (180, 130))
    screen.blit(computer_text, (180, 180))
    screen.blit(result_text, (220, 250))

    pygame.display.update()

pygame.quit()