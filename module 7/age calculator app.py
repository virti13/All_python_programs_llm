import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Age Calculator")

font = pygame.font.Font(None, 40)

birth_year = 2000
current_year = 2026

age = current_year - birth_year

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    title = font.render("Age Calculator", True, (0, 0, 0))
    result = font.render("Your Age: " + str(age), True, (0, 0, 0))

    screen.blit(title, (180, 100))
    screen.blit(result, (180, 180))

    pygame.display.update()

pygame.quit()